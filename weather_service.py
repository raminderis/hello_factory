```python
import requests
from typing import Optional, Dict, Any
from datetime import datetime


class WeatherService:
    """Service class to interact with OpenWeather API and process weather data."""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    def __init__(self, api_key: str):
        """
        Initialize the WeatherService with an API key.
        
        Args:
            api_key: OpenWeather API key
        """
        self.api_key = api_key
    
    def get_current_weather(self, city: str, units: str = "metric") -> Optional[Dict[str, Any]]:
        """
        Get current weather data for a specific city.
        
        Args:
            city: Name of the city
            units: Units of measurement (metric, imperial, standard)
        
        Returns:
            Dictionary containing weather data or None if request fails
        """
        endpoint = f"{self.BASE_URL}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": units
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def get_forecast(self, city: str, units: str = "metric", cnt: int = 5) -> Optional[Dict[str, Any]]:
        """
        Get weather forecast for a specific city.
        
        Args:
            city: Name of the city
            units: Units of measurement (metric, imperial, standard)
            cnt: Number of forecast timestamps to retrieve
        
        Returns:
            Dictionary containing forecast data or None if request fails
        """
        endpoint = f"{self.BASE_URL}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": units,
            "cnt": cnt
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return None
    
    def get_weather_by_coordinates(self, lat: float, lon: float, units: str = "metric") -> Optional[Dict[str, Any]]:
        """
        Get current weather data by geographic coordinates.
        
        Args:
            lat: Latitude
            lon: Longitude
            units: Units of measurement (metric, imperial, standard)
        
        Returns:
            Dictionary containing weather data or None if request fails
        """
        endpoint = f"{self.BASE_URL}/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": units
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data by coordinates: {e}")
            return None
    
    def process_weather_data(self, weather_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process raw weather data into a simplified format.
        
        Args:
            weather_data: Raw weather data from API
        
        Returns:
            Dictionary with processed weather information
        """
        if not weather_data:
            return {}
        
        processed = {
            "city": weather_data.get("name", "Unknown"),
            "country": weather_data.get("sys", {}).get("country", "Unknown"),
            "temperature": weather_data.get("main", {}).get("temp"),
            "feels_like": weather_data.get("main", {}).get("feels_like"),
            "temp_min": weather_data.get("main", {}).get("temp_min"),
            "temp_max": weather_data.get("main", {}).get("temp_max"),
            "pressure": weather_data.get("main", {}).get("pressure"),
            "humidity": weather_data.get("main", {}).get("humidity"),
            "description": weather_data.get("weather", [{}])[0].get("description", "N/A"),
            "weather_main": weather_data.get("weather", [{}])[0].get("main", "N/A"),
            "wind_speed": weather_data.get("wind", {}).get("speed"),
            "wind_direction": weather_data.get("wind", {}).get("deg"),
            "cloudiness": weather_data.get("clouds", {}).get("all"),
            "timestamp": weather_data.get("dt"),
            "sunrise": weather_data.get("sys", {}).get("sunrise"),
            "sunset": weather_data.get("sys", {}).get("sunset")
        }
        
        return processed
    
    def process_forecast_data(self, forecast_data: Dict[str, Any]) -> list[Dict[str, Any]]:
        """
        Process raw forecast data into a simplified format.
        
        Args:
            forecast_data: Raw forecast data from API
        
        Returns:
            List of dictionaries with processed forecast information
        """
        if not forecast_data or "list" not in forecast_data:
            return []
        
        processed_list = []
        
        for item in forecast_data.get("list", []):
            processed = {
                "timestamp": item.get("dt"),
                "datetime": datetime.fromtimestamp(item.get("dt", 0)).isoformat(),
                "temperature": item.get("main", {}).get("temp"),
                "feels_like": item.get("main", {}).get("feels_like"),
                "temp_min": item.get("main", {}).get("temp_min"),
                "temp_max": item.get("main", {}).get("temp_max"),
                "pressure": item.get("main", {}).get("pressure"),
                "humidity": item.get("main", {}).get("humidity"),
                "description": item.get("weather", [{}])[0].get("description", "N/A"),
                "weather_main": item.get("weather", [{}])[0].get("main", "N/A"),
                "wind_speed": item.get("wind", {}).get("speed"),
                "wind_direction": item.get("wind", {}).get("deg"),
                "cloudiness": item.get("clouds", {}).get("all"),
                "pop": item.get("pop", 0)
            }
            processed_list.append(processed)
        
        return processed_list
    
    def get_temperature_trend(self, forecast_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze temperature trends from forecast data.
        
        Args:
            forecast_data: Raw forecast data from API
        
        Returns:
            Dictionary with temperature trend analysis
        """
        if not forecast_data or "list" not in forecast_data:
            return {}
        
        temperatures = [item.get("main", {}).get("temp") for item in forecast_data.get("list", []) if item.get("main", {}).get("temp") is not None]
        
        if not temperatures:
            return {}
        
        return {
            "min_temperature": min(temperatures),
            "max_temperature": max(temperatures),
            "avg_temperature": sum(temperatures) / len(temperatures),
            "temperature_range": max(temperatures) - min(temperatures)
        }
```