"""Logging utilities for the project."""

import logging
import sys
from pathlib import Path
from src.utils.config import PROJECT_ROOT


def setup_logger(name: str = "insurance_analytics", log_level: str = "INFO") -> logging.Logger:
    """
    Set up a logger for the project.
    
    Parameters
    ----------
    name : str
        Logger name.
    log_level : str
        Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    
    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "analytics.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

