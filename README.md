### INF601 - Advanced Programming in Python
### Nathan Birkes
### Mini Project 1


# Stock Price Charts

Program that retrieves last 10 trading days closing prices and creates charts for stocks.

## Description

This project uses the yfinance library along with NumPy and Matplotlib to collect the last 10 trading day closing prices for stock tickers. The data is stored in lists, converted to NumPy arrays, and plotted into charts. Each chart is saved as a PNG file in a charts folder when the program runs.

## Getting Started

### Dependencies

* Windows 10 or later
* Python 3.10+
* Install required libraries:

```
pip install -r requirements.txt
```

### Installing

* Clone or download the repository from GitHub
* Navigate to the project folder
* Install dependencies with pip

### Executing program

* Open a terminal in the project folder
* Make sure stock tickers are listed in `main.py`
* Run:

```
python main.py
```

## Help

If the program errors, verify dependencies are installed and ticker symbols are valid.

## Authors

Nathan Birkes

## Version History

* 0.1

  * Initial Release

## License

This project is for educational use.

## Acknowledgments

* yfinance documentation
* Matplotlib documentation
* NumPy documentation
