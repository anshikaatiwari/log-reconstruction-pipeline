import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_event_volume(df, output_dir="plots"):
    os.makedirs(output_dir, exist_ok=True)

    temp = df.copy()
    temp["minute"] = temp["timestamp"].dt.floor("T")
    counts = temp.groupby("minute").size()

    plt.figure()
    counts.plot()
    plt.title("Event Volume Over Time")
    plt.xlabel("Time")
    plt.ylabel("Number of Events")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/event_volume.png")
    plt.close()


def plot_errors_by_service(df, output_dir="plots"):
    os.makedirs(output_dir, exist_ok=True)

    error_counts = (
        df[df["event_type"] == "ERROR"]
        .groupby("service")
        .size()
    )

    plt.figure()
    error_counts.plot(kind="bar")
    plt.title("Error Events by Service")
    plt.xlabel("Service")
    plt.ylabel("Error Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/errors_by_service.png")
    plt.close()


def plot_latency_distribution(df, output_dir="plots"):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure()
    df["latency_ms"].plot(kind="hist", bins=30)
    plt.title("Latency Distribution")
    plt.xlabel("Latency (ms)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/latency_distribution.png")
    plt.close()


def plot_session_durations(sessions, output_dir="plots"):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure()
    sessions["duration_sec"].plot(kind="hist", bins=30)
    plt.title("Reconstructed Session Durations")
    plt.xlabel("Duration (seconds)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/session_durations.png")
    plt.close()
