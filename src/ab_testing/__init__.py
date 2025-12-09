"""A/B Hypothesis Testing modules for insurance risk analytics."""

from .hypothesis_tests import (
    calculate_claim_frequency,
    calculate_claim_severity,
    test_province_risk_differences,
    test_zipcode_risk_differences,
    test_zipcode_margin_differences,
    test_gender_risk_differences,
    format_test_results
)

__all__ = [
    'calculate_claim_frequency',
    'calculate_claim_severity',
    'test_province_risk_differences',
    'test_zipcode_risk_differences',
    'test_zipcode_margin_differences',
    'test_gender_risk_differences',
    'format_test_results'
]
