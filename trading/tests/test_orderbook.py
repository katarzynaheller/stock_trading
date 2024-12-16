import unittest
from trading.controller import OrderBookController
from trading.commands import AddOrder
from trading.orderbook import Order, OrderBook
from utils.enums import OrderType
from trading.portfolio import Ticker


class TestOrderBook(unittest.TestCase):

    def setUp(self):
        self.order_book = OrderBook(investor_id="123")
        self.order_one = Order(order_type=OrderType.BUY, price=100.0, quantity=10, ticker=Ticker("AAPL", "Apple Inc."))
        self.order_two = Order(order_type=OrderType.BUY, price=50.0, quantity=13, ticker=Ticker("AMZN", "Amazon.com, Inc."))
        
    def test_add_and_remove_order(self):
        self.order_book.add(self.order_one)
        self.assertEqual(len(self.order_book.order_book), 1)
        
        # Remove order
        self.order_book.remove(self.order_one)
        self.assertEqual(len(self.order_book.order_book), 0)

        
if __name__ == '__main__':
    unittest.main()