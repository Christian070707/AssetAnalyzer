from DataLoader import DataLoader
from DataCalculations import DataCalculations
from PortfolioVisualisations import DataVisualizer


#portfolio class zodat ik niet voor elk aandeel aparte object hoe te maken loader1 en loader2

# def main():
#     the_loader = DataLoader("AAPL", "2018-01-01", "2020-12-31")
#     the_loader2 = DataLoader("NVDA", "2018-01-01", "2020-12-31")
#
#     price_data = the_loader.get_price_data(["Close", "Volume"])
#     price_data2 = the_loader2.get_price_data(["Close", "Volume"])
#
#     calculator = DataCalculations(price_data)
#     calculator2 = DataCalculations(price_data2)
#
#     print("daily returns:", calculator.daily_returns(), "\n")
#     print("Average daily returns:", calculator.calculate_average_daily_returns(), "\n")
#     print("Annual return:", calculator.calculate_total_return(), "\n")
#     print("Min value:", calculator.calculate_minimum_return(), "\n")
#     print("Min value:", calculator.calculate_minimum_value(), "\n")
#
#
#     print("Price data:\n", price_data)
#     print("Price data:\n", price_data2)
#
#     print("CAGR:", calculator.calculate_compound_annual_growth())
#     print("Daily std: ", calculator._calculate_daily_standard_deviation())
#
#     print("Annual std: ", calculator.calculate_annual_standard_deviation())
#     print("Annual std: ", calculator2.calculate_annual_standard_deviation())


def main():
    ticker = "TSLA"
    loader = DataLoader(ticker, "2020-01-01", "2026-01-01")
    raw_df = loader.clean_price_data()

    calc = DataCalculations(raw_df)

    visualizer = DataVisualizer(calc, ticker)

    visualizer.plot_price_trend()
    print(loader.cleaned_price_data)
    visualizer.plot_returns_distribution()


if __name__ == "__main__":
    main()