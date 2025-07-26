from alpaca.trading.client import TradingClient

from ..config import API_KEY, SECRET_KEY

trade_api_url = None
trade_api_wss = None
data_api_url = None
stream_data_wss = None

client = TradingClient(api_key=API_KEY, secret_key=SECRET_KEY, paper=True, url_override=trade_api_url)


def cancel_order_by_id(order_id: str = ""):
    """
    Cancels the most recent open order.

    Returns:
        str: Confirmation message for the canceled order or a message if no open orders exist.
    """
    # orders = get_all_orders_for_symbol(symbol=symbol)
    # if not orders:
    #     return "No open orders to cancel."
    # last_order = orders[0]
    print(f"cancelling order: {order_id}")
    return client.cancel_order_by_id(order_id)