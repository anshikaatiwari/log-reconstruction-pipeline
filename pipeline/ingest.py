import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

REQUIRED_COLUMNS = ["timestamp", "service", "event_type", "latency_ms"]

def ingest_logs(path):
    df = pd.read_csv(path)

    missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    logging.info(f"Ingested {len(df)} raw log records")
    return df
