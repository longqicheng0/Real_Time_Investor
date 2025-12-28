# Real-Time Investor

A modular Python framework for real-time market data analysis and trading research. This project provides a clean, extensible architecture for building trading systems with separate modules for data ingestion, technical analysis, signal generation, and backtesting.

## ⚠️ Important Notes

- **This is a skeleton/framework only** - No actual trading strategies or predictions are implemented
- **Never commit API keys or secrets** - Use environment variables via `.env` file
- **For research and educational purposes** - Not production-ready trading software

## 🏗️ Project Structure

```
real_time_investor/
├── real_time_investor/          # Main package
│   ├── __init__.py             # Package initialization
│   ├── data_ingestion/         # Real-time data streaming
│   │   ├── __init__.py
│   │   └── websocket_client.py # WebSocket-based market data client
│   ├── indicators/             # Technical indicator computation
│   │   ├── __init__.py
│   │   └── calculator.py       # Indicator calculation engine
│   ├── strategy/               # Signal generation
│   │   ├── __init__.py
│   │   └── signal_generator.py # Trading signal generator (placeholder)
│   ├── backtesting/            # Offline backtesting
│   │   ├── __init__.py
│   │   └── engine.py           # Backtesting engine
│   ├── config/                 # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py         # Settings from environment variables
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       └── helpers.py          # Common helper functions
├── examples/                   # Example scripts
│   └── basic_usage.py         # Basic usage examples
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore file (includes .env)
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup configuration
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/longqicheng0/Real_Time_Investor.git
   cd Real_Time_Investor
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual configuration (never commit this file!)
   ```

5. **Install the package in development mode:**
   ```bash
   pip install -e .
   ```

## 📝 Configuration

Configure the application by editing the `.env` file. Key settings include:

- **API_KEY / API_SECRET**: Your market data provider credentials
- **WEBSOCKET_ENDPOINT**: WebSocket URL for real-time data
- **DEFAULT_SYMBOLS**: Comma-separated list of symbols to track
- **INITIAL_CAPITAL**: Starting capital for backtesting
- **COMMISSION / SLIPPAGE**: Trading costs for backtesting

See `.env.example` for all available options.

## 💡 Usage Examples

### Basic Usage

Run the example script to see all modules in action:

```bash
python examples/basic_usage.py
```

### Using Individual Modules

#### 1. Real-Time Data Ingestion

```python
from real_time_investor import MarketDataStream

# Initialize the data stream
stream = MarketDataStream(
    api_endpoint="wss://example.com/stream",
    symbols=["AAPL", "GOOGL"],
    api_key="your_api_key"
)

# Define a callback for incoming data
def handle_data(message):
    print(f"Received: {message}")

stream.on_message(handle_data)
stream.connect()
stream.start()
```

#### 2. Technical Indicators

```python
from real_time_investor import IndicatorCalculator
import pandas as pd

calc = IndicatorCalculator()

# Calculate indicators on price data
prices = pd.Series([100, 102, 101, 103, 105])
sma = calc.calculate_sma(prices, period=3)
rsi = calc.calculate_rsi(prices, period=14)
macd = calc.calculate_macd(prices)
```

#### 3. Signal Generation

```python
from real_time_investor import SignalGenerator

generator = SignalGenerator(strategy_name="my_strategy")

# Generate signals based on market data and indicators
signal = generator.generate_signal(
    symbol="AAPL",
    market_data={"price": 150.00, "volume": 1000000},
    indicators={"sma_20": 148.00, "rsi": 65}
)

print(signal)
```

#### 4. Backtesting

```python
from real_time_investor import Backtester
import pandas as pd

backtester = Backtester(
    initial_capital=100000,
    commission=0.001,
    slippage=0.001
)

# Define your strategy function
def my_strategy(data, indicators):
    # Strategy logic here
    pass

# Run backtest
results = backtester.run(
    data=historical_data,
    strategy=my_strategy
)

print(results)
```

## 🔧 Module Details

### Data Ingestion (`data_ingestion/`)

Handles real-time market data streaming via WebSocket connections. Placeholder implementation includes:
- Connection management
- Symbol subscription
- Callback-based message handling
- Error handling and reconnection (to be implemented)

### Indicators (`indicators/`)

Computes technical indicators and features from market data:
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Volume Profile
- Batch calculation support

### Strategy (`strategy/`)

Generates trading signals (placeholder only - no actual strategies implemented):
- Signal generation framework
- Position sizing calculations
- Signal history tracking
- Confidence scoring

### Backtesting (`backtesting/`)

Offline backtesting engine for strategy evaluation:
- Historical data loading
- Trade simulation with commission and slippage
- Portfolio tracking
- Performance metrics calculation
- Trade history recording

### Configuration (`config/`)

Centralized configuration management:
- Environment variable loading
- Default settings
- Validation
- Logging configuration

### Utilities (`utils/`)

Common utility functions:
- Symbol validation
- Timestamp formatting
- Return calculations
- Data resampling
- Safe mathematical operations

## 🔐 Security Best Practices

1. **Never commit API keys or secrets** to version control
2. Always use environment variables for sensitive data
3. The `.env` file is already in `.gitignore`
4. Use `.env.example` as a template (without real credentials)
5. Rotate API keys regularly
6. Use read-only API keys when possible

## 🛠️ Development

### Adding New Features

1. Keep modules separate and focused
2. Follow the existing code structure
3. Add placeholder implementations for complex logic
4. Document your code with docstrings
5. Update this README when adding major features

### Testing

To add tests, create a `tests/` directory and use pytest:

```bash
pip install pytest pytest-cov
pytest tests/
```

### Code Style

Consider using code formatters and linters:

```bash
pip install black flake8 mypy
black real_time_investor/
flake8 real_time_investor/
mypy real_time_investor/
```

## 📚 Future Enhancements

This is a skeleton framework. Potential enhancements include:

- [ ] Implement actual WebSocket connections to real data providers
- [ ] Add more technical indicators (Fibonacci, ATR, Stochastic, etc.)
- [ ] Integrate machine learning for signal generation
- [ ] Add real-time visualization dashboard
- [ ] Implement risk management modules
- [ ] Add portfolio optimization
- [ ] Create comprehensive test suite
- [ ] Add logging and monitoring
- [ ] Implement paper trading mode
- [ ] Add database integration for data persistence

## 📖 Resources

- [WebSocket Protocol](https://websocket.org/)
- [Technical Analysis Library](https://technical-analysis-library-in-python.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Quantitative Trading Resources](https://www.quantstart.com/)

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! This is an educational project meant to provide a clean starting point for trading system development.

## ⚠️ Disclaimer

This software is for educational and research purposes only. It does not constitute financial advice. Trading stocks and other financial instruments involves risk. Always do your own research and consult with financial professionals before making investment decisions.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.
