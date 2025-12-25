import pandas as pd
from hmmlearn.hmm import GaussianHMM


def detect_volatility_regimes(
    volatility: pd.Series,
    n_regimes: int = 2,
) -> pd.DataFrame:
    """
    Detect volatility regimes using a Gaussian Hidden Markov Model (HMM).
    """

    vol = volatility.dropna().values.reshape(-1, 1)
    index = volatility.dropna().index

    model = GaussianHMM(
        n_components=n_regimes,
        covariance_type="full",
        n_iter=1000,
        random_state=42,
    )

    # Correct hmmlearn usage
    model.fit(vol)
    regimes = model.predict(vol)

    regime_df = pd.DataFrame(
        {
            "volatility": volatility.loc[index],
            "regime": regimes,
        },
        index=index,
    )

    return regime_df
