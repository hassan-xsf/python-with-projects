import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPENWEATHER_API = os.environ["OPENWEATHER_API"]

def getWeatherDetails(city):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API}")
        response.raise_for_status()
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return
        
        data = response.json()
        stringedResponse = f"\n\n\t>>> WEATHER REPORT <<<<\n\
            City: {data['name']}\n\
            Country: {data['sys']['country']}\n\
            Weather: {data['weather'][0]['main']}\n\
            Temperature: {data['main']['temp'] - 273:.2f}\t| Feels Like: {data['main']['feels_like'] - 273:.2f}\n\
            Min. Temperature: {data['main']['temp_min'] - 273:.2f}\t| Max. Temperature: {data['main']['temp_max'] - 273:.2f}\n\
            Humidity: {data['main']['humidity']}\n\
        "
        return stringedResponse

    except Exception as e:
        print(f"There was an error: {e}")

if __name__ == "__main__":
    while(True):
        city = input(">> Enter the city name to find it's weather: \n")
        if(len(city) < 1):
            print("Error: Invalid city name found, Please try again")
        else:
            weatherDetails = getWeatherDetails(city)
            print(weatherDetails)
        