import pytest
import pandas as pd
from DataCalculations import DataCalculations
import numpy as np

@pytest.fixture
def sampledata():
    data = pd.DataFrame({"Adj Close": [100, 105, 104]})
    return DataCalculations(data)


# @pytest.fixture
# def sample_data():
#     """Maakt een simpel dataframe voor de tests."""
#     # We gebruiken simpele getallen zodat we de returns makkelijk kunnen raden
#     data = pd.DataFrame({"Close": [100, 110, 104.5]})
#     # Dag 1 -> 2: +10% (0.10)
#     # Dag 2 -> 3: -5% (-0.05)
#     return DataCalculations(data)

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


def test_daily_returns(sample_data):
    returns = sample_data.daily_returns()
    assert returns.iloc[0] == pytest.approx(0.05)
    assert returns.iloc[1] == pytest.approx(-0.0096)


# def test_daily_returns(sample_data):
#     returns = sample_data.daily_returns()
#
#     # We verwachten [0.10, -0.05]
#     assert returns.iloc[0] == pytest.approx(0.10)
#     assert returns.iloc[1] == pytest.approx(-0.05)
#
#
# def test_average_daily_returns(sample_data):
#     # (0.10 + -0.05) / 2 = 0.025
#     assert sample_data.average_daily_returns == pytest.approx(0.025)
#
#
# def test_sharpe_ratio_zero_volatility():
#     # Test een 'edge case': wat als de prijs niet verandert?
#     data = pd.DataFrame({"Close": [100, 100, 100]})
#     calc = DataCalculations(data)
#     # De std is 0, dus de functie moet 0 teruggeven (zoals je geprogrammeerd hebt)
#     assert calc.calculate_sharpe_ratio() == 0