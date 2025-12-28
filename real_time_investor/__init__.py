"""
Real-Time Investor: A modular framework for market data analysis and trading research.

This package provides tools for:
- Real-time market data ingestion via WebSocket
- Technical indicator computation
- Trading signal generation
- Backtesting strategies on historical data
"""

__version__ = "0.1.0"
__author__ = "Real Time Investor Team"

from .config import config
from .data_ingestion import MarketDataStream
from .indicators import IndicatorCalculator
from .strategy import SignalGenerator
from .backtesting import Backtester

__all__ = [
    "config",
    "MarketDataStream",
    "IndicatorCalculator",
    "SignalGenerator",
    "Backtester",
]
