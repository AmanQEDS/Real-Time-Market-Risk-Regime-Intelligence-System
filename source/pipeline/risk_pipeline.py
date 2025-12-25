from source.components.data_ingestion import fetch_daily_ohlc
from source.components.data_transformation import transform_ohlc_data
from source.components.risk_metrics import compute_risk_metrics
from source.components.volatility_models import fit_garch_model


def run_risk_pipeline(
    symbol: str,
    outputsize: str = "compact",
):
    """
    Risk pipeline:
    ingestion → transformation → risk metrics → GARCH volatility
    """

    df_raw = fetch_daily_ohlc(symbol, outputsize=outputsize)

    df_transformed = transform_ohlc_data(df_raw)

    risk_df = compute_risk_metrics(df_transformed)

    garch_vol = fit_garch_model(risk_df["log_returns"])

    return risk_df, garch_vol
