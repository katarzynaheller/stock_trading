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
    def transaction_details(self) -> str:
        return f"Added {self.order} to order book"

    def execute(self):
        self.order_book.add(self.order)
        print(f"Transfer details: {self.transaction_details}")

    def undo(self):
        self.order_book.add(self.order)
        print(f"Undid transaction: {self.transaction_details}")

    def redo(self):
        self.order_book.add(self.order)
        print(f"Redid transaction: {self.transaction_details}")


@dataclass
class RemoveOrder:
    order: Order
    order_book: OrderBook

    @property
    def transaction_details(self) -> str:
        return f"Removed {self.order} from order book"
    
    def execute(self):
        self.order_book.remove(self.order)
        print(f"Transfer details: {self.transaction_details}")

    def undo(self):
        self.order_book.remove(self.order)
        print(f"Undid transaction: {self.transaction_details}")

    def redo(self):
        self.order_book.remove(self.order)
        print(f"Redid transaction: {self.transaction_details}")


@dataclass
class CancellAllOrders:
    order_book: OrderBook

    @property
    def transaction_details(self) -> str:
        return f"All orders cancelled from order book"
    
    def execute(self):
        self.order_book.cancell_all()
        print(f"Transfer details: {self.transaction_details}")

    def undo(self):
        self.order_book.cancell_all()
        print(f"Undid transaction: {self.transaction_details}")

    def redo(self):
        self.order_book.cancell_all()
        print(f"Redid transaction: {self.transaction_details}")