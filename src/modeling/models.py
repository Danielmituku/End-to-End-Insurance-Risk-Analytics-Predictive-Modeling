"""Machine learning models for insurance risk analytics."""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from typing import Dict, Tuple, Any
import warnings

warnings.filterwarnings('ignore')

# Try to import XGBoost, but make it optional
try:
    from xgboost import XGBRegressor
    XGBOOST_AVAILABLE = True
except ImportError as e:
    XGBOOST_AVAILABLE = False
    XGBRegressor = None
    warnings.warn(f"XGBoost not available: {e}. XGBoost models will not work. Install with: pip install xgboost")


def train_linear_regression(X_train: np.ndarray, y_train: np.ndarray,
                            **kwargs) -> Tuple[Any, Dict]:
    """
    Train a linear regression model.
    
    Parameters
    ----------
    X_train : np.ndarray
        Training features
    y_train : np.ndarray
        Training target
    **kwargs
        Additional arguments for LinearRegression
    
    Returns
    -------
    tuple
        (model, training_metrics)
    """
    model = LinearRegression(**kwargs)
    model.fit(X_train, y_train)
    
    # Training metrics
    y_pred_train = model.predict(X_train)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    train_r2 = r2_score(y_train, y_pred_train)
    train_mae = mean_absolute_error(y_train, y_pred_train)
    
    metrics = {
        'train_rmse': train_rmse,
        'train_r2': train_r2,
        'train_mae': train_mae
    }
    
    return model, metrics


def train_decision_tree(X_train: np.ndarray, y_train: np.ndarray,
                       max_depth: int = 10,
                       min_samples_split: int = 5,
                       **kwargs) -> Tuple[Any, Dict]:
    """
    Train a decision tree regressor.
    
    Parameters
    ----------
    X_train : np.ndarray
        Training features
    y_train : np.ndarray
        Training target
    max_depth : int
        Maximum depth of the tree
    min_samples_split : int
        Minimum samples required to split
    **kwargs
        Additional arguments for DecisionTreeRegressor
    
    Returns
    -------
    tuple
        (model, training_metrics)
    """
    model = DecisionTreeRegressor(
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42,
        **kwargs
    )
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    train_r2 = r2_score(y_train, y_pred_train)
    train_mae = mean_absolute_error(y_train, y_pred_train)
    
    metrics = {
        'train_rmse': train_rmse,
        'train_r2': train_r2,
        'train_mae': train_mae
    }
    
    return model, metrics


def train_random_forest(X_train: np.ndarray, y_train: np.ndarray,
                       n_estimators: int = 100,
                       max_depth: int = 10,
                       min_samples_split: int = 5,
                       **kwargs) -> Tuple[Any, Dict]:
    """
    Train a random forest regressor.
    
    Parameters
    ----------
    X_train : np.ndarray
        Training features
    y_train : np.ndarray
        Training target
    n_estimators : int
        Number of trees
    max_depth : int
        Maximum depth of trees
    min_samples_split : int
        Minimum samples required to split
    **kwargs
        Additional arguments for RandomForestRegressor
    
    Returns
    -------
    tuple
        (model, training_metrics)
    """
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42,
        n_jobs=-1,
        **kwargs
    )
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    train_r2 = r2_score(y_train, y_pred_train)
    train_mae = mean_absolute_error(y_train, y_pred_train)
    
    metrics = {
        'train_rmse': train_rmse,
        'train_r2': train_r2,
        'train_mae': train_mae
    }
    
    return model, metrics


def train_xgboost(X_train: np.ndarray, y_train: np.ndarray,
                 n_estimators: int = 100,
                 max_depth: int = 6,
                 learning_rate: float = 0.1,
                 **kwargs) -> Tuple[Any, Dict]:
    """
    Train an XGBoost regressor.
    
    Parameters
    ----------
    X_train : np.ndarray
        Training features
    y_train : np.ndarray
        Training target
    n_estimators : int
        Number of boosting rounds
    max_depth : int
        Maximum depth of trees
    learning_rate : float
        Learning rate
    **kwargs
        Additional arguments for XGBRegressor
    
    Returns
    -------
    tuple
        (model, training_metrics)
    
    Raises
    ------
    ImportError
        If XGBoost is not available
    """
    if not XGBOOST_AVAILABLE:
        raise ImportError(
            "XGBoost is not available. Please install it with: pip install xgboost\n"
            "If you're on macOS with Apple Silicon, try: pip install xgboost --upgrade"
        )
    
    model = XGBRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=learning_rate,
        random_state=42,
        **kwargs
    )
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    train_r2 = r2_score(y_train, y_pred_train)
    train_mae = mean_absolute_error(y_train, y_pred_train)
    
    metrics = {
        'train_rmse': train_rmse,
        'train_r2': train_r2,
        'train_mae': train_mae
    }
    
    return model, metrics


def evaluate_model(model: Any, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
    """
    Evaluate a trained model on test data.
    
    Parameters
    ----------
    model : Any
        Trained model
    X_test : np.ndarray
        Test features
    y_test : np.ndarray
        Test target
    
    Returns
    -------
    dict
        Dictionary with evaluation metrics
    """
    y_pred = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    # Calculate percentage errors
    mape = np.mean(np.abs((y_test - y_pred) / (y_test + 1e-8))) * 100
    
    metrics = {
        'rmse': rmse,
        'r2': r2,
        'mae': mae,
        'mape': mape,
        'mean_actual': np.mean(y_test),
        'mean_predicted': np.mean(y_pred)
    }
    
    return metrics


def compare_models(models_dict: Dict[str, Tuple[Any, Dict]],
                   X_test: np.ndarray, y_test: np.ndarray) -> pd.DataFrame:
    """
    Compare multiple models on test data.
    
    Parameters
    ----------
    models_dict : dict
        Dictionary with model names as keys and (model, train_metrics) tuples as values
    X_test : np.ndarray
        Test features
    y_test : np.ndarray
        Test target
    
    Returns
    -------
    pd.DataFrame
        Comparison dataframe with metrics for all models
    """
    results = []
    
    for model_name, (model, train_metrics) in models_dict.items():
        test_metrics = evaluate_model(model, X_test, y_test)
        
        results.append({
            'Model': model_name,
            'Train_RMSE': train_metrics['train_rmse'],
            'Train_R2': train_metrics['train_r2'],
            'Test_RMSE': test_metrics['rmse'],
            'Test_R2': test_metrics['r2'],
            'Test_MAE': test_metrics['mae'],
            'Test_MAPE': test_metrics['mape']
        })
    
    return pd.DataFrame(results)

