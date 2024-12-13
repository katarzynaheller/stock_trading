from datetime import datetime

from trading.enums import OrderType


class Order:
    """
    Represents an buy/sell order with a specified price and quantity
    """

    def __init__(self, order_id: int, order_type: OrderType, price: float, quantity: int, ticker: Ticker):
        self.order_id = order_id
        self.ticker = ticker
        self.order_type = order_type
        self.price = price
        self.quantity = quantity
        self.timestamp = datetime.now()
    
    def update_order(self, order_type=None, price=None, quantity=None):
        if order_type:
            self.order_type=order_type
        if price:
            self.price=price
        if quantity:
            self.quantity=quantity
    
    def __str__(self):
        return f"Order(type={self.order_type}, price={self.price}, quantity={self.quantity})"
    
    
class OrderBook:
    """
    Represents an object with collection of orders for a particular investor
    """

    def __init__(self, investor_id: str, orders: list):
        self.investor_id = investor_id
        self.orders = orders or []

    def print_orderbook(self):
        buy_orders=[]
        sell_orders=[]

        if not self.orders:
            return {"buy_orders": [], "sell_orders": []}

        for order in self.orders: 
            if order.order_type == OrderType.BUY:
                buy_orders.append(order)
            else:
                sell_orders.append(order)
        
        print(f"Current orders: "
              f"sell: {sell_orders},"
              f"buy: {buy_orders}"
            )

class OrderBookHandler:
    """
    Handles the management of buy and sell orders in an order book.
    """

    def __init__(self, order: Order, order_book: OrderBook):
        self.order_book = order_book
        self.order = order
        self.order_counter = 0

    def add_order(self, order: Order, order_book: list):
        try:
            self.order_counter += 1
            order = Order(
                order_id=self.order_counter,
                ticker=order.ticker,
                order_type=order.order_type, 
                price=order.price, 
                quantity=order.quantity
            )
            order_book.append(order)
        
        except Exception as e:
            print(f"Something went wrong with adding order: {e}")

    def remove_order(self, order: Order, order_book: list):
        try:
            for existing_order in order_book:
                if existing_order.order_id == order.order_id:
                    order_book.remove(existing_order)
                    return f"Removed {existing_order.order_type} order from order book"
        except Exception as e:
                print(f"Removing order unsuccessful because: {e}")

    def cancell_all_orders(self, order_book: list):
            try:
                confirmation = input("Are you sure you want to cancel all orders? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    order_book.clear()
                    return f"All orders are cancelled. Now list of orders is: {order_book}"
                else:
                    return "Cancellation aborted. Orders remain unchanged."
            except Exception as e:
                print(f"Cancelling was impossible because {e}")

