# Quick Start Guide

This guide will help you get started with the Insurance Risk Analytics project quickly.

## 🚀 Initial Setup

### 1. Install Dependencies

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Or use the Makefile:
```bash
make install
```

### 2. Set Up Git (Task 1.1)

```bash
# Initialize git (if not already done)
git init

# Create task-1 branch
git checkout -b task-1

# Add all files
git add .

# Make your first commit
git commit -m "feat: initial project setup with structure and CI/CD"
```

### 3. Set Up DVC (Task 2)

```bash
# Initialize DVC
dvc init

# Set up local remote storage
mkdir -p data/dvc_storage
dvc remote add -d localstorage ./data/dvc_storage

# When you have data, add it:
# dvc add data/raw/insurance_data.csv
# git add data/raw/insurance_data.csv.dvc
# git commit -m "data: add insurance dataset"
# dvc push
```

Or use the Makefile:
```bash
make setup-dvc
```

## 📊 Getting Started with EDA (Task 1.2)

### Option 1: Use Jupyter Notebook

```bash
# Start Jupyter
jupyter notebook

# Open notebooks/01_eda_analysis.ipynb
```

### Option 2: Use Python Scripts

```python
from src.data.load_data import load_insurance_data, get_data_info

# Load data
df = load_insurance_data()

# Get data info
info = get_data_info(df)
print(info)
```

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html

# Or use Makefile
make test
```

## 🔍 Code Quality

```bash
# Format code
make format
# or
black src tests

# Lint code
make lint
# or
flake8 src tests
pylint src
```

## 📝 Workflow for Each Task

### Task 1: EDA
1. Create branch: `git checkout -b task-1`
2. Work on EDA in `notebooks/` or `src/eda/`
3. Commit frequently with descriptive messages
4. Push: `git push origin task-1`
5. Create PR to merge into main

### Task 2: DVC
1. Merge task-1 into main via PR
2. Create branch: `git checkout -b task-2`
3. Set up DVC (see above)
4. Add and version control data files
5. Commit and push
6. Create PR to merge into main

### Task 3: A/B Testing
1. Merge task-2 into main via PR
2. Create branch: `git checkout -b task-3`
3. Implement hypothesis tests in `src/ab_testing/`
4. Commit and push
5. Create PR to merge into main

### Task 4: Modeling
1. Merge task-3 into main via PR
2. Create branch: `git checkout -b task-4`
3. Build models in `src/modeling/`
4. Commit and push
5. Create PR to merge into main

## 📁 Project Structure Overview

```
.
├── src/              # Source code
│   ├── data/        # Data loading
│   ├── eda/         # EDA analysis
│   ├── ab_testing/  # Hypothesis testing
│   ├── modeling/    # ML models
│   └── utils/       # Utilities
├── tests/           # Unit tests
├── data/            # Data files (DVC tracked)
├── notebooks/       # Jupyter notebooks
├── reports/         # Generated reports
└── models/          # Trained models
```

## 🔗 Next Steps

1. **Download the data** from the provided link and place it in `data/raw/`
2. **Start EDA** using the notebook template in `notebooks/01_eda_analysis.ipynb`
3. **Follow the task requirements** in the main README.md
4. **Commit frequently** with descriptive messages
5. **Create PRs** for each task branch

## 💡 Tips

- Use the Makefile for common tasks: `make help`
- Follow conventional commits: `feat:`, `fix:`, `docs:`, etc.
- Write tests as you develop
- Document your code with docstrings
- Keep the README updated with your findings

## 🆘 Need Help?

- Check the main README.md for detailed task descriptions
- Review CONTRIBUTING.md for development guidelines
- Check the references section in README.md for learning resources

Happy coding! 🎉

