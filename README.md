# Garden Weather Advisor 🌱

A Python-based weather analysis tool specifically designed for gardeners. Provides garden-specific insights like frost risk, watering recommendations, and optimal planting conditions using live weather data from OpenWeatherMap.

## 🌟 Features

### Weather Data Integration
- **Direct API Integration**: Connects to OpenWeatherMap API with professional authentication handling
- **Multiple Location Methods**: Support for city names, ZIP codes, and GPS coordinates
- **Real-time Data**: Live weather conditions updated from official sources
- **Location Precision**: ZIP-code level accuracy for microclimate considerations

### Garden-Specific Intelligence
- **Frost Risk Assessment**: Automatic alerts for plant protection needs
- **Watering Recommendations**: Smart watering advice based on humidity levels
- **Planting Condition Analysis**: Optimal timing assessments for garden activities
- **Temperature Monitoring**: Tracks conditions critical for plant health

### Professional Architecture
- **Modular Design**: Separate components for API client, data parsing, and user interface
- **Error Handling**: Comprehensive HTTP status code management and user-friendly error messages
- **Secure Configuration**: API key management with environment variables
- **Extensible Framework**: Ready for integration into larger gardening applications

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sbblanke/garden-weather-advisor.git
   cd garden-weather-advisor
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\Activate.ps1
   
   # Mac/Linux  
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key:**
   - Create a `.env` file in the project root
   - Add your OpenWeatherMap API key:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

5. **Verify installation:**
   ```bash
   python -c "from weather_api.client import WeatherClient; print('✅ Setup complete!')"
   ```

## 📖 Usage

### Basic Usage
```bash
python main.py
```

### Location Options
The advisor supports three location input methods:

1. **City Name**: `Clayton`, `Concord`, `Raleigh`
2. **ZIP Code**: `27520`, `28025`, `28083` (most precise)
3. **GPS Coordinates**: Exact latitude/longitude for your garden location

### Example Output
```
🌱 Garden Weather Advisor
========================================
📍 How would you like to specify your location?
1. City name (e.g., 'Clayton')
2. ZIP code (e.g., '27520')  
3. GPS coordinates (most precise)
Enter choice (1-3): 2
Enter ZIP code: 27520

🌤️  Getting weather for ZIP 27520...
🌱 Garden Weather Report for Clayton
--------------------------------------------------
🌡️  Temperature: 67.5°F (feels like 67.9°F)
💧 Humidity: 84%
☁️  Conditions: Clear Sky

🌱 GARDEN INSIGHTS:
❄️  Frost Risk: LOW - Plants are safe
💧 Watering: LOW - High humidity, reduce watering  
🌿 Planting Conditions: GOOD - Suitable for most plants
```

## 🏗️ Project Structure

```
garden_weather_advisor/
├── weather_api/              # Core weather functionality
│   ├── __init__.py
│   ├── client.py            # OpenWeatherMap API client
│   └── parser.py            # Garden-specific data processing
├── garden_logic/            # Future plant intelligence modules
├── config/                  # Configuration management
│   └── settings.py
├── data/                    # Weather data caching (future)
├── reports/                 # Generated garden reports (future)
├── main.py                  # Command-line interface
├── requirements.txt         # Python dependencies
├── .env                     # API keys (not committed)
├── .gitignore              # Git exclusions
└── README.md               # This file
```

## 🔧 Technical Details

### API Integration
- **Direct HTTP Requests**: Uses `requests` library for full control over API communication
- **Authentication**: Secure API key management with `python-dotenv`
- **Error Handling**: Comprehensive HTTP status code handling (401, 404, 500, etc.)
- **Response Processing**: Manual JSON parsing and validation

### Garden Intelligence Algorithms
- **Frost Risk**: Temperature-based assessment with three alert levels
- **Watering Logic**: Humidity-driven recommendations for water management
- **Planting Conditions**: Multi-factor analysis of temperature and humidity

### Security
- ✅ API keys stored in environment variables
- ✅ `.env` files excluded from version control
- ✅ No hardcoded credentials in source code

## 📊 API Usage & Costs

- **Provider**: OpenWeatherMap (official weather data)
- **Free Tier**: 1,000 API calls per day
- **Cost Efficiency**: Single API call per weather check
- **Rate Limiting**: Built-in error handling for usage limits

## 🌱 Garden Use Cases

### Daily Gardening Decisions
- **Morning Check**: Frost protection needs before sunrise
- **Watering Schedule**: Smart irrigation based on humidity forecasts
- **Planting Windows**: Optimal conditions for seed starting

### Seasonal Planning
- **Spring Setup**: Last frost date considerations
- **Summer Care**: Heat stress and watering optimization
- **Fall Preparation**: First frost protection planning

## 🚀 Future Enhancements (Planned)

### Phase 2: Enhanced Intelligence
- 🌤️ **5-Day Forecast**: Extended planning for planting and harvesting
- 📊 **Historical Comparisons**: Seasonal trend analysis
- 🌿 **Plant-Specific Alerts**: Customized advice for different crops
- 📅 **Seasonal Calendar**: Automated gardening task scheduling

### Phase 3: Professional Features  
- 💾 **Data Caching**: Offline capability and reduced API costs
- 📧 **Alert System**: Automated frost warnings and optimal condition notifications
- 📊 **Report