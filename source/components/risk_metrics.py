import pandas as pd
import numpy as np


def compute_rolling_volatility(
    returns: pd.Series,
    window: int = 21
) -> pd.Series:
    """
    Compute rolling volatility from log returns.

    Parameters
    ----------
    returns : pd.Series
        Log return series
    window : int
        Rolling window size (default: 21 trading days ~ 1 month)

    Returns
    -------
    pd.Series
        Rolling volatility series
    """
    rolling_vol = returns.rolling(window=window).std()
    return rolling_vol.dropna()


def compute_drawdown(price_series: pd.Series) -> pd.Series:
    """
    Compute drawdown from a price series.

    Parameters
    ----------
    price_series : pd.Series
        Series of prices (e.g., close prices)

    Returns
    -------
    pd.Series
        Drawdown series
    """
    cumulative_max = price_series.cummax()
    drawdown = (price_series - cumulative_max) / cumulative_max
    return drawdown


def compute_risk_metrics(
    df: pd.DataFrame,
    volatility_window: int = 21
) -> pd.DataFrame:
    """
    Compute core risk metrics from transformed data.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with columns ['close', 'log_returns']
    volatility_window : int
        Window size for rolling volatility

    Returns
    -------
    pd.DataFrame
        DataFrame with risk metrics
    """
    returns = df["log_returns"]
    prices = df["close"]

    rolling_vol = compute_rolling_volatility(returns, volatility_window)
    drawdown = compute_drawdown(prices)

    risk_df = pd.DataFrame({
        "log_returns": returns.loc[rolling_vol.index],
        "rolling_volatility": rolling_vol,
        "drawdown": drawdown.loc[rolling_vol.index],
    })

    return risk_df
