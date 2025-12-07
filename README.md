# End-to-End Insurance Risk Analytics & Predictive Modeling

A comprehensive, production-grade analytics project focused on uncovering low-risk customer segments, validating risk hypotheses, and building predictive models for dynamic insurance pricing.

## 📋 Project Overview

**Client**: AlphaCare Insurance Solutions (ACIS)  
**Objective**: Analyze historical insurance claim data to optimize marketing strategy and discover "low-risk" targets for premium reduction, thereby attracting new clients.

**Challenge Period**: December 03-09, 2025

## 🎯 Business Objectives

- **Risk Segmentation**: Identify low-risk customer segments across provinces, zip codes, and demographics
- **Premium Optimization**: Develop data-driven pricing strategies to attract new clients
- **Predictive Modeling**: Build models to predict claim severity and optimal premium values
- **Hypothesis Validation**: Statistically validate risk drivers through A/B testing

## 📊 Data Overview

The historical data spans from **February 2014 to August 2015** and includes:

- **Policy Information**: UnderwrittenCoverID, PolicyID, TransactionMonth
- **Client Demographics**: Gender, MaritalStatus, Citizenship, LegalType, etc.
- **Location Data**: Country, Province, PostalCode, MainCrestaZone, SubCrestaZone
- **Vehicle Information**: Make, Model, VehicleType, RegistrationYear, Cubiccapacity, etc.
- **Plan Details**: SumInsured, TermFrequency, CalculatedPremiumPerTerm, CoverType, etc.
- **Financial Metrics**: TotalPremium, TotalClaims

## 🏗️ Project Structure

```
.
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
├── reports/               # Generated reports and visualizations
├── models/                # Trained model artifacts
├── .github/               # GitHub Actions workflows
└── .dvc/                  # DVC configuration

```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- DVC (Data Version Control)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize DVC** (for Task 2)
   ```bash
   dvc init
   dvc remote add -d localstorage ./data/dvc_storage
   ```

## 📚 Tasks Overview

### Task 1: Git/GitHub & EDA

**1.1 Git and GitHub**
- ✅ Repository setup with comprehensive README
- ✅ Git version control with descriptive commits
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Branch management (task-1, task-2, task-3, task-4)

**1.2 Project Planning - EDA & Stats**
- Data understanding and quality assessment
- Exploratory Data Analysis (EDA)
- Statistical distributions and visualizations
- Key insights discovery

**Key Questions to Answer:**
- What is the overall Loss Ratio (TotalClaims / TotalPremium)?
- How does Loss Ratio vary by Province, VehicleType, and Gender?
- What are the distributions of key financial variables?
- Are there temporal trends in claim frequency/severity?
- Which vehicle makes/models have highest/lowest claim amounts?

### Task 2: Data Version Control (DVC)

- Install and configure DVC
- Set up local remote storage
- Track data files with DVC
- Version control data changes
- Push data to remote storage

### Task 3: A/B Hypothesis Testing

Test the following null hypotheses:

1. **H₀**: There are no risk differences across provinces
2. **H₀**: There are no risk differences between zip codes
3. **H₀**: There is no significant margin (profit) difference between zip codes
4. **H₀**: There is no significant risk difference between Women and Men

**Metrics:**
- Claim Frequency (proportion of policies with at least one claim)
- Claim Severity (average claim amount, given a claim occurred)
- Margin (TotalPremium - TotalClaims)

### Task 4: Statistical Modeling

**Modeling Goals:**

1. **Claim Severity Prediction** (Risk Model)
   - Predict TotalClaims for policies with claims > 0
   - Evaluation: RMSE, R-squared

2. **Premium Optimization** (Pricing Framework)
   - Predict optimal premium values
   - Advanced: Predict claim probability + severity for risk-based pricing

**Models to Implement:**
- Linear Regression
- Decision Trees
- Random Forests
- XGBoost

**Model Interpretability:**
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-agnostic Explanations)
- Feature importance analysis

## 🔄 Workflow

### Branch Strategy

- `main`: Production-ready code
- `task-1`: EDA and initial analysis
- `task-2`: DVC setup and data versioning
- `task-3`: A/B hypothesis testing
- `task-4`: Statistical modeling

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add EDA analysis for loss ratio by province
fix: correct data preprocessing pipeline
docs: update README with installation instructions
test: add unit tests for data loading functions
refactor: reorganize modeling module structure
```

## 📈 Key Metrics & KPIs

### Business Metrics
- **Loss Ratio**: TotalClaims / TotalPremium
- **Claim Frequency**: Proportion of policies with claims
- **Claim Severity**: Average claim amount
- **Margin**: TotalPremium - TotalClaims

### Model Performance Metrics
- **RMSE**: Root Mean Squared Error
- **R²**: Coefficient of Determination
- **Feature Importance**: SHAP values

## 🧪 Testing

Run tests with:
```bash
pytest tests/ -v --cov=src --cov-report=html
```

## 📝 Documentation

- Code documentation follows Google-style docstrings
- Reports are generated in `reports/` directory
- Final report will be in Medium blog post format

## 🗓️ Key Dates

- **Challenge Introduction**: December 03, 2025 (10:30 AM UTC)
- **Interim Submission**: December 07, 2025 (8:00 PM UTC)
- **Final Submission**: December 09, 2025 (8:00 PM UTC)

## 📦 Deliverables

### Interim Submission (Dec 07, 2025)
- GitHub link to main branch with merged task-1 and task-2
- Interim report covering EDA findings and DVC setup

### Final Submission (Dec 09, 2025)
- GitHub link to main branch
- Final report (Medium blog post format) including:
  - Non-technical overview for leadership
  - Analytical approach description
  - Key insights from EDA, hypothesis testing, and modeling
  - Data-backed recommendations for marketing and pricing strategy
  - Limitations and future work suggestions

## 👥 Team

- **Facilitators**: Kerod, Mahbubah, Filimon

## 📚 References

### Insurance Analytics
- [FSRA Insurance Analytics](https://www.fsrao.ca/media/11501/download)
- [Data Analytics in Insurance](https://www.xenonstack.com/blog/data-analytics-in-insurance)
- [Connected Car & Insurance Analytics](https://www.swissre.com/risk-knowledge/driving-digital-insurance-solutions/connected-car-how-data-analytics-is-shaping-the-future-of-auto-insurance.html)

### A/B Testing
- [A/B Testing in Healthcare](https://www.engagys.com/insights/a-b-testing-the-key-to-effective-healthcare-communications)
- [A/B Testing Hypothesis Testing](https://medium.com/tiket-com/a-b-testing-hypothesis-testing-f9624ea5580e)

### Data Version Control
- [DVC Documentation](https://dvc.org/)
- [DVC User Guide](https://dvc.org/doc/user-guide)

### Statistical Modeling
- [Statistical Modeling Guide](https://www.heavy.ai/technical-glossary/statistical-modeling)
- [Random Forest Algorithm](https://builtin.com/data-science/random-forest-algorithm)
- [XGBoost Explained](https://www.analyticsvidhya.com/blog/2018/09/an-end-to-end-guide-to-understand-the-math-behind-xgboost/)

### Version Control & CI/CD
- [Git Branching](https://learngitbranching.js.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

## 📄 License

This project is part of the 10Academy Week 3 Challenge.

## 🤝 Contributing

This is a challenge project. For questions or issues, please create a GitHub issue.

---

**Status**: 🚧 In Progress  
**Last Updated**: December 2025
