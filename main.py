# TODO - add documentation for readme (watch the youtube video)

# INF601 - Advanced Programming in Python

# Nathan Birkes

# Mini Project 1

import helpers as hf

def main() -> None:

    # Example: 
    # tickers_to_check = ["OKLO", "PLTR", "ASTS", "PL", "RGTI"]

    # TODO - Put 5 stock tickers in this list
    # tickers_to_check = []

    # My test - DELETE 
    tickers_to_check = ["OKLO", "PLTR", "ASTS", "PL", "RGTI"]

    
    for ticker in tickers_to_check:
        
        # Gets the 10 closing prices for the ticker.
        closing_prices = hf.get_last_10_closing_prices(ticker)
        
        # Creates and saves a chart for that ticker, using the closing prices we received.
        hf.create_chart(ticker, closing_prices)
        

if __name__ == "__main__":
    main()