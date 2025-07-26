CANCEL_ORDER_PROMPT = """
Agent Role: cancel_order_agent
Task: Cancel a trading order.
Inputs: order_id (str) or symbol (optional, for last order)
Process: Attempt to cancel the specified order. If no order_id is given, cancel the last open order.
Output: A confirmation message.
"""