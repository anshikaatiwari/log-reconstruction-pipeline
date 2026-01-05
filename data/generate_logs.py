import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

services = ["auth-service", "payment-service", "order-service"]
event_types = ["START", "STOP", "ERROR"]

start_time = datetime(2025, 1, 5, 10, 0, 0)

rows = []
current_time = start_time

for _ in range(1200):
    service = random.choice(services)
    event = random.choices(event_types, weights=[0.45, 0.45, 0.10])[0]

    latency = abs(int(np.random.normal(200, 80)))

    # simulate missing timestamps
    if random.random() < 0.05:
        timestamp = None
    else:
        current_time += timedelta(seconds=random.randint(1, 5))
        timestamp = current_time

    rows.append([timestamp, service, event, latency])

df = pd.DataFrame(rows, columns=["timestamp", "service", "event_type", "latency_ms"])

# introduce duplicates
df = pd.concat([df, df.sample(frac=0.03)], ignore_index=True)

# shuffle logs (out-of-order)
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("data/raw_logs.csv", index=False)
print("Synthetic raw logs generated.")
