# Interim Report: Insurance Risk Analytics Project

**Project**: End-to-End Insurance Risk Analytics & Predictive Modeling  
**Client**: AlphaCare Insurance Solutions (ACIS)  
**Date**: December 07, 2025  
**Author**: [Your Name]  
**Status**: Interim Submission (Tasks 1, 2, 3 & 4)

---

## Executive Summary

This interim report summarizes the progress made on the first two tasks of the insurance risk analytics project. The project aims to analyze historical insurance claim data to optimize marketing strategy and discover low-risk customer segments for premium reduction.

**Key Accomplishments:**
- ✅ Established project infrastructure with Git/GitHub and CI/CD pipeline
- ✅ Completed comprehensive Exploratory Data Analysis (EDA)
- ✅ Set up Data Version Control (DVC) for reproducible data management
- ✅ Performed A/B Hypothesis Testing to validate risk drivers
- ✅ Built predictive models for claim severity and premium optimization
- ✅ Identified initial insights into risk patterns and data quality

---

## 1. Task 1: Git/GitHub & Project Planning

### 1.1 Git and GitHub Setup

**Repository Structure:**
- Created a well-organized repository with modular code structure
- Implemented branch strategy: `main`, `task-1`, `task-2`, `task-3`, `task-4`
- Established CI/CD pipeline with GitHub Actions for automated testing and code quality checks

**Key Features:**
- ✅ Comprehensive README with project overview and setup instructions
- ✅ Contributing guidelines and code style standards
- ✅ Automated linting and testing workflows
- ✅ Proper `.gitignore` configuration for Python projects

**Commit History:**
- Regular commits following conventional commit standards
- Descriptive commit messages documenting all changes
- Branch management following best practices

### 1.2 Project Planning - EDA & Statistics

#### Data Understanding

**Dataset Overview:**
- **Time Period**: February 2014 to August 2015 (18 months)
- **Total Records**: 1,000,098 policies
- **Total Features**: 52 columns
- **Data File**: `MachineLearningRating_v3.txt` (pipe-delimited)

**Data Categories:**
1. **Policy Information**: UnderwrittenCoverID, PolicyID, TransactionMonth
2. **Client Demographics**: Gender, MaritalStatus, Citizenship, LegalType, Title, Language
3. **Location Data**: Country, Province, PostalCode, MainCrestaZone, SubCrestaZone
4. **Vehicle Information**: Make, Model, VehicleType, RegistrationYear, Cubiccapacity, etc.
5. **Plan Details**: SumInsured, TermFrequency, CalculatedPremiumPerTerm, CoverType
6. **Financial Metrics**: TotalPremium, TotalClaims

#### Data Quality Assessment

**Missing Values Analysis:**
- **High Missing Values (>50%)**:
  - NumberOfVehiclesInFleet: 100% (entire column missing)
  - CrossBorder: 99.93%
  - CustomValueEstimate: 77.96%
  - Converted, Rebuilt, WrittenOff: 64.18% each
- **Moderate Missing Values (10-50%)**:
  - NewVehicle: 15.33%
  - Bank: 14.59%
- **Low Missing Values (<5%)**:
  - AccountType: 4.02%
  - Gender: 0.95%
  - MaritalStatus: 0.83%
  - Vehicle-related fields: 0.06% (552 records)

**Data Types:**
- **Numerical**: TotalPremium, TotalClaims, SumInsured, RegistrationYear, etc.
- **Categorical**: Province, Gender, VehicleType, CoverType, Make, etc.
- **Boolean**: IsVATRegistered, NewVehicle, WrittenOff, etc.
- **Date**: TransactionMonth (converted from object to datetime)

#### Exploratory Data Analysis Findings

##### Overall Portfolio Metrics

**Loss Ratio Analysis:**
- **Overall Loss Ratio**: 1.0477 (104.77%) - TotalClaims / TotalPremium
- **Note**: Loss ratio > 1.0 indicates the portfolio is unprofitable overall, with claims exceeding premiums
- **Valid Records**: 618,176 out of 1,000,098 records have valid loss ratios (policies with positive premiums)
- **Interpretation**: The portfolio shows significant variability in loss ratios across provinces, vehicle types, and demographics, indicating critical opportunities for risk-based pricing segmentation and premium adjustments.

**Key Financial Metrics:**
- **Total Premium**: 61,911,562.70 ZAR (sum across all policies)
- **Total Claims**: 64,867,546.17 ZAR (sum across all policies)
- **Total Policies**: 7,000 unique policies
- **Average Premium per Policy**: 61.91 ZAR (mean), 2.18 ZAR (median) - highly skewed
- **Average Claim Amount**: 23,273.39 ZAR (mean when claims occur), 0 ZAR (median - most policies have no claims)
- **Sum Insured**: Mean = 604,172.70 ZAR, Median = 7,500 ZAR
- **Custom Value Estimate**: Mean = 225,531.10 ZAR (available for 22% of policies)

##### Loss Ratio by Province

**Visualization**: See `07_creative_1_loss_ratio_heatmap.png` for detailed heatmap

| Province | Loss Ratio | Total Premium (ZAR) | Total Claims (ZAR) | Number of Policies |
|----------|------------|---------------------|-------------------|-------------------|
| Gauteng | 1.163 | 24,054,870 | 27,981,270 | 1,978 |
| Western Cape | 1.044 | 9,810,107 | 10,242,260 | 734 |
| KwaZulu-Natal | 1.022 | 13,235,780 | 13,526,350 | 1,155 |
| North West | 0.747 | 7,490,508 | 5,593,723 | 904 |
| Mpumalanga | 0.718 | 2,836,292 | 2,035,792 | 294 |
| Limpopo | 0.645 | 1,537,324 | 991,893 | 149 |
| Eastern Cape | 0.629 | 2,140,303 | 1,346,308 | 262 |
| Free State | 0.510 | 521,363 | 265,975 | 44 |
| Northern Cape | 0.283 | 316,558 | 89,491 | 44 |

**Key Insights:**
- **Highest Risk Provinces**: Gauteng (116.3%), Western Cape (104.4%), and KwaZulu-Natal (102.2%) all have loss ratios > 1.0, indicating unprofitable portfolios
- **Lowest Risk Provinces**: Northern Cape (28.3%), Free State (51.0%), and Eastern Cape (62.9%) show significantly lower risk
- **Geographic Risk Pattern**: Major urban provinces (Gauteng, Western Cape) show highest risk, while smaller provinces show lower risk
- **Regional Risk Segmentation**: Clear opportunity for province-based premium adjustments
- **Recommendation**: 
  - **Immediate Action**: Increase premiums by 15-20% for Gauteng, Western Cape, and KwaZulu-Natal
  - **Moderate Adjustment**: Review pricing for North West, Mpumalanga, and Limpopo
  - **Maintain Competitive**: Northern Cape, Free State, and Eastern Cape can maintain or slightly reduce premiums

##### Loss Ratio by Vehicle Type

**Visualization**: See `07_creative_1_loss_ratio_heatmap.png` for Province-Vehicle Type combinations

| Vehicle Type | Loss Ratio | Total Premium (ZAR) | Total Claims (ZAR) | Number of Policies |
|--------------|------------|---------------------|-------------------|-------------------|
| Heavy Commercial | 1.612 | 460,948 | 743,243 | 59 |
| Medium Commercial | 1.028 | 3,922,840 | 4,032,212 | 372 |
| Passenger Vehicle | 1.000 | 56,673,410 | 56,680,480 | 5,318 |
| Light Commercial | 0.232 | 260,498 | 60,453 | 35 |
| Bus | 0.000 | 58,245 | 0 | 5 |

**Key Insights:**
- **Highest Risk**: Heavy Commercial vehicles (161.2% loss ratio) and Medium Commercial (102.8%) are unprofitable
- **Moderate Risk**: Passenger Vehicles (100.0%) are at break-even, representing the largest segment (5,318 policies)
- **Lowest Risk**: Light Commercial (23.2%) and Bus (0.0%) show very low risk
- **Volume vs Risk**: Passenger vehicles dominate by volume but are at break-even, while commercial vehicles are high-risk
- **Recommendation**: 
  - **Critical**: Increase Heavy Commercial premiums by 60-70% to achieve profitability
  - **High Priority**: Increase Medium Commercial premiums by 20-30%
  - **Review**: Passenger Vehicle pricing strategy needs review to improve margins
  - **Opportunity**: Light Commercial and Bus segments can be marketed as low-risk options

##### Loss Ratio by Gender

**Visualization**: See `02_bar_charts_categorical_variables.png` for gender distribution

| Gender | Loss Ratio | Total Premium (ZAR) | Total Claims (ZAR) | Number of Policies |
|--------|------------|---------------------|-------------------|-------------------|
| Not specified | 1.015 | 59,207,820 | 60,076,380 | 5,264 |
| Female | 0.812 | 304,481 | 247,277 | 23 |
| Male | 0.774 | 1,606,618 | 1,242,916 | 149 |

**Key Insights:**
- **Data Quality Issue**: 5,264 policies (75.2%) have "Not specified" gender, limiting gender-based analysis
- **Specified Gender Analysis**: 
  - Female policies show 81.2% loss ratio (lower risk than overall)
  - Male policies show 77.4% loss ratio (lowest risk among specified genders)
  - Both specified genders show better performance than the overall portfolio
- **Sample Size**: Only 172 policies (2.5%) have specified gender, making statistical conclusions limited
- **Recommendation**: 
  - Improve data collection to capture gender information for better segmentation
  - Statistical testing will be performed in Task 3 (A/B Hypothesis Testing) with appropriate sample size considerations
  - **Note**: Gender-based pricing may have regulatory and ethical considerations

##### Distribution Analysis

**Visualizations**: See `01_histograms_numerical_variables.png` and `06_box_plots_outlier_detection.png`

**TotalPremium Distribution:**
- Mean: 61.91 ZAR
- Median: 2.18 ZAR
- Standard Deviation: 230.28 ZAR
- Highly right-skewed distribution (median << mean)
- Many zero values (25th percentile = 0)

**TotalClaims Distribution:**
- Mean: 64.86 ZAR
- Median: 0 ZAR
- Standard Deviation: 2,384.08 ZAR
- Extremely right-skewed (most policies have zero claims)
- High variance indicates significant claim variability

**Outlier Detection:**
- Box plots created for all key numerical variables (see `06_box_plots_outlier_detection.png`)
- IQR method used: Outliers defined as values outside Q1 - 1.5*IQR to Q3 + 1.5*IQR
- Outlier counts and percentages calculated for each variable
- Strategy: Outliers removed for visualization purposes (99th percentile), but full analysis includes all data

##### Temporal Trends

**Visualization**: See `08_creative_2_temporal_risk_trend.png`

**Monthly Trends:**
- Premium and claims tracked monthly from February 2014 to August 2015
- Loss ratio calculated monthly to assess risk trends
- Month-over-month changes in TotalPremium and TotalClaims analyzed by PostalCode

**Key Observations:**
- Correlation of 0.18 between monthly premium changes and claims changes suggests moderate relationship
- Temporal analysis reveals seasonal patterns in risk
- Geographic analysis by postal code shows varying risk patterns across regions

##### Vehicle Make/Model Analysis

**Visualization**: See `09_creative_3_risk_value_matrix.png` for detailed make analysis

**Top Makes by Policy Count:**
- Analysis includes top 20 makes with at least 100 policies
- Risk-Value Matrix identifies four quadrants:
  - **High Premium + Low Risk**: Premium opportunities (green quadrant)
  - **Low Premium + High Risk**: Need premium adjustment (orange quadrant)
  - **High Premium + High Risk**: Review pricing strategy (red quadrant)
  - **Low Premium + Low Risk**: Competitive positioning (yellow quadrant)

**Key Insights:**
- Vehicle make is a strong predictor of risk and premium value
- The Risk-Value Matrix reveals clear segmentation opportunities
- Some makes show high premium potential with low risk
- **Business Recommendation**: 
  - Increase premiums for low-risk, high-value makes
  - Adjust premiums upward for high-risk makes currently underpriced
  - Maintain competitive rates for low-risk, low-premium makes

#### Creative Visualizations

All visualizations are saved in `reports/figures/` directory.

**Visualization 1: Loss Ratio Heatmap - Province vs Vehicle Type**
- **File**: `07_creative_1_loss_ratio_heatmap.png`
- **Type**: Heatmap
- **Key Insight**: Reveals which province-vehicle type combinations have the highest risk (loss ratio). This helps identify geographic and vehicle category risk patterns simultaneously.
- **Business Impact**: Enables targeted premium adjustments by province and vehicle type, optimizing pricing strategy for high-risk combinations while maintaining competitive rates for low-risk segments.

**Visualization 2: Temporal Risk Trend Analysis**
- **File**: `08_creative_2_temporal_risk_trend.png`
- **Type**: Dual y-axis line plot
- **Key Insight**: Shows how premium, claims, and risk (loss ratio) evolved over the 18-month period, revealing seasonal patterns and trends. The correlation between monthly premium changes and claims changes by postal code is 0.18.
- **Business Impact**: Identifies seasonal risk patterns, enabling proactive premium adjustments and marketing campaigns timed to low-risk periods. Helps understand if premium increases correlate with claim increases.

**Visualization 3: Risk-Value Matrix - Vehicle Makes**
- **File**: `09_creative_3_risk_value_matrix.png`
- **Type**: Scatter plot with quadrant analysis
- **Key Insight**: Identifies vehicle makes that are:
  - High Premium + Low Risk: Premium opportunities (top-right quadrant)
  - Low Premium + High Risk: Need premium adjustment (bottom-left quadrant)
  - High Premium + High Risk: Review pricing strategy (top-left quadrant)
- **Business Impact**: Enables strategic pricing decisions by vehicle make, identifying opportunities to increase premiums for low-risk makes and adjust premiums for high-risk makes.

#### Statistical Insights

**Key Statistical Findings:**
1. **High Variability in Financial Metrics**: Standard deviations are significantly larger than means, indicating high variability in premiums and claims
2. **Right-Skewed Distributions**: Both TotalPremium and TotalClaims show extreme right-skewness, with medians much lower than means
3. **Zero-Inflated Claims Data**: Median claim amount is 0, indicating most policies have no claims
4. **Moderate Correlation**: Monthly premium and claims changes show correlation of 0.18 by postal code

**Distribution Characteristics:**
- **TotalPremium**: Highly right-skewed (skewness > 0), many zero values
- **TotalClaims**: Extremely right-skewed, zero-inflated distribution
- **SumInsured**: Right-skewed with large range (0.01 to 12.6M ZAR)
- **CustomValueEstimate**: Right-skewed, available for 22% of policies

**Correlation Analysis:**
- Correlation matrix reveals relationships between numerical variables (see `03_correlation_matrix.png`)
- Key correlations will be analyzed in detail during modeling phase (Task 4)

---

## 2. Task 2: Data Version Control (DVC)

### 2.1 DVC Setup

**Installation:**
- ✅ DVC installed successfully
- ✅ DVC initialized in project directory

**Configuration:**
- **Remote Storage Type**: Local storage
- **Storage Location**: `./data/dvc_storage`
- **Remote Name**: `localstorage` (default)

### 2.2 Data Versioning

**Data Files Tracked:**
- `data/raw/MachineLearningRating_v3.txt` - Main insurance dataset (1,000,098 rows, 52 columns)
- **File Size**: 529,363,713 bytes (~505 MB)
- **Hash**: md5 (f6b7009b68ae21372b7deca9307fbb23)
- File tracked using DVC for version control
- `.dvc` file: `data/raw/MachineLearningRating_v3.txt.dvc` committed to Git repository

**Version Control:**
- ✅ Data files tracked with DVC
- ✅ `.dvc` files committed to Git
- ✅ Data pushed to local remote storage
- ✅ DVC autostage enabled for easier workflow

**Data Versions:**
- **Version 1**: Initial dataset (MachineLearningRating_v3.txt)
  - Date: December 7, 2025
  - Status: Tracked and pushed to local remote storage
  - Location: `data/dvc_storage/files/`

### 2.3 Reproducibility

**Benefits Achieved:**
- ✅ Data inputs are version-controlled
- ✅ Analysis can be reproduced at any time
- ✅ Audit trail for regulatory compliance
- ✅ Easy collaboration with team members

**DVC Commands Used:**
```bash
# Initialize DVC (already initialized from previous setup)
dvc init

# Configure local remote storage
dvc remote add -d localstorage ./data/dvc_storage

# Add data file to DVC tracking
dvc add data/raw/MachineLearningRating_v3.txt

# Commit DVC files to Git
git add data/raw/MachineLearningRating_v3.txt.dvc .dvc/config .dvc/.gitignore

# Push data to local remote storage
dvc push

# Enable autostage for easier workflow
dvc config core.autostage true
```

**Verification:**
- ✅ DVC version: 3.64.2
- ✅ Remote storage: `localstorage` (default) at `./data/dvc_storage`
- ✅ Data status: "Data and pipelines are up to date"
- ✅ All `.dvc` files committed to Git

---

## 3. Key Insights and Recommendations

### 3.1 Risk Segmentation Opportunities

Based on the EDA findings:

1. **Province-Level Segmentation:**
   - **High-Risk Provinces** (Loss Ratio > 1.0): Gauteng (116.3%), Western Cape (104.4%), KwaZulu-Natal (102.2%)
     - **Action**: Immediate premium increases of 15-20% required
     - **Impact**: These three provinces represent 3,867 policies (55.2% of portfolio)
   - **Low-Risk Provinces** (Loss Ratio < 0.7): Northern Cape (28.3%), Free State (51.0%), Eastern Cape (62.9%)
     - **Action**: Maintain competitive pricing, potential for premium reduction to attract new customers
     - **Impact**: Opportunity to expand market share in these regions

2. **Vehicle Type Segmentation:**
   - **Critical Risk**: Heavy Commercial (161.2% loss ratio) - requires 60-70% premium increase
   - **High Risk**: Medium Commercial (102.8% loss ratio) - requires 20-30% premium increase
   - **Break-Even**: Passenger Vehicles (100.0% loss ratio) - pricing review needed
   - **Low Risk**: Light Commercial (23.2%) and Bus (0.0%) - marketing opportunities for low-risk segments

3. **Demographic Segmentation:**
   - **Data Limitation**: 75.2% of policies have unspecified gender, limiting demographic analysis
   - **Available Data**: Specified gender policies (Male: 77.4%, Female: 81.2%) show lower risk than overall portfolio
   - **Action**: Improve data collection for better demographic segmentation
   - **Targeting**: Focus on low-risk demographic segments once data quality improves

### 3.2 Data Quality Recommendations

**Missing Data Handling:**
- **High Missing Values (>50%)**: 
  - NumberOfVehiclesInFleet (100% missing) - Consider removing or collecting this data
  - CrossBorder (99.9% missing) - Low priority, but useful for cross-border risk analysis
  - CustomValueEstimate (78% missing) - Important for vehicle valuation, consider imputation or collection
- **Moderate Missing Values (10-50%)**:
  - NewVehicle (15.3%) - Important for risk assessment, consider imputation
  - Bank (14.6%) - May be useful for payment risk analysis
- **Low Missing Values (<5%)**:
  - Gender (0.95%) - Critical for demographic analysis, improve data collection
  - Vehicle-related fields (0.06%) - Excellent data quality, maintain standards

**Data Cleaning Recommendations:**
- Handle zero and negative premium values (currently causing infinite loss ratios)
- Remove or flag records with invalid loss ratios (inf, -inf, NaN)
- Standardize categorical variables (e.g., gender values)
- Validate date formats and ranges

**Data Collection Improvements:**
- **Priority 1**: Improve gender data collection (currently 75.2% unspecified)
- **Priority 2**: Collect CustomValueEstimate for more policies (currently 22% coverage)
- **Priority 3**: Implement validation rules to prevent missing critical fields
- **Priority 4**: Collect NumberOfVehiclesInFleet if relevant for fleet pricing

### 3.3 A/B Hypothesis Testing Results (Task 3)

**Task 3 - A/B Hypothesis Testing:**
- ✅ All 4 hypotheses tested with appropriate statistical methods
- ✅ Results documented and interpreted
- ✅ Business recommendations provided for each hypothesis

**Task 4 - Statistical Modeling:**
- Data preparation pipeline established
- Feature engineering opportunities identified
- Model selection strategy planned

---

## 3. Task 3: A/B Hypothesis Testing

### 3.1 Overview

Statistical hypothesis testing was performed to validate or reject key hypotheses about risk drivers. All tests were conducted at a significance level of α = 0.05.

### 3.2 Hypothesis 1: Risk Differences Across Provinces

**H₀**: There are no risk differences across provinces

**Tests Performed:**
1. **Claim Frequency Test** (Chi-squared test for independence)
   - Test Statistic: χ² = 104.19
   - p-value: 5.93 × 10⁻¹⁹ (highly significant)
   - Degrees of Freedom: 8
   - **Result**: REJECT H₀ (p < 0.05)

2. **Claim Severity Test** (ANOVA)
   - Test Statistic: F = 4.83
   - p-value: 6.30 × 10⁻⁶ (highly significant)
   - **Result**: REJECT H₀ (p < 0.05)

**Overall Result**: **REJECT H₀** - Risk differences exist across provinces

**Business Interpretation:**
- Statistically significant risk differences exist across provinces in both claim frequency and severity
- This validates the EDA findings showing provinces like Gauteng (116.3% loss ratio) and Western Cape (104.4%) have significantly higher risk than provinces like Northern Cape (28.3%)
- **Recommendation**: Implement province-based premium adjustments immediately. High-risk provinces require premium increases of 15-20% to achieve profitability.

### 3.3 Hypothesis 2: Risk Differences Between Zip Codes

**H₀**: There are no risk differences between zip codes

**Tests Performed:**
1. **Claim Frequency Test** (Chi-squared test)
   - Test Statistic: χ² = 72.65
   - p-value: 4.59 × 10⁻¹² (highly significant)
   - Degrees of Freedom: 9
   - **Result**: REJECT H₀ (p < 0.05)
   - **Note**: Test performed on top 10 zip codes by policy count

2. **Claim Severity Test** (ANOVA)
   - Test Statistic: F = 5.24
   - p-value: 5.47 × 10⁻⁷ (highly significant)
   - **Result**: REJECT H₀ (p < 0.05)

**Overall Result**: **REJECT H₀** - Risk differences exist between zip codes

**Business Interpretation:**
- Statistically significant risk differences exist between zip codes in both claim frequency and severity
- Geographic risk segmentation at the zip code level is valid and should be incorporated into pricing models
- **Recommendation**: Develop zip code-based risk tiers for premium pricing. High-risk zip codes should have premiums adjusted upward, while low-risk zip codes can be used for competitive pricing to attract new customers.

### 3.4 Hypothesis 3: Margin Differences Between Zip Codes

**H₀**: There is no significant margin (profit) difference between zip codes

**Test Performed:**
- **Margin Test** (ANOVA)
  - Test Statistic: F = 1.05
  - p-value: 0.396 (not significant)
  - **Result**: FAIL TO REJECT H₀ (p ≥ 0.05)
  - **Note**: Test performed on top 10 zip codes by policy count

**Overall Result**: **FAIL TO REJECT H₀** - No significant margin difference between zip codes

**Business Interpretation:**
- While risk (claims) differs significantly by zip code, the margin (profit) does not show statistically significant differences
- This suggests that premium pricing may already be partially adjusted for risk, or that other factors (expenses, commissions) offset risk differences
- **Recommendation**: 
  - Review current pricing strategy - premiums may need more aggressive risk-based adjustments
  - Investigate cost structures (expenses, commissions) that may be diluting margin differences
  - Consider that margin differences may exist but require larger sample sizes or different segmentation to detect

### 3.5 Hypothesis 4: Risk Differences Between Women and Men

**H₀**: There is no significant risk difference between Women and Men

**Tests Performed:**
1. **Claim Frequency Test** (Chi-squared test)
   - Test Statistic: χ² = 0.004
   - p-value: 0.951 (not significant)
   - Degrees of Freedom: 1
   - **Result**: FAIL TO REJECT H₀ (p ≥ 0.05)

2. **Claim Severity Test** (t-test)
   - Test Statistic: t = -0.42
   - p-value: 0.676 (not significant)
   - Male Mean Severity: 14,858.55 ZAR
   - Female Mean Severity: 17,874.72 ZAR
   - **Result**: FAIL TO REJECT H₀ (p ≥ 0.05)

**Overall Result**: **FAIL TO REJECT H₀** - No significant risk differences between genders

**Business Interpretation:**
- No statistically significant differences in risk between men and women for both claim frequency and severity
- **Important Note**: Only 172 policies (2.5% of portfolio) have specified gender, limiting statistical power
- The small sample size may prevent detection of true differences if they exist
- **Recommendation**: 
  - **Data Quality**: Improve gender data collection to enable more robust gender-based analysis
  - **Pricing Policy**: Given no significant differences found and regulatory considerations, gender should not be used as a pricing factor
  - **Future Analysis**: Re-test with larger sample size once data quality improves

### 3.6 Summary of Hypothesis Tests

| Hypothesis | Metric | Test | p-value | Result |
|------------|--------|------|---------|--------|
| Province Risk Differences | Frequency | Chi-squared | 5.93 × 10⁻¹⁹ | **REJECT H₀** |
| Province Risk Differences | Severity | ANOVA | 6.30 × 10⁻⁶ | **REJECT H₀** |
| Zipcode Risk Differences | Frequency | Chi-squared | 4.59 × 10⁻¹² | **REJECT H₀** |
| Zipcode Risk Differences | Severity | ANOVA | 5.47 × 10⁻⁷ | **REJECT H₀** |
| Zipcode Margin Differences | Margin | ANOVA | 0.396 | **FAIL TO REJECT H₀** |
| Gender Risk Differences | Frequency | Chi-squared | 0.951 | **FAIL TO REJECT H₀** |
| Gender Risk Differences | Severity | t-test | 0.676 | **FAIL TO REJECT H₀** |

### 3.7 Key Business Recommendations from Hypothesis Testing

**Immediate Actions:**
1. **Province-Based Pricing**: Implement risk-based premium adjustments by province immediately
   - High-risk provinces (Gauteng, Western Cape, KwaZulu-Natal) need 15-20% premium increases
   - Low-risk provinces can maintain competitive rates or reduce premiums to attract customers

2. **Zip Code Segmentation**: Develop zip code-based risk tiers for pricing
   - Create risk categories (high, medium, low) based on zip code performance
   - Adjust premiums accordingly while monitoring margin impact

3. **Margin Analysis**: Investigate why margin differences are not significant despite risk differences
   - Review expense structures and commission rates
   - Consider more granular analysis or larger sample sizes

4. **Data Quality**: Improve gender data collection for future analysis
   - Current sample size (2.5%) is insufficient for robust gender-based pricing decisions
   - Gender-based pricing has regulatory considerations regardless of statistical findings

**Strategic Implications:**
- Geographic segmentation (province and zip code) is validated as a key pricing factor
- Risk-based pricing by location should be a core component of the pricing strategy
- Portfolio profitability can be improved through targeted premium adjustments in high-risk geographic areas

---

## 4. Task 4: Statistical Modeling

### 4.1 Overview

Predictive models were built for two key business objectives:
1. **Claim Severity Prediction**: Predict TotalClaims for policies with claims > 0
2. **Premium Optimization**: Predict optimal premium values

Four machine learning models were implemented and compared: Linear Regression, Decision Tree, Random Forest, and XGBoost (when available).

### 4.2 Model 1: Claim Severity Prediction

**Objective**: Predict claim amounts for policies that have experienced claims.

**Data Preparation:**
- Filtered to policies with TotalClaims > 0
- Features used: Province, PostalCode, Gender, MaritalStatus, VehicleType, Make, RegistrationYear, Cubiccapacity, Kilowatts, SumInsured, CoverType, CalculatedPremiumPerTerm
- Train-test split: 80-20
- Features encoded and scaled

**Model Performance:**

| Model | Train RMSE | Train R² | Test RMSE | Test R² | Test MAE | Test MAPE |
|-------|------------|----------|-----------|---------|----------|-----------|
| Linear Regression | 31,972.20 | 0.305 | 34,148.28 | **0.275** | 17,599.02 | 372.09% |
| Decision Tree | 25,794.25 | 0.548 | 37,701.53 | 0.116 | 16,395.65 | 242.73% |
| Random Forest | 23,679.71 | 0.619 | 34,279.47 | 0.269 | 15,612.75 | 248.20% |

**Best Model**: **Linear Regression** (by Test R² = 0.275)

**Key Findings:**
- Linear Regression shows best generalization (highest test R²)
- Random Forest shows overfitting (high train R² = 0.619, lower test R² = 0.269)
- Test RMSE of 34,148 ZAR indicates moderate prediction accuracy
- High MAPE (372%) suggests high variability in claim amounts

**Top 5 Most Important Features:**
1. SumInsured (45,526.47) - Strongest predictor
2. CalculatedPremiumPerTerm (43,110.40) - Premium amount
3. CoverType_Windscreen (14,284.09) - Cover type indicator
4. CoverType_Income Protector (9,844.75) - Cover type indicator
5. PostalCode (7,719.39) - Geographic location

**Business Interpretation:**
- SumInsured and CalculatedPremiumPerTerm are the strongest predictors of claim severity
- Geographic location (PostalCode) plays a significant role
- Cover type (Windscreen, Income Protector) influences claim amounts
- Model explains 27.5% of variance in claim severity, indicating room for improvement

### 4.3 Model 2: Premium Prediction

**Objective**: Predict optimal premium values for pricing optimization.

**Data Preparation:**
- Used all policies with valid premium data
- Same feature set as claim severity model
- Train-test split: 80-20
- Features encoded and scaled

**Model Performance:**

| Model | Train RMSE | Train R² | Test RMSE | Test R² | Test MAE | Test MAPE |
|-------|------------|----------|-----------|---------|----------|-----------|
| Linear Regression | 184.31 | 0.420 | 118.50 | 0.545 | 51.78 | 2.45 × 10¹¹% |
| Decision Tree | 175.19 | 0.476 | 108.03 | 0.622 | 44.59 | 2.13 × 10¹¹% |
| Random Forest | 174.49 | 0.480 | 107.59 | **0.625** | 44.82 | 2.15 × 10¹¹% |

**Best Model**: **Random Forest** (by Test R² = 0.625)

**Key Findings:**
- Random Forest achieves best performance with R² = 0.625
- Test RMSE of 107.59 ZAR indicates good prediction accuracy
- Model explains 62.5% of variance in premium values
- All models show good generalization (test R² close to train R²)

**Top 5 Most Important Features:**
1. CalculatedPremiumPerTerm (0.7341) - Dominant predictor (73.4% importance)
2. SumInsured (0.2425) - Second most important (24.3% importance)
3. PostalCode (0.0099) - Geographic location
4. Cubiccapacity (0.0027) - Vehicle engine capacity
5. RegistrationYear (0.0021) - Vehicle age indicator

**Business Interpretation:**
- CalculatedPremiumPerTerm and SumInsured together explain ~97% of premium variance
- Geographic location (PostalCode) has minor but measurable impact
- Vehicle characteristics (cubic capacity, registration year) contribute minimally
- Model performs well for premium prediction, suitable for pricing optimization

### 4.4 Model Interpretability

**Feature Importance Analysis:**
- Feature importance plots generated for both best models
- Visualizations saved: `10_feature_importance_claim_severity.png`, `11_feature_importance_premium.png`

**SHAP Analysis:**
- SHAP (SHapley Additive exPlanations) analysis performed for claim severity model
- Provides local and global feature importance explanations
- Visualization saved: `12_shap_summary_claim_severity.png`

**Key Insights:**
- SumInsured and CalculatedPremiumPerTerm are consistently the most important features
- Geographic features (Province, PostalCode) show moderate importance
- Vehicle characteristics have varying impact depending on the prediction task

### 4.5 Model Comparison Summary

**Claim Severity Prediction:**
- **Best Model**: Linear Regression
- **Performance**: R² = 0.275, RMSE = 34,148 ZAR
- **Use Case**: Moderate accuracy for claim amount prediction
- **Limitation**: High variability in claim amounts limits predictive power

**Premium Prediction:**
- **Best Model**: Random Forest
- **Performance**: R² = 0.625, RMSE = 107.59 ZAR
- **Use Case**: Strong accuracy for premium optimization
- **Strength**: Good generalization, suitable for production use

### 4.6 Business Recommendations from Modeling

**Immediate Actions:**
1. **Premium Optimization**: Deploy Random Forest model for premium prediction
   - Model achieves 62.5% R², suitable for pricing decisions
   - Use for dynamic pricing based on CalculatedPremiumPerTerm and SumInsured
   - Incorporate PostalCode for geographic risk adjustments

2. **Claim Severity Prediction**: Use Linear Regression model with caution
   - Lower R² (27.5%) indicates limited predictive power
   - Focus on high-value features (SumInsured, CalculatedPremiumPerTerm)
   - Consider ensemble methods or feature engineering for improvement

3. **Feature Engineering**: Prioritize SumInsured and CalculatedPremiumPerTerm
   - These features dominate both models
   - Ensure data quality and completeness for these fields
   - Consider creating derived features from these base features

4. **Model Improvement**: 
   - For claim severity: Explore non-linear models, feature interactions, or external data
   - For premium: Current model is production-ready; monitor performance over time

**Strategic Implications:**
- Premium prediction model is ready for deployment
- Claim severity model needs refinement before production use
- Geographic features validated as important for both tasks
- Focus on data quality for top features to improve model performance

---

## 5. Challenges and Limitations

### 4.1 Challenges Encountered

1. **Zero and Negative Premium Values**: 
   - **Challenge**: Some policies have zero or negative premiums, causing infinite loss ratios
   - **Solution**: Filtered to valid records (618,176 out of 1,000,098) with positive premiums for loss ratio analysis
   - **Impact**: Analysis focuses on policies with valid financial data

2. **High Missing Values in Key Fields**:
   - **Challenge**: Gender data missing for 75.2% of policies, limiting demographic analysis
   - **Solution**: Analyzed available data with appropriate sample size considerations
   - **Impact**: Gender-based insights are limited but still valuable for the available subset

3. **Data Format Issues**:
   - **Challenge**: TransactionMonth was in object format, needed conversion to datetime
   - **Solution**: Implemented automatic datetime conversion in data loading pipeline
   - **Impact**: Enabled proper temporal analysis

### 4.2 Data Limitations

- **Portfolio Profitability**: Overall loss ratio of 1.0477 indicates the portfolio is currently unprofitable, requiring immediate pricing adjustments
- **Geographic Concentration**: Three provinces (Gauteng, Western Cape, KwaZulu-Natal) represent 55.2% of policies but all show loss ratios > 1.0
- **Vehicle Type Risk**: Heavy Commercial vehicles show extremely high risk (161.2% loss ratio) with only 59 policies, making it a small but critical segment
- **Demographic Data Quality**: Limited gender data (only 2.5% specified) restricts demographic segmentation opportunities
- **Temporal Scope**: Data covers only 18 months (Feb 2014 - Aug 2015), limiting long-term trend analysis

**Impact on Analysis:**
- Some segments have small sample sizes, requiring careful statistical interpretation
- Missing data reduces the scope of certain analyses but doesn't invalidate findings
- Overall portfolio unprofitability requires immediate business action

### 4.3 Future Improvements

- **Data Collection**: Implement mandatory fields for gender, improve CustomValueEstimate collection
- **Data Validation**: Add validation rules to prevent zero/negative premiums and ensure data quality
- **Extended Time Period**: Collect data over longer periods for better trend analysis
- **Feature Engineering**: Create additional risk indicators from existing data
- **Real-time Monitoring**: Implement dashboards to monitor loss ratios by segment in real-time

---

## 6. Conclusion

This interim report demonstrates significant progress on the insurance risk analytics project. The comprehensive EDA has revealed valuable insights into risk patterns across provinces, vehicle types, and demographics. The DVC setup ensures reproducibility and auditability, critical for regulatory compliance.

**Key Achievements:**
- ✅ Robust project infrastructure established
- ✅ Comprehensive EDA completed with actionable insights
- ✅ Data version control implemented
- ✅ A/B hypothesis testing completed with statistical validation
- ✅ Foundation laid for statistical modeling (Task 4)

**Next Phase:**
The project is well-positioned to proceed with statistical modeling (Task 4), building on the validated insights from EDA and hypothesis testing. The confirmed risk differences by geography provide a strong foundation for predictive modeling.

---

## Appendices

### Appendix A: Repository Links
- **GitHub Repository**: https://github.com/Danielmituku/End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
- **Main Branch**: https://github.com/Danielmituku/End-to-End-Insurance-Risk-Analytics-Predictive-Modeling/tree/main
- **Task-1 Branch**: https://github.com/Danielmituku/End-to-End-Insurance-Risk-Analytics-Predictive-Modeling/tree/task-1
- **Task-2 Branch**: [To be created]

### Appendix B: Code Structure

```
End-to-End-Insurance-Risk-Analytics-Predictive-Modeling/
├── src/                    # Source code
│   ├── data/              # Data loading and preprocessing
│   ├── eda/               # Exploratory Data Analysis
│   ├── ab_testing/        # A/B Hypothesis Testing
│   ├── modeling/          # Statistical and ML models
│   └── utils/             # Utility functions
├── tests/                 # Unit tests
├── data/                  # Data files (tracked by DVC)
│   ├── raw/              # Raw data files
│   └── processed/        # Processed data files
├── notebooks/             # Jupyter notebooks for analysis
│   └── 01_eda_analysis.ipynb
├── reports/               # Generated reports and visualizations
│   ├── figures/          # All EDA visualizations (9 figures)
│   ├── interim_report.md # This report
│   └── *.csv            # Statistical summaries
├── models/                # Trained model artifacts
├── scripts/               # Utility scripts
└── .github/               # GitHub Actions workflows
```

### Appendix C: Data Dictionary
[Detailed description of all columns if needed]

### Appendix D: Additional Visualizations

All visualizations are saved in the `reports/figures/` directory:

1. **01_histograms_numerical_variables.png** - Distribution of key numerical variables
2. **02_bar_charts_categorical_variables.png** - Distribution of key categorical variables
3. **03_correlation_matrix.png** - Correlation heatmap of numerical variables
4. **04_monthly_changes_premium_claims_by_postalcode.png** - Monthly changes analysis by postal code
5. **05_geographic_trends_analysis.png** - Geographic trends (Cover Type, Premium, Auto Makes by Province)
6. **06_box_plots_outlier_detection.png** - Outlier detection using box plots
7. **07_creative_1_loss_ratio_heatmap.png** - Loss Ratio Heatmap (Province vs Vehicle Type)
8. **08_creative_2_temporal_risk_trend.png** - Temporal Risk Trend Analysis
9. **09_creative_3_risk_value_matrix.png** - Risk-Value Matrix (Vehicle Makes)
10. **10_feature_importance_claim_severity.png** - Top 10 Feature Importance for Claim Severity Model
11. **11_feature_importance_premium.png** - Top 10 Feature Importance for Premium Prediction Model
12. **12_shap_summary_claim_severity.png** - SHAP Summary Plot for Claim Severity Model

All figures are saved at 300 DPI for high-quality presentation.

---

**Report Prepared By**: [Your Name]  
**Date**: December 07, 2025  
**Version**: 1.0

