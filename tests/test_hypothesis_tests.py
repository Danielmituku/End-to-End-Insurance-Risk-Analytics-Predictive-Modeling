"""Tests for hypothesis testing functions."""

import pytest
import pandas as pd
import numpy as np
from src.ab_testing.hypothesis_tests import (
    calculate_claim_frequency,
    calculate_claim_severity,
    test_province_risk_differences,
    test_zipcode_risk_differences,
    test_zipcode_margin_differences,
    test_gender_risk_differences
)


@pytest.fixture
def sample_data():
    """Create sample insurance data for testing."""
    np.random.seed(42)
    n = 1000
    
    data = {
        'Province': np.random.choice(['Gauteng', 'Western Cape', 'KwaZulu-Natal'], n),
        'PostalCode': np.random.choice([1000, 2000, 3000, 4000, 5000], n),
        'Gender': np.random.choice(['Male', 'Female', 'Not specified'], n),
        'TotalPremium': np.random.uniform(10, 1000, n),
        'TotalClaims': np.random.choice([0, 0, 0, 100, 200, 300], n)  # Most have no claims
    }
    
    return pd.DataFrame(data)


def test_calculate_claim_frequency(sample_data):
    """Test claim frequency calculation."""
    result = calculate_claim_frequency(sample_data, 'Province')
    
    assert 'Province' in result.columns
    assert 'Claim_Frequency' in result.columns
    assert 'Total_Policies' in result.columns
    assert len(result) > 0


def test_calculate_claim_severity(sample_data):
    """Test claim severity calculation."""
    result = calculate_claim_severity(sample_data, 'Province')
    
    if len(result) > 0:
        assert 'Province' in result.columns
        assert 'Mean_Severity' in result.columns


def test_test_province_risk_differences(sample_data):
    """Test province risk differences function."""
    result = test_province_risk_differences(sample_data, alpha=0.05)
    
    assert 'frequency_test' in result
    assert 'severity_test' in result
    assert 'overall_interpretation' in result


def test_test_gender_risk_differences(sample_data):
    """Test gender risk differences function."""
    result = test_gender_risk_differences(sample_data, alpha=0.05)
    
    assert 'frequency_test' in result or 'error' in result
    if 'overall_interpretation' in result:
        assert isinstance(result['overall_interpretation']['reject_null'], bool)

