# extracts data from web page and displays weather information for user selected city.


import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

# following conversion from degrees to cardinal points
# thanks to GitHub RobertSudwarts/deg_to_cardinal.py
# https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f
def degrees_to_cardinal(d):
    '''
    note: this is highly approximate...
    '''
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    pprint(weather_data)

    cardinal = degrees_to_cardinal(weather_data["wind"]["deg"])

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nCurrent temp {weather_data["main"]["temp"]}C')
    print(
        f'\nFeels like {weather_data["main"]["feels_like"]}C and {weather_data["weather"][0]["description"].title()}.'
    )
    print(f'\nWind from {weather_data["wind"]["deg"]} ({cardinal})'
          f' speed {weather_data["wind"]["speed"]}.\n')



if __name__ == "__main__":
    get_current_weather()