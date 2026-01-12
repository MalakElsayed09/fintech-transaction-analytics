# Transaction Pricing Analysis (FinTech Case Study)

## Overview

This project simulates a real-world fintech analysis task where transaction data is analyzed to identify merchants who may be overpaying on payment processing fees due to inefficient pricing models.

Using Python and pandas, the script automates fee calculations, compares pricing models, and generates actionable recommendations for cost optimization.

---

## Business Problem

Payment processors often offer multiple pricing models, such as:

- **Tiered pricing**
- **Interchange-plus pricing**

Some merchants unknowingly pay higher fees under tiered pricing.  
The goal of this analysis is to:

- Calculate processing fees per transaction
- Compare pricing models at the merchant level
- Identify merchants potentially overpaying by more than 10%

---

## Dataset

The dataset (`transactions.csv`) contains simulated transaction data with the following fields:

| Column Name    | Description                   |
| -------------- | ----------------------------- |
| transaction_id | Unique transaction identifier |
| merchant_id    | Merchant identifier           |
| card_type      | Credit or debit card          |
| pricing_model  | Tiered or interchange         |
| amount         | Transaction amount            |
| fee_percent    | Processing fee percentage     |
| date           | Transaction date              |

---

## Approach

1. Load and clean transaction data using pandas
2. Calculate processing fees per transaction
3. Aggregate total fees by merchant
4. Compute average fee percentages by pricing model
5. Compare tiered vs interchange pricing per merchant
6. Flag merchants overpaying by more than 10%
7. Export results to a CSV file for business review

---

## Key Logic

- Merchants without data for both pricing models are **not flagged**
- Missing pricing data is handled gracefully and marked as `N/A`
- Overpayment is only flagged when both pricing models are available

This reflects realistic production data conditions.

---

## Output

The script generates a file called:
