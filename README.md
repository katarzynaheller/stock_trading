A stock_trading is a package to track trading orders for a single investor. It helps managing holdings' porfolio and execute action depending on order type. Is build with three main components.

# Order
The `Order` class is an object describing order attributes as `id`, `order_type`, `price` and `quantity`. Parameter `order_type` is introduced as enum: ADD, REMOVE, MODIFY, CANCELL_ALL

## Order Options

| Parameter  | Type      | Example      | Default value |
| ---------- | --------- | ------------ | ------------- |
| order_type | enum      | BUY, SELL    | -             |
| price      | float > 0 | 10           | -             |
| quantity   | int       | 20           | -             |


# OrderBook
OrderBook is a representation of orders for a single investor. It contains buy orders and sell orders with defined action to execute (add or remove).


## OrderBook Options

| Parameter   | Type      | Example      | Default value |
| ----------  | --------- | ------------ | ------------- |
| action      | enum      | ADD, REMOVE  | -             |
| investor_id | int       | 22           | -             |


## OrderBook methods

### handle_order
Method to execute particular operation according to given `order_type` and `action`.

### match_orders
Method representing logic that communicates with an external exchange or trading system due to track prices and match orders when given conditions will be fullfilled.

If the order can be executed (e.g. there is a market price available that matches the investor's expectations), it is added to the transaction history and the investor's portfolio balance (e.g. the amount of cash and shares) is updated. If the market price does not meet the trader's criteria, the order is postponed or canceled.

## Portfolio 
Used to track an investor's holdings (e.g., the amount of shares)

### Ticker
A unique identifier for a given holding, typically representing a stock symbol (e.g., "AAPL" for Apple Inc.).
Used to track specific assets in a portfolio.

### Holdings
A list of holdings for a given investior represented in investor's portfolio.

### Balance
Used to track an investor's wallet