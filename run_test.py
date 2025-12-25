from source.components.data_ingestion import fetch_daily_ohlc
from source.components.data_transformation import transform_ohlc_data
from source.components.risk_metrics import compute_risk_metrics

print("Fetching data...")
df_raw = fetch_daily_ohlc("AAPL", outputsize="compact")
print(df_raw.head())

print("\nTransforming data...")
df_transformed = transform_ohlc_data(df_raw)
print(df_transformed.head())

print("\nComputing risk metrics...")
risk_df = compute_risk_metrics(df_transformed)
print(risk_df.head())

print("\nSUCCESS: All steps executed")
