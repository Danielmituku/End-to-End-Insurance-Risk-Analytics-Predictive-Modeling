"""Data loading utilities."""

import pandas as pd
from pathlib import Path
from typing import Optional
from src.utils.config import RAW_DATA_DIR


def load_insurance_data(file_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load insurance data from CSV or text file.
    
    Parameters
    ----------
    file_path : str, optional
        Path to the data file. If None, looks for data in RAW_DATA_DIR.
    
    Returns
    -------
    pd.DataFrame
        Loaded insurance data.
    
    Raises
    ------
    FileNotFoundError
        If the data file is not found.
    """
    if file_path is None:
        # Look for common data file names (CSV and TXT)
        possible_files = list(RAW_DATA_DIR.glob("*.csv")) + list(RAW_DATA_DIR.glob("*.txt"))
        if not possible_files:
            raise FileNotFoundError(
                f"No data files (CSV or TXT) found in {RAW_DATA_DIR}. "
                "Please provide a file_path or place data in the raw data directory."
            )
        file_path = possible_files[0]
    
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")
    
    print(f"Loading data from: {file_path}")
    
    # Detect delimiter based on file extension and content
    if file_path.suffix.lower() == '.txt':
        # Try pipe delimiter first (common for insurance data)
        # If that fails, try comma
        try:
            df = pd.read_csv(file_path, sep='|', low_memory=False)
        except Exception:
            df = pd.read_csv(file_path, sep=',', low_memory=False)
    else:
        # For CSV files, use comma delimiter
        df = pd.read_csv(file_path, low_memory=False)
    
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    
    return df


def get_data_info(df: pd.DataFrame) -> dict:
    """
    Get basic information about the dataset.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    
    Returns
    -------
    dict
        Dictionary containing data information.
    """
    info = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024**2,
    }
    return info

