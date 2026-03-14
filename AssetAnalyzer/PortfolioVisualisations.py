import plotly.graph_objects as go

class DataVisualizer:
    def __init__(self, calculation_object, ticker):
        self.ticker = ticker
        self.calc = calculation_object

    def plot_price_trend(self):

        price_data = self.calc.data
        minimum_line = self.calc.minimum_value
        maximum_line = self.calc.maximum_value

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=price_data.index,
            y=price_data,
            name=f"{self.ticker} close price",
            showlegend=True,
        ))

        fig.add_hline(
            y=minimum_line,
            annotation_text=f"Lowest stockprice {self.ticker}",
            line_color="red",
            line_dash="dash"
        )

        fig.add_hline(
            y=maximum_line,
            annotation_text=f"Highest stockprice {self.ticker}",
            line_color="green",
            line_dash='dash',
        )

        fig.update_layout(
            title=f"{self.ticker} stockprice",
            xaxis_title = "Date",
            yaxis_title = "Price $",
            template = "plotly_dark"
        )
        return fig

    def plot_returns_distribution(self):

        daily_returns = self.calc.daily_returns()
        average_daily_returns = self.calc.average_daily_returns
        standard_deviation = self.calc.daily_standard_deviation

        fig = go.Figure()

        fig.add_trace(go.Histogram(
            x=daily_returns,
            name=self.ticker,
            showlegend=True
        ))

        fig.add_vline(
            x=average_daily_returns + standard_deviation,
            annotation_text="+σ",
            line_color="white",
            line_dash='dot',
            )

        fig.add_vline(
            x=average_daily_returns - standard_deviation,
            annotation_text="-σ",
            line_color="white",
            line_dash='dot',
            )

        fig.update_layout(
            title=f"Distribution of returns from {self.ticker}",
            xaxis_title="Daily returns",
            yaxis_title="Frequency",
            template="plotly_dark"
        )
        return fig

