def print_missing(df):
    missing_cols = [col for col in df.columns if df[col].isnull().any()]
    for col in missing_cols:
        n_missing = df[col].isnull().sum()
        print(f"{col}: {n_missing} missing ({n_missing * 100 / len(df):.2f}%). Type: {df[col].dtype}")