from dataclasses import dataclass, field

from trading.transaction import Transaction


@dataclass
class OrderBookController:
    undo_stack: list[Transaction] = field(default_factory=list)
    redo_stack: list[Transaction] = field(default_factory=list)
    
    def execute(self, transaction: Transaction) -> None:
        transaction.execute()
        self.redo_stack.clear()
        self.undo_stack.append(transaction)

    def undo(self) -> None:
        if not self.undo_stack:
            return
        transaction =  self.undo_stack.pop()
        transaction.undo()
        self.redo_stack.append()

    def redo(self) -> None:
        if not self.redo_stack:
            return
        transaction =  self.redo_stack.pop()
        transaction.undo()
        self.undo_stack.append()
    