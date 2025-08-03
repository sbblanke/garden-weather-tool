import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WeatherClient:

    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            raise ValueError("OPENEWEATHER_API_KEY not found in .env file.")
        
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city):
        """Get current weather for a city - garden relevant data"""
        
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'imperial' # Fahrenheit for US gardeners
        }

    # Add this method to your WeatherClient class
    def get_weather_by_zip(self, zip_code, country_code="US"):
        """Get weather by ZIP code - more precise than city names"""
        url = f"{self.base_url}/weather"
        params = {
            'zip': f"{zip_code},{country_code}",
            'appid': self.api_key,
            'units': 'imperial',
        }
        
        try:
            response = requests.get(url, params=params)
            print(f"Status Code: {response.status_code}")  # Keep debugging for now
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise Exception("Invalid API key")
            elif response.status_code == 404:
                raise Exception(f"ZIP code '{zip_code}' not found")
            else:
                raise Exception(f"API error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")    

        #try:
            #response = requests.get(url, params=params)
            
            #if response.status_code == 200:
                #return response.json()
            #elif response.status_code == 401:
                #raise Exception("Invalid API key. Please check your .env file.")
            #elif response.status_code == 404:
                #raise Exception(f"City '{city}' not found. Please check the city name.")
            #else:
                #raise Exception(f"API error: {response.status_code}")
        
        #except requests.exceptions.RequestException as e:
            #raise Exception(f"Network error: {e}")

        try:
            # Make the HTTP request
            response = requests.get(url, params=params)
            
            # DEBUG: Let's see what we actually got
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
            
            # Check if request was successful
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise Exception("Invalid API key - check your .env file")
            elif response.status_code == 404:
                raise Exception(f"City '{city}' not found. Response: {response.text}")
            else:
                raise Exception(f"API error: {response.status_code}. Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        
if __name__ == "__main__":
    client = WeatherClient()
    weather = client.get_current_weather("Raleigh")
    print("Raw weather data:", weather)

    