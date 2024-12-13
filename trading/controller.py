from dataclasses import dataclass

from trading.transaction import Transaction


@dataclass
class OrderBookController:
    
    def execute(self, transaction: Transaction):
        transaction.execute()
    
    