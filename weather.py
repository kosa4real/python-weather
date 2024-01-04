from dotenv import load_dotenv
import os
from pprint import pprint
import requests


load_dotenv()


def get_current_weather(city="Kansas City"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metrics"
    
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")

    if not bool(city.strip()):
        city = "Kansas City"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)