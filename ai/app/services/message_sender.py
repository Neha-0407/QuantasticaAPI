from flask import Flask, request
from twilio.rest import Client
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
from ..agents.trade_execution.trade_execution_agent.subagents.place_order_agent.place_order_tool import place_order
app = Flask(__name__)
CORS(app)

# Use environment variables for security (recommended)
TWILIO_ACCOUNT_SID = 'AC085fe07b1be21eb42fe86dd1b82d75b4'
TWILIO_AUTH_TOKEN = 'a31e7368c28eefc27f697d46a162daa6'
FROM_WHATSAPP = 'whatsapp:+14155238886'
TO_WHATSAPP = 'whatsapp:+918451920618'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Global dictionary to keep the last trade sent
last_trade = {}

@app.route('/send_alert', methods=['POST'])
def send_trade_alert():
    data = request.json
    last_trade['symbol'] = data['symbol']
    last_trade['price'] = data['price']
    last_trade['quantity'] = data['quantity']
    last_trade['order'] = data['order']
    message = f"""
📢 *Trade Alert: {data['symbol']}*
Price: ${data['price']}
Quantity: {data['quantity']} shares
Action suggested: {data['order']}
Reply *yes* to confirm execution.
"""

    client.messages.create(
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP,
        body=message
    )
    return {"status": "success", "message": "Alert sent successfully"}, 200

@app.route("/webhook", methods=["POST"])
def receive_reply():
    incoming_msg = request.form.get("Body")         # User's message text
    sender = request.form.get("From")               # WhatsApp number that sent it
    recipient = request.form.get("To")              # Your Twilio number
    message_sid = request.form.get("MessageSid")    # Unique ID for message

    print(f"Incoming message: {incoming_msg} from {sender}")

    if incoming_msg == 'yes':
        # Simulate API call or trade execution
        # place_order(
        #     "symbol": last_trade['symbol'],
        #     "qty": last_trade['quantity'],
        #     "side": last_trade['order'],
        #     "order_type": "market",
        # )
        place_order(symbol=last_trade['symbol'], qty=last_trade['quantity'], side=last_trade['order'], order_type='market')
    return {}, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)