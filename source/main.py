from source.pipeline.regime_pipeline import run_regime_pipeline


def main():
    symbol = "NIFTYBEES.NS"

    final_df = run_regime_pipeline(symbol)

    print(final_df.tail())


if __name__ == "__main__":
    main()
