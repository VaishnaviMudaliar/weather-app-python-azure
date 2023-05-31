# build a weather cli in python using openweathermap api

import click
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("0526b523e212e6d1b780cb2edd273c55")

@click.group()
def main():
    pass

@main.command()
@click.argument('city')
def current(city):
    """Get current weather"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    print(f"Current weather in {city}:")
    print(f"Temperature: {data['main']['temp']}")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Wind speed: {data['wind']['speed']}")
    print(f"Wind direction: {data['wind']['deg']}")
    print(f"Clouds: {data['clouds']['all']}")
    print(f"Pressure: {data['main']['pressure']}")
    print(f"Humidity: {data['main']['humidity']}")
    print(f"Sunrise: {data['sys']['sunrise']}")
    print(f"Sunset: {data['sys']['sunset']}")
    print(f"Geo coords: [{data['coord']['lon']}, {data['coord']['lat']}]")

@main.command()
@click.argument('city')
def forecast(city):

    """Get forecast weather"""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    print(f"Weather forecast in {city}:")
    for i in range(0, len(data['list'])):
        print(f"Time: {data['list'][i]['dt_txt']}")
        print(f"Temperature: {data['list'][i]['main']['temp']}")
        print(f"Weather: {data['list'][i]['weather'][0]['description']}")
        print(f"Wind speed: {data['list'][i]['wind']['speed']}")
        print(f"Wind direction: {data['list'][i]['wind']['deg']}")
        print(f"Clouds: {data['list'][i]['clouds']['all']}")
        print(f"Pressure: {data['list'][i]['main']['pressure']}")
        print(f"Humidity: {data['list'][i]['main']['humidity']}")
        print(f"Geo coords: [{data['city']['coord']['lon']}, {data['city']['coord']['lat']}]")
        
if __name__ == "__main__":
    main()



# deploy it to azure functions through azure cli

# https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python

# https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python

#   1. Create a function app
#   2. Create a function in Azure
#   3. Deploy the function code to Azure
#   4. Test the function
#   5. Clean up resources







