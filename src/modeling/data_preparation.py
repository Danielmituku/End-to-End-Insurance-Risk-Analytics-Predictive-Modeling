"""Data preparation functions for modeling."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from typing import Tuple, List, Optional
import warnings

warnings.filterwarnings('ignore')


def prepare_claim_severity_data(df: pd.DataFrame, 
                                target_col: str = 'TotalClaims',
                                test_size: float = 0.2,
                                random_state: int = 42) -> Tuple:
    """
    Prepare data for claim severity prediction (policies with claims > 0).
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    target_col : str
        Target column name (default: 'TotalClaims')
    test_size : float
        Proportion of data for testing (default: 0.2)
    random_state : int
        Random seed for reproducibility
    
    Returns
    -------
    tuple
        (X_train, X_test, y_train, y_test, feature_names, preprocessor)
    """
    # Filter to policies with claims
    df_claims = df[df[target_col] > 0].copy()
    
    if len(df_claims) == 0:
        raise ValueError("No policies with claims found in the dataset")
    
    # Select features for modeling
    feature_cols = [
        'Province', 'PostalCode', 'Gender', 'MaritalStatus',
        'VehicleType', 'make', 'RegistrationYear', 'cubiccapacity',
        'kilowatts', 'SumInsured', 'CoverType', 'CalculatedPremiumPerTerm'
    ]
    
    # Filter to available columns
    available_cols = [col for col in feature_cols if col in df_claims.columns]
    X = df_claims[available_cols].copy()
    y = df_claims[target_col].copy()
    
    # Handle missing values
    # For numerical: fill with median
    numerical_cols = X.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        X[col].fillna(X[col].median(), inplace=True)
    
    # For categorical: fill with mode
    categorical_cols = X.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        X[col].fillna(X[col].mode()[0] if len(X[col].mode()) > 0 else 'Unknown', inplace=True)
    
    # Encode categorical variables
    X_encoded = encode_categorical_features(X, categorical_cols)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=test_size, random_state=random_state
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    feature_names = X_encoded.columns.tolist()
    
    return (X_train_scaled, X_test_scaled, y_train, y_test, 
            feature_names, {'scaler': scaler, 'encoders': {}})


def prepare_premium_prediction_data(df: pd.DataFrame,
                                    target_col: str = 'TotalPremium',
                                    test_size: float = 0.2,
                                    random_state: int = 42) -> Tuple:
    """
    Prepare data for premium prediction.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    target_col : str
        Target column name (default: 'TotalPremium')
    test_size : float
        Proportion of data for testing
    random_state : int
        Random seed
    
    Returns
    -------
    tuple
        (X_train, X_test, y_train, y_test, feature_names, preprocessor)
    """
    df_clean = df.copy()
    
    # Select features
    feature_cols = [
        'Province', 'PostalCode', 'Gender', 'MaritalStatus',
        'VehicleType', 'make', 'RegistrationYear', 'cubiccapacity',
        'kilowatts', 'SumInsured', 'CoverType', 'CalculatedPremiumPerTerm',
        'VehicleType', 'bodytype', 'NumberOfDoors'
    ]
    
    available_cols = [col for col in feature_cols if col in df_clean.columns]
    X = df_clean[available_cols].copy()
    y = df_clean[target_col].copy()
    
    # Remove rows with missing target
    mask = y.notna() & (y >= 0)  # Also filter negative premiums
    X = X[mask].copy()
    y = y[mask].copy()
    
    # Handle missing values
    numerical_cols = X.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        X[col].fillna(X[col].median(), inplace=True)
    
    categorical_cols = X.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        X[col].fillna(X[col].mode()[0] if len(X[col].mode()) > 0 else 'Unknown', inplace=True)
    
    # Encode categorical variables
    X_encoded = encode_categorical_features(X, categorical_cols)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=test_size, random_state=random_state
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    feature_names = X_encoded.columns.tolist()
    
    return (X_train_scaled, X_test_scaled, y_train, y_test,
            feature_names, {'scaler': scaler, 'encoders': {}})


def encode_categorical_features(X: pd.DataFrame, categorical_cols: List[str]) -> pd.DataFrame:
    """
    Encode categorical features using one-hot encoding.
    
    Parameters
    ----------
    X : pd.DataFrame
        Input dataframe
    categorical_cols : list
        List of categorical column names
    
    Returns
    -------
    pd.DataFrame
        Dataframe with encoded categorical features
    """
    X_encoded = X.copy()
    
    # One-hot encode categorical variables
    for col in categorical_cols:
        if col in X_encoded.columns:
            # Get dummies
            dummies = pd.get_dummies(X_encoded[col], prefix=col, drop_first=True)
            X_encoded = pd.concat([X_encoded.drop(columns=[col]), dummies], axis=1)
    
    return X_encoded


def create_claim_probability_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary feature indicating if a policy has a claim.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    
    Returns
    -------
    pd.DataFrame
        Dataframe with 'HasClaim' feature added
    """
    df = df.copy()
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    return df

