"""
Utility functions and helpers.

Common utility functions used across the application.
"""

import logging
import re
from typing import Any, Optional
from datetime import datetime
import pandas as pd


logger = logging.getLogger(__name__)


def validate_symbol(symbol: str) -> bool:
    """
    Validate that a symbol string is in the correct format.
    
    Args:
        symbol: Stock/asset symbol to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not symbol or not isinstance(symbol, str):
        return False
    
    # Basic validation: alphanumeric, uppercase, 1-5 characters
    # Adjust pattern based on actual requirements
    pattern = r'^[A-Z]{1,5}$'
    is_valid = bool(re.match(pattern, symbol.upper()))
    
    if not is_valid:
        logger.warning(f"Invalid symbol format: {symbol}")
    
    return is_valid


def format_timestamp(timestamp: Any) -> str:
    """
    Format a timestamp into a standardized string format.
    
    Args:
        timestamp: Timestamp (datetime, pd.Timestamp, or string)
        
    Returns:
        Formatted timestamp string (ISO 8601)
    """
    if isinstance(timestamp, str):
        try:
            timestamp = pd.to_datetime(timestamp)
        except Exception as e:
            logger.error(f"Failed to parse timestamp: {e}")
            return ""
    
    if isinstance(timestamp, (datetime, pd.Timestamp)):
        return timestamp.isoformat()
    
    logger.warning(f"Unsupported timestamp type: {type(timestamp)}")
    return ""


def calculate_returns(prices: pd.Series) -> pd.Series:
    """
    Calculate simple returns from price series.
    
    Args:
        prices: Series of prices
        
    Returns:
        Series of returns
    """
    if len(prices) < 2:
        return pd.Series(dtype=float)
    
    returns = prices.pct_change()
    return returns


def calculate_log_returns(prices: pd.Series) -> pd.Series:
    """
    Calculate logarithmic returns from price series.
    
    Args:
        prices: Series of prices
        
    Returns:
        Series of log returns
    """
    import numpy as np
    
    if len(prices) < 2:
        return pd.Series(dtype=float)
    
    log_returns = np.log(prices / prices.shift(1))
    return log_returns


def resample_ohlc(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    """
    Resample OHLC data to a different timeframe.
    
    Args:
        df: DataFrame with datetime index and OHLC columns
        timeframe: Target timeframe (e.g., '5T' for 5 minutes, '1H' for 1 hour)
        
    Returns:
        Resampled DataFrame
    """
    if not isinstance(df.index, pd.DatetimeIndex):
        logger.error("DataFrame must have DatetimeIndex for resampling")
        return df
    
    resampled = df.resample(timeframe).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })
    
    return resampled.dropna()


def parse_timeframe(timeframe: str) -> int:
    """
    Parse timeframe string into seconds.
    
    Args:
        timeframe: Timeframe string (e.g., '1m', '5m', '1h', '1d')
        
    Returns:
        Number of seconds
    """
    units = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400
    }
    
    pattern = r'^(\d+)([smhd])$'
    match = re.match(pattern, timeframe.lower())
    
    if not match:
        logger.error(f"Invalid timeframe format: {timeframe}")
        return 0
    
    value, unit = match.groups()
    return int(value) * units[unit]


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, returning a default value if denominator is zero.
    
    Args:
        numerator: Numerator
        denominator: Denominator
        default: Default value to return if division fails
        
    Returns:
        Result of division or default value
    """
    if denominator == 0 or pd.isna(denominator):
        return default
    
    try:
        return numerator / denominator
    except (TypeError, ValueError) as e:
        logger.warning(f"Division failed: {e}")
        return default
