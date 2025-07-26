from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, OrderType, TimeInForce
from alpaca.trading.requests import GetOrdersRequest
from get_all_orders import get_all_orders_for_symbol
from config import API_KEY, SECRET_KEY

trade_api_url = None
trade_api_wss = None
data_api_url = None
stream_data_wss = None

client = TradingClient(api_key=API_KEY, secret_key=SECRET_KEY, paper=True, url_override=trade_api_url)


def cancel_last_order(order_id: str = None):
    """
    Cancels the most recent open order.

    Returns:
        str: Confirmation message for the canceled order or a message if no open orders exist.
    """
    # orders = get_all_orders_for_symbol(symbol=symbol)
    # if not orders:
    #     return "No open orders to cancel."
    # last_order = orders[0]
    return client.cancel_order_by_id(order_id)