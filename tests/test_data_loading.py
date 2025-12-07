"""Tests for data loading functions."""

import pytest
import pandas as pd
from pathlib import Path
from src.data.load_data import load_insurance_data, get_data_info


def test_get_data_info():
    """Test get_data_info function."""
    # Create a sample dataframe
    df = pd.DataFrame({
        "col1": [1, 2, 3, None],
        "col2": ["a", "b", "c", "d"],
        "col3": [1.1, 2.2, 3.3, 4.4]
    })
    
    info = get_data_info(df)
    
    assert "shape" in info
    assert "columns" in info
    assert "dtypes" in info
    assert "missing_values" in info
    assert info["shape"] == (4, 3)
    assert len(info["columns"]) == 3
    assert info["missing_values"]["col1"] == 1

