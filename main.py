from trading.orderbook import Order, OrderBook
from trading.controller import OrderBookController
from trading.commands import AddOrder, RemoveOrder, CancellAllOrders
from utils.enums import OrderType
from utils.importers import TickerImporter

def main():
    

    importer = TickerImporter('tickers.csv')
    importer.load_tickers()
    tickers = importer.get_ticker_data()

    # Create OrderBook object:
    order_book = OrderBook(investor_id=1)
    controller = OrderBookController()

    #Create Order instance:
    order_one = Order(order_type=OrderType.BUY, price=1.2, quantity=10, ticker=('XYZ', "Xam Yan Zu"))
    order_two = Order(order_type=OrderType.BUY, price=2.5, quantity=20, ticker=('ZYA', "Zam YA"))


    #Execute actions:
    controller.execute(AddOrder(order_book=order_book, order=order_one))
    controller.execute(AddOrder(order_book=order_book, order=order_two))

    controller.execute(RemoveOrder(order_book=order_book, order=order_one))

    print(order_book.show_orderbook)
    
if __name__ == "__main__":
    main()
    