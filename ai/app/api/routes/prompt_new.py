import uuid
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Base URL for the local ADK agent service
BASE_URL = "http://localhost:8000"

@app.route('/run_agent', methods=['POST'])
def run_agent():
    """
    This endpoint accepts a user ID, app name, and a prompt,
    then interacts with the local agent service.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    user_id = data.get('user_id')
    app_name = data.get('app_name')
    user_prompt = data.get('prompt')

    if not all([user_id, app_name, user_prompt]):
        return jsonify({"error": "Missing required fields: user_id, app_name, prompt"}), 400

    # Generate a unique session ID
    session_id = f"s_{uuid.uuid4().hex[:8]}"
    print(f"[INFO] New request received. User: {user_id}, App: {app_name}, Session: {session_id}")

    # 1. Create session
    session_url = f"{BASE_URL}/apps/{app_name}/users/{user_id}/sessions/{session_id}"
    session_payload = {
        "state": {
            "initial_key": "initial_value"
        }
    }

    try:
        print(f"[INFO] Creating session at: {session_url}")
        session_response = requests.post(session_url, json=session_payload, timeout=10)

        if session_response.status_code == 200:
            print(f"[✅] Session created: {session_id}")
        elif session_response.status_code == 400 and "already exists" in session_response.text:
            print(f"[ℹ️] Session already exists — continuing.")
        else:
            print(f"[❌] Failed to create session: {session_response.status_code} {session_response.text}")
            return jsonify({
                "error": "Failed to create session",
                "details": session_response.text
            }), 500

        # 2. Send prompt
        run_url = f"{BASE_URL}/run"
        run_payload = {
            "app_name": app_name,
            "user_id": user_id,
            "session_id": session_id,
            "new_message": {
                "role": "user",
                "parts": [
                    {"text": user_prompt}
                ]
            }
        }

        print(f"[INFO] Sending prompt to: {run_url}")
        run_response = requests.post(run_url, json=run_payload, timeout=30)

        if run_response.status_code == 200:
            print("[✅] Prompt sent successfully.")
            return jsonify({
                "message": "Agent run successful",
                "session_id": session_id,
                "events": run_response.json()
            }), 200
        else:
            print(f"[❌] Failed to send prompt: {run_response.status_code} {run_response.text}")
            return jsonify({
                "error": "Agent failed to respond",
                "details": run_response.text
            }), 500

    except requests.exceptions.RequestException as e:
        print(f"[❌] Network error: {e}")
        return jsonify({"error": "Connection failed to agent service"}), 503

if __name__ == '__main__':
    app.run(debug=True, port=9003)
