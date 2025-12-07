"""Script to extract actual values from EDA and update interim report."""

import pandas as pd
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

from src.data.load_data import load_insurance_data

# Load data
print("Loading data...")
df = load_insurance_data()

# Calculate Loss Ratio (handle division by zero)
df['LossRatio'] = df.apply(
    lambda row: row['TotalClaims'] / row['TotalPremium'] if row['TotalPremium'] > 0 else 0,
    axis=1
)

# Filter out invalid loss ratios
df_valid = df[(df['TotalPremium'] > 0) & (df['LossRatio'].notna()) & 
             (df['LossRatio'] != float('inf')) & (df['LossRatio'] != float('-inf'))]

print(f"\nValid records for loss ratio analysis: {len(df_valid):,} out of {len(df):,}")

# Loss Ratio by Province
print("\n" + "="*80)
print("LOSS RATIO BY PROVINCE")
print("="*80)
province_stats = df_valid.groupby('Province').agg({
    'TotalPremium': 'sum',
    'TotalClaims': 'sum',
    'PolicyID': 'nunique',
    'LossRatio': 'mean'
}).reset_index()
province_stats['LossRatio_Overall'] = province_stats['TotalClaims'] / province_stats['TotalPremium']
province_stats = province_stats.sort_values('LossRatio_Overall', ascending=False)
print(province_stats.to_string(index=False))

# Loss Ratio by Vehicle Type
print("\n" + "="*80)
print("LOSS RATIO BY VEHICLE TYPE")
print("="*80)
vehicle_stats = df_valid.groupby('VehicleType').agg({
    'TotalPremium': 'sum',
    'TotalClaims': 'sum',
    'PolicyID': 'nunique',
    'LossRatio': 'mean'
}).reset_index()
vehicle_stats['LossRatio_Overall'] = vehicle_stats['TotalClaims'] / vehicle_stats['TotalPremium']
vehicle_stats = vehicle_stats.sort_values('LossRatio_Overall', ascending=False)
print(vehicle_stats.to_string(index=False))

# Loss Ratio by Gender
print("\n" + "="*80)
print("LOSS RATIO BY GENDER")
print("="*80)
gender_stats = df_valid.groupby('Gender').agg({
    'TotalPremium': 'sum',
    'TotalClaims': 'sum',
    'PolicyID': 'nunique',
    'LossRatio': 'mean'
}).reset_index()
gender_stats['LossRatio_Overall'] = gender_stats['TotalClaims'] / gender_stats['TotalPremium']
gender_stats = gender_stats.sort_values('LossRatio_Overall', ascending=False)
print(gender_stats.to_string(index=False))

# Overall portfolio metrics
print("\n" + "="*80)
print("OVERALL PORTFOLIO METRICS")
print("="*80)
total_premium = df['TotalPremium'].sum()
total_claims = df['TotalClaims'].sum()
overall_loss_ratio = total_claims / total_premium if total_premium > 0 else 0
print(f"Total Premium: {total_premium:,.2f} ZAR")
print(f"Total Claims: {total_claims:,.2f} ZAR")
print(f"Overall Loss Ratio: {overall_loss_ratio:.4f}")
print(f"Total Policies: {df['PolicyID'].nunique():,}")
print(f"Average Premium per Policy: {df['TotalPremium'].mean():.2f} ZAR")
print(f"Average Claim Amount: {df[df['TotalClaims'] > 0]['TotalClaims'].mean():.2f} ZAR")

# Save to CSV for easy reference
province_stats.to_csv('reports/province_loss_ratios.csv', index=False)
vehicle_stats.to_csv('reports/vehicle_type_loss_ratios.csv', index=False)
gender_stats.to_csv('reports/gender_loss_ratios.csv', index=False)

print("\n\nData saved to CSV files in reports/ directory")

