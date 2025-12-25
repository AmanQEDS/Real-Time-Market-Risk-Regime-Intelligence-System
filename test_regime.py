from source.components.data_ingestion import fetch_daily_ohlc
from source.components.data_transformation import transform_ohlc_data
from source.components.risk_metrics import compute_risk_metrics
from source.components.volatility_models import fit_garch_model
from source.components.regime_detection import detect_volatility_regimes

print("Fetching data...")
df_raw = fetch_daily_ohlc("AAPL", outputsize="compact")

print("Transforming data...")
df_transformed = transform_ohlc_data(df_raw)

print("Computing risk metrics...")
risk_df = compute_risk_metrics(df_transformed)

print("Fitting GARCH model...")
garch_vol = fit_garch_model(risk_df["log_returns"])

print("Detecting regimes...")
regime_df = detect_volatility_regimes(garch_vol, n_regimes=2)

print(regime_df.head())
print("\nRegime counts:")
print(regime_df["regime"].value_counts())

print("\nSUCCESS: Regime detection completed")
