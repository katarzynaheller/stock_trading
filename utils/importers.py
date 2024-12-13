import csv

class TickerImporter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tickers = []

    def load_tickers(self):
        """Loads tickers from a CSV file and stores them in self.tickers."""
        try:
            with open(self.filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Follow the pattern introduced in csv file
                    self.tickers.append((row['symbol'], row['name']))
            print(f"Loaded {len(self.tickers)} tickers from {self.filepath}")
        except FileNotFoundError:
            print(f"File {self.filepath} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_ticker_data(self):
        """Returns the loaded tickers as a list of tuples."""
        return self.tickers

