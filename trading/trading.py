from trading.utils.importers import TickerImporter
from trading.orderbook import OrderBook
from trading.portfolio import Portfolio


class StockTradingHandler:

    def __init__(self, order_book: OrderBook, portfolio: Portfolio):
        self.order_book = order_book
        self.portfolio = portfolio

    def connect(self):
        """Logic to connect to external trading system """
        pass

    def match_orders(self):
        """Logic to monitor market prices and execute command when demanded conditions are met.
        Consider using FIFO LIFO or RANDOM algorithm in implementation"""
        pass

    def update_portfolio(self):
        """Logic to add successfully bought holdings to investors portfolio"""
        pass