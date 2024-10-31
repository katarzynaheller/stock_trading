from enum import Enum

class OrderType(Enum):
    BUY = "buy"
    SELL = "sell"


class ActionType(Enum):
    ADD = "add"
    REMOVE = "remove"
    MODIFY = "modify"
    CANCEL_ALL = "cancel_all"