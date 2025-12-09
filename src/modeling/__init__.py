"""Statistical and Machine Learning modeling modules."""

from .data_preparation import (
    prepare_claim_severity_data,
    prepare_premium_prediction_data,
    encode_categorical_features,
    create_claim_probability_feature
)

from .models import (
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    evaluate_model,
    compare_models
)

# Import XGBoost only if available
try:
    from .models import train_xgboost
except ImportError:
    train_xgboost = None

from .interpretability import (
    get_feature_importance,
    plot_feature_importance,
    explain_with_shap,
    plot_shap_summary,
    explain_with_lime
)

__all__ = [
    # Data preparation
    'prepare_claim_severity_data',
    'prepare_premium_prediction_data',
    'encode_categorical_features',
    'create_claim_probability_feature',
    # Models
    'train_linear_regression',
    'train_decision_tree',
    'train_random_forest',
    'train_xgboost',
    'evaluate_model',
    'compare_models',
    # Interpretability
    'get_feature_importance',
    'plot_feature_importance',
    'explain_with_shap',
    'plot_shap_summary',
    'explain_with_lime'
]
