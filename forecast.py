# help me write a cli that will take in a location and return the weather
# use openweather api
# api key is 0526b523e212e6d1b780cb2edd273c55

import requests
import json
import sys

def get_weather_forecast(city_name):

    # Construct url name with city name and api key
    api_key = "0526b523e212e6d1b780cb2edd273c55"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    # Make request to the api
    try:
        response = requests.get(url)
        data = response.json()

        # Check if response is successful
        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            # Print out the weather forecast
            print(f"weather forecast of {city_name}:")
            print(f"Description : {weather_description}")
            print(f"Temperature : {temperature} degree celcius")
            print(f"Humidity : {humidity} %")
        
        # Print out error message if response is not successful
        else:
            print(f"Error : {data['message']}")
    except requests.exceptions.RequestException as e:
         # Print out error message if response is not successful

        print(f"Error : {str(e)}")
        sys.exit(1)

     
      # Print out the weather forecast
      
if __name__ == "__main__":
        
        city_name = input('Please enter a city name: ')
    
        print(get_weather_forecast(city_name))

# how to upload the code to github
# git init  
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin
# git push -u origin main
# git push origin main
# git pull origin main
# git status
# git log
# git checkout -b "branch name"
# git checkout "branch name"
# git merge "branch name"
# git branch -d "branch name"
# git branch -D "branch name"
# git push origin --delete "branch name"
# git push origin "branch name"
# git push origin main
# git push origin --delete "branch name"
# git push origin main
# git push origin main
# git push origin main






