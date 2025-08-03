# weather_api/parser.py - Convert raw weather to garden insights
class GardenWeatherParser:
    """Transform raw weather data into gardening insights"""
    
    def parse_current_conditions(self, weather_data):
        """Extract garden-relevant info from OpenWeather response"""
        
        # Extract key data points
        main = weather_data['main']
        weather = weather_data['weather'][0]
        
        # Calculate garden conditions
        garden_data = {
            'temperature': main['temp'],
            'feels_like': main['feels_like'],
            'humidity': main['humidity'],
            'description': weather['description'],
            'city': weather_data['name'],
            
            # Garden-specific insights
            'frost_risk': self._check_frost_risk(main['temp']),
            'watering_needed': self._check_watering_need(main['humidity']),
            'planting_conditions': self._assess_planting_conditions(main['temp'], main['humidity'])
        }
        
        return garden_data
    
    def _check_frost_risk(self, temp):
        """Determine frost protection needs"""
        if temp <= 32:
            return "HIGH - Protect plants immediately!"
        elif temp <= 40:
            return "MODERATE - Monitor tonight"
        else:
            return "LOW - Plants are safe"
    
    def _check_watering_need(self, humidity):
        """Suggest watering based on humidity"""
        if humidity < 30:
            return "HIGH - Dry conditions, water deeply"
        elif humidity < 60:
            return "MODERATE - Check soil moisture"
        else:
            return "LOW - High humidity, reduce watering"
    
    def _assess_planting_conditions(self, temp, humidity):
        """Overall planting assessment"""
        if 60 <= temp <= 75 and 40 <= humidity <= 70:
            return "EXCELLENT - Perfect for planting!"
        elif 50 <= temp <= 80:
            return "GOOD - Suitable for most plants"
        else:
            return "POOR - Wait for better conditions"