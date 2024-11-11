import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from markets.models import DailyPrice, Equity_Tickers, Bond_Tickers, Forex_Tickers, Cryptocurrency_Tickers, Commodity_Tickers
from decimal import Decimal, InvalidOperation

class Command(BaseCommand):
    help = 'Populate the DailyPrice table with historical price data from yfinance'

    def handle(self, *args, **kwargs):
        # Define the asset classes and their corresponding models
        asset_class_models = {
            'equity': Equity_Tickers,
            'bond': Bond_Tickers,
            'forex': Forex_Tickers,
            'cryptocurrency': Cryptocurrency_Tickers,
            'commodity': Commodity_Tickers,
        }
        
        # List to store tickers with errors
        not_found_tickers = []

        # Loop through each asset class and its model
        for asset_class, model in asset_class_models.items():
            self.stdout.write(f"Processing {asset_class} tickers")
            tickers = model.objects.values_list('ticker', 'name')  # Get ticker and name

            # For each ticker, fetch data from yfinance
            for ticker, name in tickers:
                if ticker:  # Ensure the ticker is not empty
                    # self.stdout.write(f"Fetching data for ticker: {ticker} ({name})")
                    if not self.fetch_and_save_daily_price_data(ticker, name, asset_class):
                        # If fetching data fails, add to not_found_tickers list
                        not_found_tickers.append({'ticker': ticker, 'name': name, 'asset_class': asset_class})

        # Print the tickers that were not found
        if not_found_tickers:
            self.stdout.write("Tickers not found or encountered errors:")
            for ticker_info in not_found_tickers:
                self.stdout.write(f"{ticker_info['ticker']} - {ticker_info['name']} ({ticker_info['asset_class']})")
        else:
            self.stdout.write("All tickers processed successfully without errors.")

    def fetch_and_save_daily_price_data(self, ticker, name, asset_class):
        try:
            # Fetch historical data for the past 7 days (you can adjust the period)
            data = yf.download(ticker, start="2024-01-01", progress=False)

             # Check if data is empty, meaning no data was found for the ticker
            if data.empty:
                return False  # No data found for this ticker, add it to not_found_tickers

            # Store OHLCV data in the database using iloc for specific elements
            for i in range(len(data)):
                row = data.iloc[i]
                date = data.index[i].date()  # Convert timestamp index to date

                # Extract OHLCV data using iloc with specific indices
                open_price = float(row.iloc[0]) if pd.notna(row.iloc[0]) else None
                high_price = float(row.iloc[1]) if pd.notna(row.iloc[1]) else None
                low_price = float(row.iloc[2]) if pd.notna(row.iloc[2]) else None
                adj_close_price = float(row.iloc[3]) if pd.notna(row.iloc[3]) else None
                volume = int(row.iloc[4]) if pd.notna(row.iloc[4]) else None

                # Update or create the DailyPrice entry
                DailyPrice.objects.update_or_create(
                    date=date,
                    asset_class=asset_class,
                    ticker=ticker,
                    name=name,
                    defaults={
                        'open': open_price,
                        'high': high_price,
                        'low': low_price,
                        'adj_close': adj_close_price,
                        'volume': volume,
                    }
                )
            return True  # Data was successfully found and processed    

        except Exception as e:
            self.stdout.write(f"Error fetching data for ticker {ticker}: {e}")