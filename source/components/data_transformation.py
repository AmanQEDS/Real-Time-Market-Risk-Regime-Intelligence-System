import numpy as np
import pandas as pd


def clean_price_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw OHLCV price data.

    Steps:
    - Sort by date
    - Forward-fill missing values

    Parameters
    ----------
    df : pd.DataFrame
        Raw OHLCV data indexed by date

    Returns
    -------
    pd.DataFrame
        Cleaned OHLCV data
    """
    df = df.sort_index()
    df = df.ffill()
    return df


def compute_log_returns(price_series: pd.Series) -> pd.Series:
    """
    Compute log returns from a price series.

    Parameters
    ----------
    price_series : pd.Series
        Series of prices (e.g., closing prices)

    Returns
    -------
    pd.Series
        Log return series
    """
    log_returns = np.log(price_series / price_series.shift(1))
    return log_returns.dropna()


def transform_ohlc_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full transformation pipeline:
    - Clean raw data
    - Extract close prices
    - Compute log returns

    Parameters
    ----------
    df : pd.DataFrame
        Raw OHLCV data

    Returns
    -------
    pd.DataFrame
        DataFrame with 'close' prices and 'log_returns'
    """
    df = clean_price_data(df)

    close_prices = df["close"]
    log_returns = compute_log_returns(close_prices)

    transformed_df = pd.DataFrame({
        "close": close_prices.loc[log_returns.index],
        "log_returns": log_returns
    })

    return transformed_df
