"""Model interpretability using SHAP and feature importance."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Any, List, Optional
import warnings

try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False
    warnings.warn("SHAP not available. Install with: pip install shap")

try:
    import lime
    from lime.lime_tabular import LimeTabularExplainer
    LIME_AVAILABLE = True
except ImportError:
    LIME_AVAILABLE = False
    warnings.warn("LIME not available. Install with: pip install lime")

warnings.filterwarnings('ignore')


def get_feature_importance(model: Any, feature_names: List[str],
                          model_type: str = 'auto') -> pd.DataFrame:
    """
    Get feature importance from a model.
    
    Parameters
    ----------
    model : Any
        Trained model
    feature_names : list
        List of feature names
    model_type : str
        Type of model ('tree', 'linear', 'auto')
    
    Returns
    -------
    pd.DataFrame
        Dataframe with feature names and importance scores
    """
    if model_type == 'auto':
        # Detect model type
        if hasattr(model, 'feature_importances_'):
            model_type = 'tree'
        elif hasattr(model, 'coef_'):
            model_type = 'linear'
        else:
            raise ValueError("Cannot determine model type")
    
    if model_type == 'tree':
        importances = model.feature_importances_
    elif model_type == 'linear':
        # Use absolute coefficients for linear models
        importances = np.abs(model.coef_)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    
    # Create dataframe
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    return importance_df


def plot_feature_importance(importance_df: pd.DataFrame,
                           top_n: int = 10,
                           title: str = "Top Feature Importance",
                           save_path: Optional[str] = None):
    """
    Plot feature importance.
    
    Parameters
    ----------
    importance_df : pd.DataFrame
        Feature importance dataframe
    top_n : int
        Number of top features to plot
    title : str
        Plot title
    save_path : str, optional
        Path to save the plot
    """
    top_features = importance_df.head(top_n)
    
    plt.figure(figsize=(10, 8))
    sns.barplot(data=top_features, y='feature', x='importance', palette='viridis')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Importance', fontsize=12)
    plt.ylabel('Feature', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def explain_with_shap(model: Any, X_sample: np.ndarray,
                     feature_names: List[str],
                     max_evals: int = 100) -> Optional[Any]:
    """
    Generate SHAP explanations for model predictions.
    
    Parameters
    ----------
    model : Any
        Trained model
    X_sample : np.ndarray
        Sample data for explanation
    feature_names : list
        List of feature names
    max_evals : int
        Maximum evaluations for SHAP (for TreeExplainer, can be higher)
    
    Returns
    -------
    shap.Explainer or None
        SHAP explainer object
    """
    if not SHAP_AVAILABLE:
        print("SHAP is not available. Install with: pip install shap")
        return None
    
    try:
        # Use TreeExplainer for tree-based models
        if hasattr(model, 'tree_') or hasattr(model, 'get_booster'):
            explainer = shap.TreeExplainer(model)
        else:
            # Use KernelExplainer for other models
            explainer = shap.KernelExplainer(model.predict, X_sample[:100])
        
        shap_values = explainer.shap_values(X_sample[:max_evals])
        
        return {
            'explainer': explainer,
            'shap_values': shap_values,
            'feature_names': feature_names
        }
    except Exception as e:
        print(f"Error generating SHAP explanations: {e}")
        return None


def plot_shap_summary(shap_result: dict, save_path: Optional[str] = None):
    """
    Plot SHAP summary plot.
    
    Parameters
    ----------
    shap_result : dict
        Result from explain_with_shap
    save_path : str, optional
        Path to save the plot
    """
    if not SHAP_AVAILABLE or shap_result is None:
        print("SHAP results not available")
        return
    
    try:
        plt.figure(figsize=(12, 8))
        shap.summary_plot(
            shap_result['shap_values'],
            feature_names=shap_result['feature_names'],
            show=False
        )
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    except Exception as e:
        print(f"Error plotting SHAP summary: {e}")


def explain_with_lime(model: Any, X_sample: np.ndarray,
                     feature_names: List[str],
                     instance_idx: int = 0) -> Optional[dict]:
    """
    Generate LIME explanation for a single instance.
    
    Parameters
    ----------
    model : Any
        Trained model
    X_sample : np.ndarray
        Sample data
    feature_names : list
        List of feature names
    instance_idx : int
        Index of instance to explain
    
    Returns
    -------
    dict or None
        LIME explanation result
    """
    if not LIME_AVAILABLE:
        print("LIME is not available. Install with: pip install lime")
        return None
    
    try:
        explainer = LimeTabularExplainer(
            X_sample,
            feature_names=feature_names,
            mode='regression'
        )
        
        explanation = explainer.explain_instance(
            X_sample[instance_idx],
            model.predict,
            num_features=10
        )
        
        return {
            'explainer': explainer,
            'explanation': explanation,
            'instance_idx': instance_idx
        }
    except Exception as e:
        print(f"Error generating LIME explanation: {e}")
        return None

