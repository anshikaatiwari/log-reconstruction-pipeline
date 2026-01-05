import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def reconstruct_events(df):
    reconstructed = []

    for service, group in df.groupby("service"):
        stack = []

        for _, row in group.iterrows():
            if row["event_type"] == "START":
                stack.append(row)
            elif row["event_type"] == "STOP" and stack:
                start = stack.pop()
                duration = (row["timestamp"] - start["timestamp"]).total_seconds()
                reconstructed.append({
                    "service": service,
                    "start_time": start["timestamp"],
                    "end_time": row["timestamp"],
                    "duration_sec": duration
                })

    recon_df = pd.DataFrame(reconstructed)
    logging.info(f"Reconstructed {len(recon_df)} complete sessions")
    return recon_df
