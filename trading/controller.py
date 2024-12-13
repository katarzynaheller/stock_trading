from dataclasses import dataclass

from trading.orderbook import (
    Order, 
    OrderBook
)


@dataclass
class OrderController:
    order: Order
    order_book: OrderBook

    @property
    def trading_details(self) -> str:
        return f" Added {self.order} to order book"
    
    def execute(self, order: Order, order_book: OrderBook):
        order_book.execute(order)
    
    