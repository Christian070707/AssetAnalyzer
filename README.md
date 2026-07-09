# AssetAnalyzer

**AssetAnalyzer** is a Python-based dashboard for analyzing the historical performance and risk of a stock. It pulls price data, calculates common financial metrics, and visualizes the results in an interactive [Streamlit](https://streamlit.io/) app.

## Features

- **Data loading**: Fetches and cleans historical price data for any ticker via [`yfinance`](https://pypi.org/project/yfinance/).
- **Performance metrics**, including:
  - Compound Annual Growth Rate (CAGR)
  - Annual standard deviation (volatility)
  - Average daily return
  - Sharpe ratio (using a configurable risk-free rate)
  - Maximum drawdown
- **Visualizations**:
  - Price trend over time
  - Distribution of daily returns
- **Interactive dashboard** built with Streamlit, letting you adjust the ticker, date range, and risk-free rate on the fly.

## Project structure

| File | Description |
|---|---|
| `StreamlitApp.py` | Main entry point — launches the Streamlit dashboard. |
| `DataLoader.py` | Downloads and cleans historical price data for a given ticker. |
| `DataCalculations.py` | Computes financial metrics (CAGR, volatility, Sharpe ratio, drawdown, etc.). |
| `PortfolioVisualisations.py` | Builds the Plotly charts used in the dashboard. |
| `Notepad.py` | Scratch/notes file used during development. |
| `test_calculations.py` | Unit tests for the calculation logic. |
| `requirements.txt` | Python dependencies. |

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`:
  - `streamlit`
  - `pandas`
  - `numpy`
  - `plotly`
  - `yfinance`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Christian070707/AssetAnalyzer.git
   cd AssetAnalyzer
   ```

2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run StreamlitApp.py
```

This opens the dashboard in your browser, where you can:

1. Enter a stock **ticker** (e.g. `NVDA`).
2. Set a **start date** and **end date** for the analysis period.
3. Set a **risk-free rate** used for the Sharpe ratio calculation.

The dashboard will then display key indicators (CAGR, volatility, average daily return, Sharpe ratio, and max drawdown) alongside a price trend chart and a returns distribution chart.

## Running tests

Unit tests for the calculation logic can be run with:

```bash
python -m pytest test_calculations.py
```

## License

No license has been specified yet for this project.

## Author

Created by [Christian070707](https://github.com/Christian070707).
