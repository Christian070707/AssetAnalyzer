import pytest
import pandas as pd
from DataCalculations import DataCalculations
import numpy as np

@pytest.fixture
def sample_data():
    data = pd.DataFrame({"Close": [100, 105, 104]})
    return DataCalculations(data)

def test_maximum_drawdown_logic():
    test_data = pd.DataFrame({'Close': [100, 80, 120, 90]})
    calc = DataCalculations(test_data)
    result = calc.max_drawdown_asset
    assert result == -0.25


def test_sharpe_ratio():
    test_data = pd.DataFrame({"Adj Close": [100, 101, 102, 103]})
    calc = DataCalculations(test_data)
    risk_free_rate = 0.02
    result = calc.calculate_sharpe_ratio()
    returns = test_data["Adj Close"].pct_change().dropna()
    mean_return = returns.mean() * 252
    ann_std = returns.std() * np.sqrt(252)
    expected = (mean_return - risk_free_rate) / ann_std
    assert result == pytest.approx(expected, rel=1e-4)

    """Testing edge case: Division by 0"""
    data_edge = pd.DataFrame({"Adj Close": [50, 50, 50]})
    calc_edge = DataCalculations(data_edge)
    assert calc_edge.calculate_sharpe_ratio() == 0


def test_daily_returns(sample_data):
    returns = sample_data.daily_returns()
    assert returns.iloc[0] == pytest.approx(0.05, rel=1e-4)
    assert returns.iloc[1] == pytest.approx(-0.0095238, rel=1e-4)

def test_average_daily_returns(sample_data):
    assert sample_data.average_daily_returns == pytest.approx(0.0202381, rel=1e-4)