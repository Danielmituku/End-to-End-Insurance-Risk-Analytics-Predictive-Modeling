# Figures Directory

This directory contains all visualizations generated during the Exploratory Data Analysis (EDA) phase.

## Figure Files

### Standard EDA Visualizations

1. **01_histograms_numerical_variables.png**
   - Distribution histograms for key numerical variables
   - Variables: TotalPremium, TotalClaims, SumInsured, RegistrationYear, cubiccapacity, kilowatts

2. **02_bar_charts_categorical_variables.png**
   - Distribution bar charts for key categorical variables
   - Variables: Province, Gender, VehicleType, CoverType, make, MaritalStatus

3. **03_correlation_matrix.png**
   - Correlation heatmap showing relationships between numerical variables
   - Helps identify multicollinearity and feature relationships

4. **04_monthly_changes_premium_claims_by_postalcode.png**
   - Scatter plot showing monthly changes in TotalPremium vs TotalClaims by PostalCode
   - Required analysis for Task 1

5. **05_geographic_trends_analysis.png**
   - Three-panel visualization:
     - Cover Type distribution by Province
     - Average Premium by Province
     - Top 5 Auto Makes by Province

6. **06_box_plots_outlier_detection.png**
   - Box plots for outlier detection using IQR method
   - Shows outliers for: TotalPremium, TotalClaims, SumInsured, CustomValueEstimate, cubiccapacity, kilowatts

### Creative Visualizations (Task 1 Requirement)

7. **07_creative_1_loss_ratio_heatmap.png**
   - Loss Ratio Heatmap: Province vs Vehicle Type
   - Identifies high-risk province-vehicle type combinations

8. **08_creative_2_temporal_risk_trend.png**
   - Temporal Risk Trend: Premium, Claims, and Loss Ratio over time
   - Dual y-axis plot showing trends from Feb 2014 to Aug 2015

9. **09_creative_3_risk_value_matrix.png**
   - Risk-Value Matrix: Premium vs Loss Ratio by Vehicle Make
   - Quadrant analysis identifying pricing opportunities

## Technical Details

- **Resolution**: All figures saved at 300 DPI for high-quality presentation
- **Format**: PNG format for compatibility
- **Size**: Optimized with `bbox_inches='tight'` for clean edges

## Usage

These figures are referenced in:
- Interim Report (`reports/interim_report.md`)
- Final Report (to be created)
- Presentation materials

## Regeneration

To regenerate all figures, run the complete `notebooks/01_eda_analysis.ipynb` notebook. All figures will be automatically saved to this directory.

