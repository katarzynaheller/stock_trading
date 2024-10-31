from datetime import datetime
from trading.importers import TickerImporter
from trading.enums import (
    OrderType,
    ActionType
)

class Order:
    """
    Object describing order attributes with order methods
    """
    def __init__(self, order_id: int, order_type: OrderType, price: float, quantity: int):
        self.order_id = order_id
        self.order_type = order_type
        self.price = price
        self.quantity = quantity
        self.timestamp = datetime.now()
    
    def update_order(self, order_type=None, price=None, quantity=None):
        if order_type:
            self.order_type=order_type
        if price:
            self.price=price
        if quantity:
            self.quantity=quantity
    
    def __repr__(self):
        return f"{self.order_type} Order(price={self.price}, quantity={self.quantity})"
    

class Portfolio:
    """
    Object to track an investor's holdings 
    """
    def __init__(self, tickers):
        self.tickers = tickers
        self.holdings = {}

    def update_portfolio(self, quantity: int, ticker_symbol: str):
        ticker = next((t for t in self.tickers if t['symbol'] == ticker_symbol), None)

        if ticker:
            if ticker_symbol in self.holdings:
                self.holdings[ticker_symbol] += quantity
            else:
                self.holdings[ticker_symbol] = quantity
        else:
            new_ticker = {'symbol': ticker_symbol, 'name': ticker_symbol}
            self.tickers.append(new_ticker)
            self.holdings[ticker_symbol] = {
                'name': ticker_symbol,
                'quantity': quantity
            }
            print(f"Added new ticker {new_ticker} with {quantity} to portfolio")

    def print_portfolio(self):
        print("Current holdings:")
        for symbol, data in self.holdings.items():
            quantity = data if isinstance(data, int) else data.get('quantity', 0)
            print(f"{symbol}: {quantity}") 


class OrderBook:
    """
    Object storing collection of orders
    """
    def __init__(self, investor_id: int):
        self.investor_id = investor_id
        self.buy_orders = []
        self.sell_orders = []
        self.order_counter = 0
        self.portfolio = Portfolio(tickers)

    def handle_order(self, order_id: int, order_type: OrderType, action: ActionType, price: float, quantity: int):
        order_list = self.buy_orders if order_type == OrderType.BUY else self.sell_orders

        if action == ActionType.ADD:
            self.order_counter += 1
            order = Order(
                order_id=self.order_counter,
                order_type=order_type, 
                price=price, 
                quantity=quantity
            )
            order_list.append(order)
            print(f"Added {order.order_type} order: {order.quantity} @ {order.price}")
        
        elif action == ActionType.REMOVE:
            for existing_order in order_list:
                if existing_order.order_id == order_id:
                    order_list.remove(existing_order)
                    print(f"Removed {existing_order.order_type} order: {existing_order.quantity} @ {existing_order.price}")
                    break
            else:
                print(f"No matching {order_type} order found to remove.")

        elif action == ActionType.MODIFY:
            for existing_order in order_list:
                if existing_order.order_id == order_id:
                    existing_order.update_order(
                        order_type=order_type,
                        price=price,
                        quantity=quantity
                    )
                    print(f"Updated order: {existing_order}")
            else:
                print(f"Unsuccessful update")
        
        elif action == ActionType.CANCEL_ALL:
            order_list.clear()
            print(f"All orders are cancelled")
        else:
            raise ValueError("Invalid action.")

    def match_orders(self):
        """Logic to track external trading system"""
        pass


if __name__ == "__main__":
    importer = TickerImporter('tickers.csv')
    importer.load_tickers()

    tickers = importer.get_ticker_data()
    Portfolio(tickers=tickers)