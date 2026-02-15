# TODO - add documentation for readme (watch the youtube video)

# INF601 - Advanced Programming in Python

# Nathan Birkes

# Mini Project 1

import os
import matplotlib as mp
import numpy as np
import yfinance as yf
import helpers as hf
from datetime import datetime


# Example: 
# tickers_to_check = ["OKLO", "PLTR", "ASTS", "PL", "RGTI"]

# TODO - Put 5 stock tickers in this list
# tickers_to_check = []


# My test
tickers_to_check = ["OKLO", "PLTR", "ASTS", "PL", "RGTI"]

# Testing output
for ticker in tickers_to_check:
    
    result = hf.get_last_10_closing_prices(ticker)

    print(f"Ticker: {ticker}")
    print(f"Results: {result}")
