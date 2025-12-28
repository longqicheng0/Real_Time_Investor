"""
Example script demonstrating how to use the Real-Time Investor framework.

This shows the basic usage of each module without implementing actual strategies.
"""

import logging
from real_time_investor import (
    config,
    MarketDataStream,
    IndicatorCalculator,
    SignalGenerator,
    Backtester
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def example_live_data_stream():
    """Example: Set up a live market data stream."""
    logger.info("=== Live Data Stream Example ===")
    
    # Initialize the market data stream
    stream = MarketDataStream(
        api_endpoint=config.websocket_endpoint,
        symbols=['AAPL', 'GOOGL'],
        api_key=config.api_key
    )
    
    # Define a callback for incoming data
    def handle_market_data(message):
        logger.info(f"Received market data: {message}")
        # Process the data here
    
    # Register callback
    stream.on_message(handle_market_data)
    
    # Connect and start streaming (placeholder)
    stream.connect()
    logger.info("Stream ready (placeholder implementation)")
    stream.disconnect()


def example_indicators():
    """Example: Calculate technical indicators."""
    logger.info("=== Indicators Example ===")
    
    import pandas as pd
    
    # Create sample price data
    sample_prices = pd.Series([100, 102, 101, 103, 105, 104, 106])
    
    # Initialize calculator
    calc = IndicatorCalculator()
    
    # Calculate various indicators (placeholder)
    sma = calc.calculate_sma(sample_prices, period=5)
    ema = calc.calculate_ema(sample_prices, period=5)
    rsi = calc.calculate_rsi(sample_prices, period=14)
    
    logger.info("Indicators calculated (placeholder implementation)")


def example_signal_generation():
    """Example: Generate trading signals."""
    logger.info("=== Signal Generation Example ===")
    
    # Initialize signal generator
    generator = SignalGenerator(strategy_name="example_strategy")
    
    # Sample market data and indicators
    market_data = {
        'price': 150.50,
        'volume': 1000000,
        'timestamp': '2024-01-01T10:00:00'
    }
    
    indicators = {
        'sma_20': 148.00,
        'rsi': 65.0,
        'macd': 1.5
    }
    
    # Generate signal
    signal = generator.generate_signal(
        symbol='AAPL',
        market_data=market_data,
        indicators=indicators
    )
    
    logger.info(f"Generated signal: {signal}")


def example_backtesting():
    """Example: Run a backtest."""
    logger.info("=== Backtesting Example ===")
    
    # Initialize backtester
    backtester = Backtester(
        initial_capital=config.initial_capital,
        commission=config.commission,
        slippage=config.slippage
    )
    
    # In a real implementation, you would:
    # 1. Load historical data
    # 2. Define a strategy function
    # 3. Run the backtest
    # 4. Analyze results
    
    logger.info("Backtester initialized (placeholder implementation)")
    
    # Placeholder strategy function
    def placeholder_strategy(data, indicators):
        """Placeholder strategy - does not implement actual logic."""
        return None
    
    # Run backtest (placeholder)
    import pandas as pd
    results = backtester.run(
        data=pd.DataFrame(),
        strategy=placeholder_strategy
    )
    
    logger.info(f"Backtest results: {results}")


def main():
    """Run all examples."""
    logger.info("Starting Real-Time Investor Examples")
    logger.info(f"Configuration: {config}")
    
    # Validate configuration
    if not config.validate():
        logger.warning("Configuration validation failed - some features may not work")
    
    # Run examples
    example_live_data_stream()
    print()
    
    example_indicators()
    print()
    
    example_signal_generation()
    print()
    
    example_backtesting()
    print()
    
    logger.info("All examples completed")


if __name__ == "__main__":
    main()
