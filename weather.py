import requests

def get_weather(location):
    """Get weather data for a location"""
    try:
        # Using Minneapolis coordinates
        lat = 44.9778
        lon = -93.2650
        
        print(f"Getting weather for Minneapolis (lat={lat}, lon={lon})")
        
        # Use Open-Meteo API (no API key required)
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,wind_direction_10m,rain,showers,snowfall&daily=weather_code,temperature_2m_max,temperature_2m_min&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
        
        print(f"Making request to: {url}")
        
        # Make the request with a timeout
        response = requests.get(url, timeout=10)
        
        print(f"Response status: {response.status_code}")
        
        # If successful, return the JSON data
        if response.status_code == 200:
            data = response.json()
            print("Successfully got weather data")
            return data
        else:
            print(f"API error: {response.status_code}")
            print(f"Response text: {response.text}")
            return None
            
    except Exception as e:
        print(f"Exception getting weather: {str(e)}")
        import traceback
        traceback.print_exc()
        return None