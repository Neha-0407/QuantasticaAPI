import time
from alpaca.trading.enums import OrderSide
from cancel_order import cancel_last_order
from place_order import place_order
from update_order import update_order
from get_all_orders import get_all_orders_for_symbol

def main():
    symbol = "GOOG"
    print("Placing a market order...")
    place_result = place_order(
        symbol=symbol,
        qty=1,
        side=OrderSide.BUY.value,
        order_type="market"
    )
    print(place_result)

    print("Updating the order...")

    time.sleep(2)

    # Fetch all orders to see the current state
    print(get_all_orders_for_symbol(symbol='GOOG'))

    update_result = update_order(
        symbol=symbol,
        new_qty=2,
        new_price=None,
        order_type="market"
    )
    print(update_result)

    # Step 3: Cancel the last order
    print("Canceling the last order...")
    order_id="1a01049a-49c3-4b1f-8428-a327ccaffec2"
    cancel_result = cancel_last_order(order_id)
    print(cancel_result)


if __name__ == "__main__":
    main()
