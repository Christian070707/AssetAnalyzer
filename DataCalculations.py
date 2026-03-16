class DataCalculations:
    def __init__(self, data):
        self.df = data

        if "Adj Close" in data.columns:
            self.data = data["Adj Close"]
        elif "Close" in data.columns:
            self.data = data["Close"]
        else:
            raise ValueError("No data column found for calculations")

        self.returns = None


#   === DATA PREP ===

    def daily_returns(self):
        """
        Calculates the daily returns of a stock.

        formula:
            daily returns = (today's closing price - yesterday's closing price)/ yesterday's closing price

        daily returns can be devided into two components: Intraday returns + Overnight returns.

        Meaning/interpretation:
            meaning the difference between current and previous day's price.
        """

        """
            Calculates the daily percentage change in closing prices.

            Mathematical Formula (Simple Return):
            $R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$

            Where:
            - $R_t$: Return at time t
            - $P_t$: Price at time t
            - $P_{t-1}$: Price at previous time step

            Methodology:
            Uses the Pandas `pct_change()` method. The first row will result in NaN 
            and is removed using `dropna()` to ensure clean statistical calculations.

            Returns:
                pd.Series: A series of decimal values representing daily growth/decline.
        """
        if self.returns is None:
            if self.data.empty:
                print("No data found!")
                return None
            self.returns = self.data.pct_change().dropna()
        return self.returns

    def _calculate_running_years(self):
        """Calculates the amount of years that an investment is running"""
        running_years = (self.data.count()) / 252
        return running_years

#   === PERFORMANCE METRICS ===

    @property
    def average_daily_returns(self):
        """Calculates the mean of the daily returns."""
        if self.returns is None:
            self.daily_returns()
        return self.returns.mean()

    @property
    def annualized_average_return(self):
        return self.average_daily_returns * 252

    @property
    def total_return(self):
        """Calculates the total return between the given start and end-date."""
        total_return = (self.data.iloc[-1] - self.data.iloc[0]) / self.data.iloc[0]
        return total_return

    @property
    def compound_annual_growth(self):
        """Compound Annual Growth Rate (CAGR) measures the mean annual growth rate over a specific time longer than a year."""
        compound_annual_growth = ((self.data.iloc[-1] / self.data.iloc[0]) ** (1 / self._calculate_running_years())) - 1
        return compound_annual_growth

#   === RISK STATISTICS ===

    @property
    def daily_standard_deviation(self):
        """Calculates daily standard deviation on the given data"""
        returns = self.daily_returns()
        return returns.std()

    @property
    def annual_standard_deviation(self):
        """Calculates annual standard deviation on the given data."""
        annual_standard_deviation = self.daily_standard_deviation * (252**0.5)
        return annual_standard_deviation

    @property
    def max_drawdown_asset(self):
        cummax = self.data.cummax()
        daily_drawdown = self.data / cummax - 1
        max_drawdown = daily_drawdown.min()
        return max_drawdown


    def calculate_sharpe_ratio(self, risk_free_rate=0.02):

        returns = self.annualized_average_return
        std = self.annual_standard_deviation

        if std <= 0:
            return 0

        return (returns - risk_free_rate)/std

#   === PRICE STATISTICS ===

    @property
    def minimum_return(self):
        """Calculates the lowest value"""
        return self.returns.min()

    @property
    def maximum_return(self):
        """Calculates the Highest value"""
        return self.returns.max()

    @property
    def minimum_value(self):
        """Calculates the lowest value"""
        return self.data.min()

    @property
    def maximum_value(self):
        """Calculates the Highest value"""
        return self.data.max()









