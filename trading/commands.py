from dataclasses import dataclass

from trading.orderbook import (
    Order,
    OrderBook
)


@dataclass
class AddOrder:
    order: Order
    order_book: OrderBook

    @property
    def order_details(self) -> str:
        return f"Added {self.order} to order book"

    def execute(self):
        self.order_book.add_order(self.order, self.order_book)
        print(f"Transfer details: {self.order_details}")


@dataclass
class RemoveOrder:
    order: Order
    order_book: OrderBook

    @property
    def order_details(self) -> str:
        return f"Removed {self.order} to order book"
    
    def execute(self):
        self.order_book.remove_order(self.order, self.order_book)


@dataclass
class CancellAllOrders:
    order_book: OrderBook

    @property
    def order_details(self) -> str:
        return f"All orders cancelled from order book"
    
    def execute(self):
        self.order_book.cancell_all(self.order_book)