import os
from typing import Optional

import pandas as pd
from alpha_vantage.timeseries import TimeSeries


def fetch_daily_ohlc(
    symbol: str,
    api_key: Optional[str] = None,
    outputsize: str = "compact",
) -> pd.DataFrame:
    """
    Fetch daily OHLC data for a given symbol from Alpha Vantage.

    Parameters
    ----------
    symbol : str
        Ticker symbol (e.g., 'AAPL', 'MSFT', 'SPY')
    api_key : str, optional
        Alpha Vantage API key. If None, reads from environment variable
        ALPHA_VANTAGE_API_KEY.
    outputsize : str
        'compact' (last 100 points) or 'full' (full history)

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by date with columns:
        ['open', 'high', 'low', 'close', 'volume']
    """

    api_key = api_key or os.getenv("ALPHA_VANTAGE_API_KEY")
    if api_key is None:
        raise ValueError("Alpha Vantage API key not provided.")

    ts = TimeSeries(key=api_key, output_format="pandas")

    data, _ = ts.get_daily(symbol=symbol, outputsize=outputsize)

    # Rename columns to clean names
    data = data.rename(
        columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume",
        }
    )

    # Ensure chronological order
    data = data.sort_index()

    return data
