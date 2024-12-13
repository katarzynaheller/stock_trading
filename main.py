from trading.utils.importers import TickerImporter

def main():
    importer = TickerImporter('tickers.csv')
    importer.load_tickers()
    tickers = importer.get_ticker_data()
    print(tickers)

if __name__ == "__main__":
    main()
    