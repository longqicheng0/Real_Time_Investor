"""
Data Ingestion Module

Handles real-time market data streaming via WebSocket connections.
"""

from .websocket_client import MarketDataStream

__all__ = ["MarketDataStream"]
