# Task 1: Minimum Essential Checklist

## ✅ Completed Items

- [x] **GitHub Repository**: Created and configured
- [x] **Branch Creation**: `task-1` branch created and active
- [x] **Data Loading**: Data successfully loaded (1,000,098 rows, 52 columns)
- [x] **Basic Data Info**: Dataset shape and column names reviewed
- [x] **Missing Values Check**: Missing values analysis completed
- [x] **Initial Descriptive Statistics**: Basic stats for financial variables

## ⚠️ Partially Completed

- [~] **Commits**: 3 commits made, but need to ensure "at least three times a day" during active work
- [~] **Descriptive Statistics**: Started but need to complete variability calculations for all numerical features

## ❌ Missing Items

### 1. Data Summarization
- [ ] **Descriptive Statistics - Variability**: 
  - Need to calculate standard deviation, variance, range, IQR for ALL numerical features (not just financial ones)
  - Include: TotalPremium, TotalClaims, SumInsured, CustomValueEstimate, RegistrationYear, Cubiccapacity, Kilowatts, etc.

- [ ] **Data Structure Review**:
  - Review dtype of each column
  - Check if categorical variables are properly formatted (object vs category)
  - Check if dates (TransactionMonth) are properly formatted as datetime
  - Identify which columns should be categorical vs numerical

### 2. Univariate Analysis
- [ ] **Distribution of Variables**:
  - [ ] Histograms for ALL numerical columns (TotalPremium, TotalClaims, SumInsured, RegistrationYear, etc.)
  - [ ] Bar charts for ALL categorical columns (Province, Gender, VehicleType, Make, CoverType, etc.)
  - [ ] Analyze distribution shapes (normal, skewed, bimodal, etc.)

### 3. Bivariate/Multivariate Analysis
- [ ] **Correlations and Associations**:
  - [ ] Calculate correlation matrix for numerical variables
  - [ ] Create scatter plots showing relationships
  - [ ] **SPECIFIC REQUIREMENT**: Explore relationships between monthly changes in TotalPremium and TotalClaims as a function of ZipCode (PostalCode)
  - [ ] Create correlation heatmap

### 4. Data Comparison
- [ ] **Trends Over Geography**:
  - [ ] Compare insurance cover type by Province/PostalCode
  - [ ] Compare premium by Province/PostalCode
  - [ ] Compare auto make by Province/PostalCode
  - [ ] Visualize geographic patterns

### 5. Outlier Detection
- [ ] **Box Plots**:
  - [ ] Create box plots for ALL numerical variables
  - [ ] Identify outliers in TotalPremium
  - [ ] Identify outliers in TotalClaims
  - [ ] Identify outliers in CustomValueEstimate
  - [ ] Identify outliers in other key numerical features
  - [ ] Document outlier handling strategy

### 6. Visualization
- [ ] **3 Creative and Beautiful Plots**:
  - [ ] Plot 1: [Description of creative visualization]
  - [ ] Plot 2: [Description of creative visualization]
  - [ ] Plot 3: [Description of creative visualization]
  - These should capture KEY INSIGHTS from EDA

### 7. Commit Frequency
- [ ] Ensure commits are made at least 3 times per day during active work
- [ ] Use descriptive commit messages following conventional commits

---

## Recommended Next Steps

1. **Complete Data Structure Review**: Check and fix data types
2. **Create Univariate Analysis**: Histograms and bar charts for all variables
3. **Perform Bivariate Analysis**: Focus on ZipCode relationships with monthly changes
4. **Geographic Analysis**: Compare trends across provinces and zip codes
5. **Outlier Analysis**: Box plots for all numerical variables
6. **Creative Visualizations**: Design 3 insightful plots
7. **Document Findings**: Update interim report with all findings

---

## Notes

- The data file is `MachineLearningRating_v3.txt` (not CSV, so may need delimiter specification)
- TransactionMonth needs to be converted to datetime
- Many columns have high missing values (e.g., NumberOfVehiclesInFleet 100%, CrossBorder 99.9%)
- Loss Ratio calculation shows some issues (inf values) - need to handle division by zero

