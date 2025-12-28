"""
Application settings and configuration management.

Loads settings from environment variables and provides a centralized
configuration object.
"""

import os
import logging
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file if it exists
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)


logger = logging.getLogger(__name__)


class Config:
    """
    Configuration class for application settings.
    
    Loads settings from environment variables with sensible defaults.
    Never hardcode API keys or secrets - always use environment variables.
    """
    
    def __init__(self):
        """Initialize configuration from environment variables."""
        
        # API Configuration (load from environment)
        self.api_key: Optional[str] = os.getenv('API_KEY')
        self.api_secret: Optional[str] = os.getenv('API_SECRET')
        self.websocket_endpoint: str = os.getenv(
            'WEBSOCKET_ENDPOINT', 
            'wss://example.com/stream'  # Placeholder
        )
        
        # Data Configuration
        self.data_dir: Path = Path(os.getenv('DATA_DIR', './data'))
        self.cache_dir: Path = Path(os.getenv('CACHE_DIR', './cache'))
        
        # Backtesting Configuration
        self.initial_capital: float = float(os.getenv('INITIAL_CAPITAL', '100000'))
        self.commission: float = float(os.getenv('COMMISSION', '0.001'))
        self.slippage: float = float(os.getenv('SLIPPAGE', '0.001'))
        
        # Logging Configuration
        self.log_level: str = os.getenv('LOG_LEVEL', 'INFO')
        self.log_file: Optional[str] = os.getenv('LOG_FILE')
        
        # Market Data Configuration
        self.default_symbols: list[str] = self._parse_symbols(
            os.getenv('DEFAULT_SYMBOLS', 'AAPL,GOOGL,MSFT')
        )
        
        # Strategy Configuration
        self.strategy_name: str = os.getenv('STRATEGY_NAME', 'placeholder')
        self.risk_per_trade: float = float(os.getenv('RISK_PER_TRADE', '0.02'))
        
        # Feature Flags
        self.enable_live_trading: bool = os.getenv('ENABLE_LIVE_TRADING', 'false').lower() == 'true'
        self.enable_notifications: bool = os.getenv('ENABLE_NOTIFICATIONS', 'false').lower() == 'true'
        
        self._setup_logging()
        self._create_directories()
        
        logger.info("Configuration loaded successfully")
        if not self.api_key:
            logger.warning("API_KEY not set in environment variables")
    
    def _parse_symbols(self, symbols_str: str) -> list[str]:
        """Parse comma-separated symbols string into list."""
        return [s.strip().upper() for s in symbols_str.split(',') if s.strip()]
    
    def _setup_logging(self) -> None:
        """Configure logging based on settings."""
        log_level = getattr(logging, self.log_level.upper(), logging.INFO)
        
        handlers = [logging.StreamHandler()]
        if self.log_file:
            handlers.append(logging.FileHandler(self.log_file))
        
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=handlers
        )
    
    def _create_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def validate(self) -> bool:
        """
        Validate that required configuration is present.
        
        Returns:
            True if configuration is valid, False otherwise
        """
        errors = []
        
        if self.enable_live_trading and not self.api_key:
            errors.append("API_KEY required for live trading")
        
        if self.enable_live_trading and not self.api_secret:
            errors.append("API_SECRET required for live trading")
        
        if errors:
            for error in errors:
                logger.error(f"Configuration error: {error}")
            return False
        
        return True
    
    def __repr__(self) -> str:
        """String representation (hides sensitive data)."""
        return (
            f"Config("
            f"websocket_endpoint={self.websocket_endpoint}, "
            f"strategy={self.strategy_name}, "
            f"symbols={self.default_symbols}, "
            f"api_key={'***' if self.api_key else 'None'})"
        )


# Global configuration instance
config = Config()
