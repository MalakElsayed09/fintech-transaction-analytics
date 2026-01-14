import pandas as pd

# Step 1: Define PayZero logic
def calculate_card_price(base_price, fee_rate):
    return round(base_price * (1 + fee_rate), 2)

# Step 2: Load test cases
df = pd.read_csv("payzero_tests_500plus.csv")


# Step 3: Run calculations
df["calculated_card_price"] = df.apply(
    lambda row: calculate_card_price(row["base_price"], row["fee_rate"]),
    axis=1
)


# Step 4: Validate results
df["pass"] = df["calculated_card_price"] == df["expected_card_price"]

print("PayZero validation results:")
print(df)
print()


# Step 5: Assert correctness
assert df["pass"].all(), "❌ PayZero validation failed!"

print("✅ All PayZero test cases passed successfully.")
