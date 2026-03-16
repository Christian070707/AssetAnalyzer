import streamlit as st
from DataLoader import DataLoader
from DataCalculations import DataCalculations
from PortfolioVisualisations import DataVisualizer
from datetime import date

st.set_page_config(page_title="Stock Analytics Dashboard", layout="wide")

#Title
st.title("Stock analysis")

#Sidebar
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Ticker", value="NVDA")
start_date = st.sidebar.text_input("Start Date", value="2020-01-01")
end_date = st.sidebar.text_input("End Date", value= date.today())
risk_free_rate = st.sidebar.number_input("Risk Free Rate", value=0.02)


#Making the objects
loader = DataLoader(ticker, str(start_date), str(end_date))
raw_df = loader.clean_price_data()
calc = DataCalculations(raw_df)
viz = DataVisualizer(calc, ticker)

#Making the figures
fig_price = viz.plot_price_trend()
fig_hist = viz.plot_returns_distribution()

#Key indicators
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Compound Annual Growth Rate (CAGR)", f"{calc.compound_annual_growth:.2f}%")

with col2:
    st.metric("Annual Standard Deviation", f"{calc.annual_standard_deviation:.2f}%")

with col3:
    st.metric("Average Daily Return", f"{calc.average_daily_returns:.2%}")

with col4:
    st.metric("Sharpe Ratio", f"{calc.calculate_sharpe_ratio(risk_free_rate):.2f}")

with col5:
    st.metric("Max Drawdown", f"{calc.max_drawdown_asset:.2f}%")

#Plotting the graphs
st.plotly_chart(fig_price)
st.plotly_chart(fig_hist)

