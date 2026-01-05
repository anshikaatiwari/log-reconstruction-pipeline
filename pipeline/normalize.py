import logging

logging.basicConfig(level=logging.INFO)

def normalize_logs(df):
    before = len(df)

    df = df.drop_duplicates()
    df = df.sort_values("timestamp")

    logging.info(f"Removed {before - len(df)} duplicate records")
    return df
