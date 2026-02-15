# INF601 - Advanced Programming in Python

# Nathan Birkes

# Mini Project 1

import helpers as hf

def main() -> None:

    # Put list of tickers here: 
    tickers_to_check = ["OKLO", "PLTR", "ASTS", "PL", "RGTI"]

    # List placeholders - holds all of the data for each ticker and their respected closing prices & the dates.
    full_closing_prices_list = []
    full_dates_list = []

    for ticker in tickers_to_check:
        
        # Gets the 10 closing prices for the ticker.
        dates, closing_prices = hf.get_last_10_closing_prices(ticker)
        
        # Adding each ticker and their closing_prices to the full list & each date to the date list.
        full_closing_prices_list.append(closing_prices)
        full_dates_list.append(dates)

    # Creates and saves a chart for that ticker, using the closing prices we received.
    hf.create_charts(tickers_to_check, full_dates_list, full_closing_prices_list)
        
if __name__ == "__main__":
    main()