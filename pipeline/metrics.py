import logging

logging.basicConfig(level=logging.INFO)

def generate_metrics(df, sessions):
    metrics = {
        "total_logs": len(df),
        "error_events": int((df["event_type"] == "ERROR").sum()),
        "avg_latency_ms": float(df["latency_ms"].mean()),
        "reconstructed_sessions": len(sessions)
    }

    logging.info("Metrics generated")
    return metrics
