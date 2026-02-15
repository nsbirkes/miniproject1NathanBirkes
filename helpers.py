import os
import matplotlib as mp
import numpy as np
import yfinance as yf
from datetime import datetime

def get_last_10_closing_prices(ticker: str) -> list[float]:
    """
    Gets the last 10 trading day closing prices for a ticker passed in, using yfinance
    Returns a list of floats - length 10.

    Params
    --------
    ticker: str
        The stocks symbols that we want to use to get the finance data from.
    
    Returns
    --------
    closes: list[float]
        A list of 10 values for the last 10 trading days of the tickers closing prices.
    """
    
    data = yf.download(
        ticker,
        period="14d", # Getting a few extra days to prevent the .squeeze from erroring out.
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    if data.empty: # Would be an error if we can't find it on yfinance.
        raise ValueError(f"Incorrect ticker: {ticker} Try a different ticker.")

    # Retrieve the close price from the data, get the last 10 and round to 2 decimals.
    closes = data["Close"].squeeze().dropna().tail(10).round(2)

    # if len(closes) < 10: # Delete - probably wont need it - should always have 10, and want to show it even if there isn't 10 days.
        # raise ValueError(f"Only {len(closes)} closing prices found for {ticker}")

    return closes.tolist()


def create_chart(ticker: str, closing_prices: np.array) -> None:
    pass

