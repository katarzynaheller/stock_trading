import uuid
from datetime import datetime

from utils.enums import OrderType
from trading.portfolio import Ticker

class Order:
    """
    Represents an buy/sell order with a specified price and quantity
    """
    def __init__(self, order_type: OrderType, price: float, quantity: int, ticker: Ticker):
        self.order_id = str(uuid.uuid4()) 
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
    Represents and manages a collection of buy/sell orders queued for trading 
    """

    def __init__(self, investor_id: str, orders=None):
        self.investor_id = investor_id
        self.order_book = orders or []
        self.order_counter=0

    def add(self, order: Order):
        try:
            self.order_counter += 1
            order = Order(
                ticker=order.ticker,
                order_type=order.order_type, 
                price=order.price, 
                quantity=order.quantity
            )

            self.order_book.append(order)
            return self.order_book
        
        except Exception as e:
            print(f"Something went wrong with adding order: {e}")

    def remove(self, order: Order):
        try:
            for existing_order in self.order_book:
                if existing_order.order_id == order.order_id:
                    self.order_book.remove(existing_order)
                    print(f"Removed {existing_order.order_type} order from order book")
                    return self.order_book
        except Exception as e:
                print(f"Removing order unsuccessful because: {e}")

    def cancell_all(self):
            try:
                confirmation = input("Are you sure you want to cancel all orders? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    self.order_book.clear()
                    print(f"All orders are cancelled. Now list of orders is: {self.show_orderbook}")
                    return self.order_book
                else:
                    return "Cancellation aborted. Orders remain unchanged."
            except Exception as e:
                print(f"Cancelling was impossible because {e}")


    @property
    def show_orderbook(self):
        buy_orders=[]
        sell_orders=[]

        if not self.order_book:
            return f"Order book is empty"

        for order in self.order_book: 
            if order.order_type == OrderType.BUY:
                buy_orders.append(order)
            else:
                sell_orders.append(order)
        
        return(f"Current orders: "
              f"sell: {sell_orders},"
              f"buy: {buy_orders}"
            )  