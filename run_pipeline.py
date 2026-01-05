from pipeline.ingest import ingest_logs
from pipeline.normalize import normalize_logs
from pipeline.validate import validate_logs
from pipeline.reconstruct import reconstruct_events
from pipeline.metrics import generate_metrics

RAW_PATH = "data/raw_logs.csv"

def main():
    df = ingest_logs(RAW_PATH)
    df = normalize_logs(df)

    validation_report = validate_logs(df)
    sessions = reconstruct_events(df)
    metrics = generate_metrics(df, sessions)

    df.to_csv("data/cleaned_logs.csv", index=False)
    validation_report.to_csv("data/validation_report.csv", index=False)
    sessions.to_csv("data/reconstructed_sessions.csv", index=False)

    print("\nPIPELINE SUMMARY")
    for k, v in metrics.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
