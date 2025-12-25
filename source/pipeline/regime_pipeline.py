from source.pipeline.risk_pipeline import run_risk_pipeline
from source.components.regime_detection import detect_volatility_regimes


def run_regime_pipeline(
    symbol: str,
    n_regimes: int = 2
):
    """
    End-to-end regime pipeline:
    risk pipeline → regime detection
    """

    # Run risk pipeline
    risk_df, garch_vol = run_risk_pipeline(symbol)

    # Detect regimes using GARCH volatility
    regime_df = detect_volatility_regimes(
        garch_vol,
        n_regimes=n_regimes
    )

    # Merge risk + regime information
    final_df = risk_df.copy()
    final_df["regime"] = regime_df["regime"]

    return final_df

