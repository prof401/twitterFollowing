import requests
import os

consumer_key        = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret     = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token        = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")

def check_weather(city):
    """
    This function takes a city name as an argument and returns the current weather in that city.

    Parameters:
    city (str): The name of the city to check the weather for

    Returns:
    str: The current weather in the specified city
    """
    try:
        # Make a request to the OpenWeatherMap API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
        response = requests.get(url)

        # Parse the response and extract the weather information
        data = response.json()
        weather = data["weather"][0]["description"]

        # Return the weather information
        return weather
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return "Unable to retrieve weather information"  # Return a default message in case of error

def check_current_weather():
        """
        This function makes an API call to OpenWeatherMap to get the current weather in London.

        Returns:
        str: The current weather in London
        """
    try:
        # Make the API call
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY")

        # Check if the response was successful
        if response.status_code != 200:
            raise Exception("Failed to get weather data")

        # Extract the weather information from the response
        weather_data = response.json()
        weather_description = weather_data["weather"][0]["description"]

        # Return the weather description
        return weather_description
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return "Failed to get weather data"