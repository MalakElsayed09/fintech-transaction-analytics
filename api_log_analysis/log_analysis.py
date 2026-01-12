import json
import pandas as pd

# -----------------------------
# Step 1: Load API logs
# -----------------------------
with open("api_logs.json") as f:
    logs = json.load(f)

df = pd.DataFrame(logs)

print("API Logs:")
print(df)
print()

# -----------------------------
# Step 2: Identify issues
# -----------------------------
auth_errors = df[df["status_code"] == 401]
server_errors = df[df["status_code"] >= 500]
timeouts = df[df["response_time_ms"] > 1000]

# -----------------------------
# Step 3: Calculate uptime
# -----------------------------
uptime = (df[df["status_code"] == 200].shape[0] / len(df)) * 100

print(f"System uptime: {uptime:.2f}%")
print()

# -----------------------------
# Step 4: Report findings
# -----------------------------
print("Findings:")
print(f"- Authentication errors (401): {len(auth_errors)}")
print(f"- Server errors (5xx): {len(server_errors)}")
print(f"- Timeout risks (>1000 ms): {len(timeouts)}")
