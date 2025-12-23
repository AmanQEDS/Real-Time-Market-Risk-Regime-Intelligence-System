import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM


def detect_volatility_regimes(
    volatility: pd.Series,
    n_regimes: int = 2,
    covariance_type: str = "diag",
    n_iter: int = 1000
) -> pd.DataFrame:
    """
    Detect market regimes using Hidden Markov Model on volatility.

    Parameters
    ----------
    volatility : pd.Series
        Volatility series (e.g., GARCH conditional volatility)
    n_regimes : int
        Number of hidden regimes
    covariance_type : str
        Covariance type for HMM ('diag', 'full')
    n_iter : int
        Maximum number of iterations for convergence

    Returns
    -------
    pd.DataFrame
        DataFrame with columns:
        ['volatility', 'regime']
    """

    # Prepare data for HMM (must be 2D)
    X = volatility.values.reshape(-1, 1)

    hmm = GaussianHMM(
        n_components=n_regimes,
        covariance_type=covariance_type,
        n_iter=n_iter,
        random_state=42
    )

    hmm.fit(X)

    hidden_states = hmm.predict(X)

    regime_df = pd.DataFrame(
        {
            "volatility": volatility.values,
            "regime": hidden_states
        },
        index=volatility.index
    )

    return regime_df
