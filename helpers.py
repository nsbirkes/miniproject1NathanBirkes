import os
import matplotlib.pyplot as mp
import numpy as np
import yfinance as yf
from datetime import datetime


def get_last_10_closing_prices(ticker: str) -> tuple[list[str], list[float]]:
    """
    Gets the last 10 trading day closing prices for a ticker passed in, using yfinance
    Returns a list of dates and a list of floats - length 10

    Params
    --------
    ticker: str
        The stocks symbols that we want to use to get the finance data from.
    
    Returns
    --------
    dates, prices: tuple[list[str], list[float]]
        A list of dates for each of the trading days we are looking at.      
        A list of 10 values for the last 10 trading days of the tickers closing prices.
    """
    
    # Downloads data for the ticker we provided
    data = yf.download(
        ticker,
        period="14d", # Getting a few extra days to prevent the .squeeze from erroring out.
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    if data.empty: # Would be an error if we can't find it on yfinance.
        raise ValueError(f"Incorrect ticker: {ticker} Try a different ticker.")

    # Retrieves the close price from the data, gets the last 10 and round to 2 decimals.
    closes = data["Close"].squeeze().dropna().tail(10).round(2)

    # Retrieves the dates for these 10 days - and format them.
    dates = closes.index.strftime("%m-%d-%y").tolist()
    prices = closes.tolist()

    return dates, prices


def create_charts(
        tickers_to_check: list[str],
        full_dates_list: list[list[str]],
        full_closing_prices_list: list[list[float]]
    ) -> None:

    """
    Creates and saves a chart for each ticker.

    Params
    --------
    tickers_to_check: list[str]
        List of the tickers we passed in.
    full_dates_list: list[list[str]],
        Dates for the last 10 trading days.
    full_closing_prices_list: list[list[float]]
        Closing prices for the last 10 trading days on the ticker we passed in.
    """

    # Going into the charts folder to save the images.
    os.chdir("charts/")

    # Checking to make sure we have a list for each ticker. Otherwise our data would be inaccurate.
    if len(tickers_to_check) != len(full_closing_prices_list):
        raise ValueError(f"Tickers list length: {len(tickers_to_check)} must match full_closing_prices_list length: {len(full_closing_prices_list)}.")

    # Sets each list to a numpy array, and will create + save the charts for each ticker.
    for ticker, dates_list, closing_price_list in zip(tickers_to_check, full_dates_list, full_closing_prices_list):
        
        # convert python list to a numpy array
        closes_np = np.array(closing_price_list, dtype=float)

        mp.figure(figsize=(10, 6)) # creates the figure
        mp.plot(dates_list, closes_np, marker="o") # sets x and y axis
        mp.title(f"{ticker} - Last 10 Trading Day Closes") # title for chart
        mp.xlabel("Trading Date") # x axis lable
        mp.ylabel("Close Price (USD)") # y axis lable
        mp.xticks(rotation=45)  # prevents x labels from being on top of eachother
        mp.grid(True) # adds gridlines

        filename = f"{ticker}_{datetime.now().strftime('%m-%d-%y')}.png"

        mp.tight_layout()
        mp.savefig(filename)
        mp.close()