# Data Directory

This directory contains the insurance data files.

## Structure

- `raw/`: Original, unprocessed data files
- `processed/`: Cleaned and processed data files

## Data Files

The insurance data should be placed in the `raw/` directory. The data spans from February 2014 to August 2015.

## Data Version Control

Data files are tracked using DVC (Data Version Control). To add data:

```bash
dvc add data/raw/insurance_data.csv
git add data/raw/insurance_data.csv.dvc
git commit -m "data: add insurance dataset"
dvc push
```

## Data Schema

See the main README.md for a complete description of the data columns.

