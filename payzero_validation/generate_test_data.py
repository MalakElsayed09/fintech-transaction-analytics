import pandas as pd
import random

# Generate 500+ comprehensive test cases
test_cases = []
transaction_id = 1

# 1. Standard pricing range (200 cases)
for i in range(200):
    base = round(random.uniform(5.00, 150.00), 2)
    fee = round(random.uniform(0.025, 0.035), 3)
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# 2. Edge cases - Very low prices (50 cases)
for i in range(50):
    base = round(random.uniform(0.01, 5.00), 2)
    fee = round(random.uniform(0.025, 0.035), 3)
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# 3. Edge cases - Very high prices (50 cases)
for i in range(50):
    base = round(random.uniform(500.00, 9999.99), 2)
    fee = round(random.uniform(0.025, 0.035), 3)
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# 4. Boundary fee rates - Minimum (50 cases)
for i in range(50):
    base = round(random.uniform(10.00, 100.00), 2)
    fee = 0.025  # Minimum fee
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# 5. Boundary fee rates - Maximum (50 cases)
for i in range(50):
    base = round(random.uniform(10.00, 100.00), 2)
    fee = 0.035  # Maximum fee
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# 6. Common retail prices (50 cases)
common_prices = [9.99, 19.99, 29.99, 49.99, 99.99, 14.99, 24.99, 39.99, 79.99, 149.99]
for i in range(50):
    base = random.choice(common_prices)
    fee = round(random.uniform(0.025, 0.035), 3)
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# 7. Extreme edge cases (50 cases)
edge_prices = [0.01, 0.50, 1.00, 9999.99, 5000.00, 0.99, 1.99, 2.99]
for i in range(50):
    base = random.choice(edge_prices)
    fee = round(random.uniform(0.025, 0.035), 3)
    expected = round(base * (1 + fee), 2)
    test_cases.append({
        'transaction_id': f'PZ{transaction_id:04d}',
        'base_price': base,
        'fee_rate': fee,
        'expected_card_price': expected
    })
    transaction_id += 1

# Create DataFrame
df = pd.DataFrame(test_cases)

# Save to CSV
df.to_csv('payzero_tests_500plus.csv', index=False)

print(f"✅ Generated {len(df)} test cases")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nLast 5 rows:")
print(df.tail())
print(f"\nStats:")
print(f"  - Price range: ${df['base_price'].min():.2f} - ${df['base_price'].max():.2f}")
print(f"  - Fee range: {df['fee_rate'].min():.3f} - {df['fee_rate'].max():.3f}")
print(f"\nFile saved as: payzero_tests_500plus.csv")