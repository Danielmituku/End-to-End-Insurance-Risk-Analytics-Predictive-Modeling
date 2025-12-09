"""A/B Hypothesis Testing for Insurance Risk Analytics.

This module contains functions to test various hypotheses about risk differences
across provinces, zip codes, and demographics.
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Tuple, Dict, List
import warnings

warnings.filterwarnings('ignore')


def calculate_claim_frequency(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Calculate claim frequency (proportion of policies with at least one claim) by group.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with TotalClaims column
    group_col : str
        Column name to group by (e.g., 'Province', 'PostalCode', 'Gender')
    
    Returns
    -------
    pd.DataFrame
        Summary statistics with claim frequency by group
    """
    df = df.copy()
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    
    summary = df.groupby(group_col).agg({
        'HasClaim': ['sum', 'count', 'mean'],
        'TotalPremium': 'sum',
        'TotalClaims': 'sum'
    }).reset_index()
    
    summary.columns = [
        group_col, 'Claims_Count', 'Total_Policies', 'Claim_Frequency',
        'Total_Premium', 'Total_Claims'
    ]
    
    summary['Claim_Severity'] = summary['Total_Claims'] / summary['Claims_Count']
    summary['Margin'] = summary['Total_Premium'] - summary['Total_Claims']
    summary['Loss_Ratio'] = summary['Total_Claims'] / summary['Total_Premium']
    
    return summary


def calculate_claim_severity(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Calculate claim severity (average claim amount given a claim occurred) by group.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    group_col : str
        Column name to group by
    
    Returns
    -------
    pd.DataFrame
        Claim severity statistics by group
    """
    df_with_claims = df[df['TotalClaims'] > 0].copy()
    
    if len(df_with_claims) == 0:
        return pd.DataFrame()
    
    severity = df_with_claims.groupby(group_col).agg({
        'TotalClaims': ['mean', 'std', 'count']
    }).reset_index()
    
    severity.columns = [group_col, 'Mean_Severity', 'Std_Severity', 'Claim_Count']
    
    return severity


def test_province_risk_differences(df: pd.DataFrame, alpha: float = 0.05) -> Dict:
    """
    Test H₀: There are no risk differences across provinces.
    
    Uses chi-squared test for claim frequency and ANOVA/t-test for claim severity.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    alpha : float
        Significance level (default: 0.05)
    
    Returns
    -------
    dict
        Test results including p-value, statistic, and interpretation
    """
    results = {}
    
    # Prepare data
    df = df.copy()
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    
    # Test 1: Claim Frequency (Chi-squared test)
    contingency_table = pd.crosstab(df['Province'], df['HasClaim'])
    
    if contingency_table.shape[0] < 2:
        results['frequency_test'] = {
            'test': 'chi2_contingency',
            'statistic': None,
            'p_value': None,
            'result': 'Insufficient data'
        }
    else:
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        results['frequency_test'] = {
            'test': 'chi2_contingency',
            'statistic': chi2,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'reject_null': p_value < alpha,
            'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀'
        }
    
    # Test 2: Claim Severity (ANOVA or Kruskal-Wallis)
    df_with_claims = df[df['TotalClaims'] > 0].copy()
    
    if len(df_with_claims) == 0:
        results['severity_test'] = {
            'test': 'ANOVA',
            'statistic': None,
            'p_value': None,
            'result': 'No claims data available'
        }
    else:
        # Group by province
        groups = [group['TotalClaims'].values 
                 for name, group in df_with_claims.groupby('Province')]
        
        # Remove groups with less than 2 observations
        groups = [g for g in groups if len(g) >= 2]
        
        if len(groups) < 2:
            results['severity_test'] = {
                'test': 'ANOVA',
                'statistic': None,
                'p_value': None,
                'result': 'Insufficient groups for ANOVA'
            }
        else:
            # Test normality (Shapiro-Wilk on sample)
            # Use Kruskal-Wallis if data is not normal
            try:
                f_stat, p_value = stats.f_oneway(*groups)
                test_name = 'ANOVA'
            except:
                # Use Kruskal-Wallis (non-parametric alternative)
                h_stat, p_value = stats.kruskal(*groups)
                test_name = 'Kruskal-Wallis'
                f_stat = h_stat
            
            results['severity_test'] = {
                'test': test_name,
                'statistic': f_stat,
                'p_value': p_value,
                'reject_null': p_value < alpha,
                'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀'
            }
    
    # Overall interpretation
    freq_reject = results.get('frequency_test', {}).get('reject_null', False)
    sev_reject = results.get('severity_test', {}).get('reject_null', False)
    
    results['overall_interpretation'] = {
        'reject_null': freq_reject or sev_reject,
        'summary': 'Risk differences exist across provinces' if (freq_reject or sev_reject) 
                   else 'No significant risk differences across provinces'
    }
    
    return results


def test_zipcode_risk_differences(df: pd.DataFrame, alpha: float = 0.05, 
                                  top_n: int = 10) -> Dict:
    """
    Test H₀: There are no risk differences between zip codes.
    
    Tests top N zip codes by policy count to ensure sufficient sample sizes.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    alpha : float
        Significance level
    top_n : int
        Number of top zip codes to test (default: 10)
    
    Returns
    -------
    dict
        Test results
    """
    results = {}
    
    # Get top N zip codes by policy count
    zipcode_counts = df['PostalCode'].value_counts().head(top_n)
    top_zipcodes = zipcode_counts.index.tolist()
    
    df_filtered = df[df['PostalCode'].isin(top_zipcodes)].copy()
    df_filtered['HasClaim'] = (df_filtered['TotalClaims'] > 0).astype(int)
    
    # Test 1: Claim Frequency (Chi-squared test)
    contingency_table = pd.crosstab(df_filtered['PostalCode'], df_filtered['HasClaim'])
    
    if contingency_table.shape[0] < 2:
        results['frequency_test'] = {
            'test': 'chi2_contingency',
            'statistic': None,
            'p_value': None,
            'result': 'Insufficient data'
        }
    else:
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        results['frequency_test'] = {
            'test': 'chi2_contingency',
            'statistic': chi2,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'reject_null': p_value < alpha,
            'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀',
            'top_zipcodes_tested': top_zipcodes
        }
    
    # Test 2: Claim Severity
    df_with_claims = df_filtered[df_filtered['TotalClaims'] > 0].copy()
    
    if len(df_with_claims) == 0:
        results['severity_test'] = {
            'test': 'ANOVA',
            'statistic': None,
            'p_value': None,
            'result': 'No claims data available'
        }
    else:
        groups = [group['TotalClaims'].values 
                 for name, group in df_with_claims.groupby('PostalCode')]
        groups = [g for g in groups if len(g) >= 2]
        
        if len(groups) < 2:
            results['severity_test'] = {
                'test': 'ANOVA',
                'statistic': None,
                'p_value': None,
                'result': 'Insufficient groups for ANOVA'
            }
        else:
            try:
                f_stat, p_value = stats.f_oneway(*groups)
                test_name = 'ANOVA'
            except:
                h_stat, p_value = stats.kruskal(*groups)
                test_name = 'Kruskal-Wallis'
                f_stat = h_stat
            
            results['severity_test'] = {
                'test': test_name,
                'statistic': f_stat,
                'p_value': p_value,
                'reject_null': p_value < alpha,
                'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀'
            }
    
    freq_reject = results.get('frequency_test', {}).get('reject_null', False)
    sev_reject = results.get('severity_test', {}).get('reject_null', False)
    
    results['overall_interpretation'] = {
        'reject_null': freq_reject or sev_reject,
        'summary': 'Risk differences exist between zip codes' if (freq_reject or sev_reject)
                   else 'No significant risk differences between zip codes'
    }
    
    return results


def test_zipcode_margin_differences(df: pd.DataFrame, alpha: float = 0.05,
                                    top_n: int = 10) -> Dict:
    """
    Test H₀: There is no significant margin (profit) difference between zip codes.
    
    Margin = TotalPremium - TotalClaims
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    alpha : float
        Significance level
    top_n : int
        Number of top zip codes to test
    
    Returns
    -------
    dict
        Test results
    """
    results = {}
    
    # Get top N zip codes
    zipcode_counts = df['PostalCode'].value_counts().head(top_n)
    top_zipcodes = zipcode_counts.index.tolist()
    
    df_filtered = df[df['PostalCode'].isin(top_zipcodes)].copy()
    df_filtered['Margin'] = df_filtered['TotalPremium'] - df_filtered['TotalClaims']
    
    # Group by zip code
    groups = [group['Margin'].values 
             for name, group in df_filtered.groupby('PostalCode')]
    groups = [g for g in groups if len(g) >= 2]
    
    if len(groups) < 2:
        results['test'] = {
            'test': 'ANOVA',
            'statistic': None,
            'p_value': None,
            'result': 'Insufficient groups for ANOVA'
        }
    else:
        try:
            f_stat, p_value = stats.f_oneway(*groups)
            test_name = 'ANOVA'
        except:
            h_stat, p_value = stats.kruskal(*groups)
            test_name = 'Kruskal-Wallis'
            f_stat = h_stat
        
        results['test'] = {
            'test': test_name,
            'statistic': f_stat,
            'p_value': p_value,
            'reject_null': p_value < alpha,
            'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀',
            'top_zipcodes_tested': top_zipcodes
        }
    
    return results


def test_gender_risk_differences(df: pd.DataFrame, alpha: float = 0.05) -> Dict:
    """
    Test H₀: There is no significant risk difference between Women and Men.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    alpha : float
        Significance level
    
    Returns
    -------
    dict
        Test results
    """
    results = {}
    
    # Filter to only Male and Female (exclude "Not specified")
    df_filtered = df[df['Gender'].isin(['Male', 'Female'])].copy()
    
    if len(df_filtered) == 0:
        return {
            'error': 'No data with specified gender (Male/Female) available'
        }
    
    df_filtered['HasClaim'] = (df_filtered['TotalClaims'] > 0).astype(int)
    
    # Test 1: Claim Frequency (Chi-squared test)
    contingency_table = pd.crosstab(df_filtered['Gender'], df_filtered['HasClaim'])
    
    if contingency_table.shape[0] < 2:
        results['frequency_test'] = {
            'test': 'chi2_contingency',
            'statistic': None,
            'p_value': None,
            'result': 'Insufficient data'
        }
    else:
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        results['frequency_test'] = {
            'test': 'chi2_contingency',
            'statistic': chi2,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'reject_null': p_value < alpha,
            'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀'
        }
    
    # Test 2: Claim Severity (t-test or Mann-Whitney U)
    df_with_claims = df_filtered[df_filtered['TotalClaims'] > 0].copy()
    
    if len(df_with_claims) == 0:
        results['severity_test'] = {
            'test': 't-test',
            'statistic': None,
            'p_value': None,
            'result': 'No claims data available'
        }
    else:
        male_claims = df_with_claims[df_with_claims['Gender'] == 'Male']['TotalClaims'].values
        female_claims = df_with_claims[df_with_claims['Gender'] == 'Female']['TotalClaims'].values
        
        if len(male_claims) < 2 or len(female_claims) < 2:
            results['severity_test'] = {
                'test': 't-test',
                'statistic': None,
                'p_value': None,
                'result': 'Insufficient data for comparison'
            }
        else:
            # Try t-test first, use Mann-Whitney U if assumptions not met
            try:
                t_stat, p_value = stats.ttest_ind(male_claims, female_claims)
                test_name = 't-test'
            except:
                u_stat, p_value = stats.mannwhitneyu(male_claims, female_claims, alternative='two-sided')
                test_name = 'Mann-Whitney U'
                t_stat = u_stat
            
            results['severity_test'] = {
                'test': test_name,
                'statistic': t_stat,
                'p_value': p_value,
                'reject_null': p_value < alpha,
                'interpretation': 'Reject H₀' if p_value < alpha else 'Fail to reject H₀',
                'male_mean': np.mean(male_claims),
                'female_mean': np.mean(female_claims)
            }
    
    freq_reject = results.get('frequency_test', {}).get('reject_null', False)
    sev_reject = results.get('severity_test', {}).get('reject_null', False)
    
    results['overall_interpretation'] = {
        'reject_null': freq_reject or sev_reject,
        'summary': 'Risk differences exist between genders' if (freq_reject or sev_reject)
                   else 'No significant risk differences between genders'
    }
    
    return results


def format_test_results(results: Dict, hypothesis_name: str) -> str:
    """
    Format test results for reporting.
    
    Parameters
    ----------
    results : dict
        Test results dictionary
    hypothesis_name : str
        Name of the hypothesis being tested
    
    Returns
    -------
    str
        Formatted results string
    """
    output = f"\n{'='*80}\n"
    output += f"HYPOTHESIS: {hypothesis_name}\n"
    output += f"{'='*80}\n\n"
    
    for key, value in results.items():
        if key == 'overall_interpretation':
            continue
        if isinstance(value, dict):
            output += f"{key.upper().replace('_', ' ')}:\n"
            for k, v in value.items():
                if k != 'top_zipcodes_tested':
                    output += f"  {k}: {v}\n"
            output += "\n"
    
    if 'overall_interpretation' in results:
        output += f"OVERALL RESULT: {results['overall_interpretation']['summary']}\n"
        output += f"Reject H₀: {results['overall_interpretation']['reject_null']}\n"
    
    return output

