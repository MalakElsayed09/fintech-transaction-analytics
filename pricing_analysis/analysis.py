import pandas as pd

# -----------------------------
# Step 1: Load transaction data
# -----------------------------
df = pd.read_csv("transactions.csv")

# -----------------------------
# Step 2: Calculate processing fee per transaction
# -----------------------------
df["fee"] = df["amount"] * (df["fee_percent"] / 100)

# -----------------------------
# Step 3: Total fees per merchant
# -----------------------------
merchant_fees = (
    df.groupby("merchant_id")["fee"]
    .sum()
    .reset_index()
)

print("Total fees per merchant:")
print(merchant_fees)
print()

# -----------------------------
# Step 4: Average fee percent by pricing model
# -----------------------------
avg_pricing = df.groupby("pricing_model")["fee_percent"].mean()

print("Average fee percent by pricing model:")
print(avg_pricing)
print()

# -----------------------------
# Step 5: Compare Tiered vs Interchange per merchant
# -----------------------------
tiered = df[df["pricing_model"] == "tiered"]
interchange = df[df["pricing_model"] == "interchange"]

tiered_avg = tiered.groupby("merchant_id")["fee_percent"].mean()
interchange_avg = interchange.groupby("merchant_id")["fee_percent"].mean()

comparison = pd.concat([tiered_avg, interchange_avg], axis=1)
comparison.columns = ["tiered_fee_percent", "interchange_fee_percent"]

# -----------------------------
# Step 6: Identify overpaying merchants (>10%)
comparison["overpaying"] = (
    (comparison["tiered_fee_percent"].notna()) &
    (comparison["interchange_fee_percent"].notna()) &
    (comparison["tiered_fee_percent"] > comparison["interchange_fee_percent"] * 1.10)
)

# Replace NaN with 'N/A' for readability
comparison = comparison.fillna("N/A")

# Reset index for clean CSV output
comparison = comparison.reset_index()

print("Pricing comparison per merchant:")
print(comparison)
print()

# -----------------------------
# Step 7: Export recommendations
# -----------------------------
comparison.to_csv("pricing_recommendations.csv", index=False)

print("Saved pricing_recommendations.csv successfully.")
