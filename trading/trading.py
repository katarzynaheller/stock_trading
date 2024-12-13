from trading.portfolio import Portfolio

class StockTradingHandler:

    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio

    def connect(self):
        """Logic for connection to external trading system """
        pass

    def match_orders(self):
        """Logic for monitoring market prices and execute command when demanded conditions are met.
        Consider using FIFO LIFO or RANDOM algorithm in implementation"""
        pass

    def order_as_holding(self):
        """Logic for saving/transforming order to holding
        - check if ticker exists in uploaded list; if not update by ticker.check_ticker() method
        - update portfolio by portolio.update()
        """
        pass