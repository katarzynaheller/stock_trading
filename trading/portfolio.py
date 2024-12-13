from abc import ABC
from collections import defaultdict


class TickerTemplate(ABC):
    """
    Abstract class with a common ticker template
    """
    def __init__(self, symbol: str, name: str):
        self.symbol=symbol
        self.name=name
        ...


class Ticker(TickerTemplate):
    """
    Pattern for storing collection of tickers is a list of tuples:
    [('AAPL', 'Apple Inc.'), ('TSLA', 'Tesla'), ...]
    """
    def __init__(self, symbol, name):
        super().__init__(symbol, name)

    def check_ticker(self, tickers: list[tuple]) -> list:
        for s, n in tickers:
            if not any(s==symbol for symbol, name in tickers):
                tickers.append((self.symbol, self.name))
            else:
                for i, (s, n) in enumerate(tickers):
                    if self.symbol==s:
                        tickers[i]=(self.name, self.symbol)
        return tickers


class Holding:
    def __init__(self, ticker: tuple, quantity: int, price: float):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price


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
        Creates the initial holdings defaultdict based on the loaded tickers 
        with `symbol` as a key and`name` and `quantity` as values
                                 {
                                    'AAPL': {'name': 'Apple', 'quantity': 0},
                                    'GOOGL': {'name': 'Alphabet', 'quantity': 0}
                                }
        """
        holdings = defaultdict(lambda: {'name': '','quantity':0})
        for symbol, name in self.tickers:
            holdings[symbol]['name'] = name
            holdings[symbol]['quantity'] = 0
        return holdings
    
    def update_portfolio(self, holding: Holding):
        ticker_symbol = holding.ticker.symbol
        ticker_name = holding.ticker.name

        if ticker_symbol not in self.holdings.keys():
            self.tickers.append((ticker_symbol, ticker_name))

        self.holdings[ticker_symbol]['name']=ticker_name
        self.holdings[ticker_symbol]['quantity']+=holding.quantity
        
        print(f"Added ticker {ticker_symbol} with {holding.quantity} to portfolio")

    def print_portfolio(self):
        print("Current holdings:")
        for symbol, data in self.holdings.items():
            print(f"{symbol}: {data['quantity']}") 

