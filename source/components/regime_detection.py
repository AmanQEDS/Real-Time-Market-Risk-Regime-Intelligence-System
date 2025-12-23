import pandas as pd
from arch import arch_model


def fit_garch_model(
    returns: pd.Series,
    p: int = 1,
    q: int = 1,
    dist: str = "normal"
) -> pd.Series:
    """
    Fit a GARCH(p, q) model to log returns and return conditional volatility.

    Parameters
    ----------
    returns : pd.Series
        Log return series
    p : int
        Order of ARCH term
    q : int
        Order of GARCH term
    dist : str
        Distribution assumption ('normal', 't', etc.)

    Returns
    -------
    pd.Series
        Conditional volatility series
    """
    # GARCH models expect returns in percentage terms
    returns_pct = returns * 100

    model = arch_model(
        returns_pct,
        vol="GARCH",
        p=p,
        q=q,
        dist=dist,
        rescale=False
    )

    fitted_model = model.fit(disp="off")

    conditional_volatility = fitted_model.conditional_volatility / 100

    return conditional_volatility
