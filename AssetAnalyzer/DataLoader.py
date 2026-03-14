import yfinance as yf
import pandas as pd

class DataLoader:
    def __init__(self, ticker, start_date, end_date):
        self.cleaned_price_data = None
        self.raw_data = None
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def download_price_data(self):
        self.raw_data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return self.raw_data

    def clean_price_data(self):
        if self.raw_data is None:
            self.download_price_data()

        self.cleaned_price_data = self.raw_data.dropna(how="any").copy()

        # VOEG DIT TOE: Haal de Ticker-naam laag weg
        if isinstance(self.cleaned_price_data.columns, pd.MultiIndex):
            self.cleaned_price_data.columns = self.cleaned_price_data.columns.get_level_values(0)

        return self.cleaned_price_data

    def get_price_data(self, price_column):
        if self.raw_data is None:
            self.download_price_data()

        if self.cleaned_price_data is None:
            self.clean_price_data()

        return self.cleaned_price_data[price_column]