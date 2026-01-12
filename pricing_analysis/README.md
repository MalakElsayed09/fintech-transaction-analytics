# Pricing Analysis Automation

## Overview

This module analyzes transaction-level payment data to compare tiered pricing versus interchange pricing models. The goal is to identify merchants who may be overpaying on processing fees and provide data-driven recommendations.

## What This Does

- Loads transaction data from a CSV file
- Calculates processing fees per transaction
- Aggregates total fees by merchant
- Compares average fee percentages between pricing models
- Flags merchants potentially overpaying under tiered pricing

## Tools & Technologies

- Python
- pandas
- CSV data processing

## Outcome

The analysis produces a summary file highlighting merchants who could reduce processing costs by switching pricing models, supporting pricing optimization decisions.
