import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def validate_logs(df, gap_threshold_seconds=20):
    issues = []

    for service, group in df.groupby("service"):
        group = group.sort_values("timestamp")

        # timestamp gaps
        gaps = group["timestamp"].diff().dt.total_seconds()
        gap_count = (gaps > gap_threshold_seconds).sum()

        # sequence issues
        starts = (group["event_type"] == "START").sum()
        stops = (group["event_type"] == "STOP").sum()

        issues.append({
            "service": service,
            "large_time_gaps": int(gap_count),
            "start_stop_mismatch": abs(starts - stops)
        })

    report = pd.DataFrame(issues)
    logging.info("Validation completed")
    return report
