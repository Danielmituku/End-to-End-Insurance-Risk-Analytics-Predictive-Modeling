.PHONY: help install test lint format clean setup-dvc

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make format       - Format code with Black"
	@echo "  make clean        - Clean temporary files"
	@echo "  make setup-dvc    - Initialize DVC"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v --cov=src --cov-report=html

lint:
	flake8 src tests
	pylint src

format:
	black src tests

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/

setup-dvc:
	dvc init
	dvc remote add -d localstorage ./data/dvc_storage
	@echo "DVC initialized. Add data files with: dvc add data/raw/your_data.csv"

