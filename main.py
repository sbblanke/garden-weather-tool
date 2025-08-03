# main.py - Garden Weather Advisor
from weather_api.client import WeatherClient
from weather_api.parser import GardenWeatherParser

def get_location_input():
    """Get user's preferred location method"""
    print("\n📍 How would you like to specify your location?")
    print("1. City name (e.g., 'Concord')")
    print("2. ZIP code (e.g., '28025')")  # Concord, NC ZIP
    print("3. GPS coordinates (most precise)")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "2":
        zip_code = input("Enter ZIP code: ").strip()
        return "zip", zip_code
    elif choice == "3":
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
        return "coords", (lat, lon)
    else:
        city = input("Enter city name: ").strip()
        return "city", city

def main():
    print("🌱 Garden Weather Advisor")
    print("=" * 40)
    
    try:
        # Get location preference
        location_type, location_data = get_location_input()
        
        # Get weather based on location type
        client = WeatherClient()
        
        if location_type == "zip":
            print(f"\n🌤️  Getting weather for ZIP {location_data}...")
            raw_weather = client.get_weather_by_zip(location_data)
        elif location_type == "coords":
            lat, lon = location_data
            print(f"\n🌤️  Getting weather for coordinates {lat}, {lon}...")
            raw_weather = client.get_weather_by_coordinates(lat, lon)
        else:
            print(f"\n🌤️  Getting weather for {location_data}...")
            raw_weather = client.get_current_weather(location_data)
        
        # Parse for garden insights
        parser = GardenWeatherParser()
        garden_weather = parser.parse_current_conditions(raw_weather)
        
        # Display garden-specific insights
        print(f"\n🌱 Garden Weather Report for {garden_weather['city']}")
        print("-" * 50)
        print(f"🌡️  Temperature: {garden_weather['temperature']:.1f}°F (feels like {garden_weather['feels_like']:.1f}°F)")
        print(f"💧 Humidity: {garden_weather['humidity']}%")
        print(f"☁️  Conditions: {garden_weather['description'].title()}")
        
        print(f"\n🌱 GARDEN INSIGHTS:")
        print(f"❄️  Frost Risk: {garden_weather['frost_risk']}")
        print(f"💧 Watering: {garden_weather['watering_needed']}")
        print(f"🌿 Planting Conditions: {garden_weather['planting_conditions']}")
        
        # Show raw data for learning
        print(f"\n📊 Raw API Response Preview:")
        print(f"API returned {len(raw_weather)} data fields")
        print(f"Available data: {list(raw_weather.keys())[:5]}...")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()