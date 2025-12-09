# Task 3: A/B Hypothesis Testing - Setup Complete

## ✅ Framework Created

### 1. Hypothesis Testing Module
- **File**: `src/ab_testing/hypothesis_tests.py`
- **Functions Created**:
  - `calculate_claim_frequency()` - Calculate claim frequency by group
  - `calculate_claim_severity()` - Calculate claim severity by group
  - `test_province_risk_differences()` - Test Hypothesis 1
  - `test_zipcode_risk_differences()` - Test Hypothesis 2
  - `test_zipcode_margin_differences()` - Test Hypothesis 3
  - `test_gender_risk_differences()` - Test Hypothesis 4
  - `format_test_results()` - Format results for reporting

### 2. Statistical Tests Implemented

**For Claim Frequency (Categorical):**
- Chi-squared test for independence

**For Claim Severity (Continuous):**
- ANOVA (when assumptions met)
- Kruskal-Wallis (non-parametric alternative)
- t-test (for two groups)
- Mann-Whitney U (non-parametric alternative)

**For Margin (Continuous):**
- ANOVA
- Kruskal-Wallis

### 3. Notebook Created
- **File**: `notebooks/02_ab_hypothesis_testing.ipynb`
- Template with all 4 hypothesis tests
- Summary section for business recommendations

### 4. Tests Created
- **File**: `tests/test_hypothesis_tests.py`
- Unit tests for all hypothesis testing functions

## 📋 Hypotheses to Test

1. **H₀**: There are no risk differences across provinces
2. **H₀**: There are no risk differences between zip codes
3. **H₀**: There is no significant margin (profit) difference between zip codes
4. **H₀**: There is no significant risk difference between Women and Men

## 📊 Metrics Used

- **Claim Frequency**: Proportion of policies with at least one claim
- **Claim Severity**: Average claim amount (given a claim occurred)
- **Margin**: TotalPremium - TotalClaims

## 🔧 Next Steps

1. Run the notebook: `notebooks/02_ab_hypothesis_testing.ipynb`
2. Execute all hypothesis tests
3. Review results and p-values
4. Create business recommendations based on findings
5. Update interim report with results
6. Commit and push changes

## ✅ Requirements Met

- ✅ Branch `task-3` created
- ✅ Hypothesis testing framework implemented
- ✅ All 4 hypotheses have test functions
- ✅ Statistical tests properly implemented
- ✅ Notebook template created
- ✅ Unit tests added

