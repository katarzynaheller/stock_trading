from abc import ABC
from collections import defaultdict
from .orderbook import Order


class Ticker(ABC):
    """
    Abstract class with a common ticker template needed to represent Holding objects
    """
    def __init__(self, symbol: str, name: str):
        self.symbol=symbol
        self.name=name
        ...


class Portfolio:
    """
    Represents an investor's portfolio of purchased holdings
    """

    def __init__(self, tickers: list, investor_id: str, order_book=None):
        self.investor_id = investor_id
        self.tickers = tickers
        self.holdings = self._initialize_holdings()
        self.order_book = order_book

    def _initialize_holdings(self) -> defaultdict:
        """
        Creates the initial holdings defaultdict based on the loaded tickers.

        Returns:
            defaultdict: A defaultdict where each key is a ticker symbol and the value
                         is a dictionary with `name` and `quantity` set to 0.
                         example: {
                                    'AAPL': {'name': 'Apple', 'quantity': 0},
                                    'GOOGL': {'name': 'Alphabet', 'quantity': 0}
                                }
        """
        holdings = defaultdict(lambda: {'name': '','quantity':0})
        for symbol, name in self.tickers:
            holdings[symbol]['name'] = name
            holdings[symbol]['quantity'] = 0
        return holdings
    
    def update_portfolio(self, successfull_order: Order):
        holding_symbol = successfull_order.ticker.symbol
        holding_name = successfull_order.ticker.name

        if holding_symbol not in self.holdings.keys():
            self.tickers.append((holding_symbol, holding_name))

        self.holdings[holding_symbol]['name']=holding_name
        self.holdings[holding_symbol]['quantity']+=successfull_order.quantity
        
        print(f"Added new ticker {holding_symbol} with {successfull_order.quantity} to portfolio")

    def print_portfolio(self):
        print("Current holdings:")
        for symbol, data in self.holdings.items():
            print(f"{symbol}: {data['quantity']}") 

