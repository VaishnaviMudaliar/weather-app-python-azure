from configparser import ConfigParser
import argparse
import sys
from urllib import  error, parse,request
import json
import style
 


# concatenate the user input into a valid URL that you’ll use to send API requests to OpenWeather’s API


BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

# Weather Condition Codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)




def _get_api_key():
    
    # Fetch the API key from your configuration file.
    

    """Fetch the API key from your configuration file.


    Expects a configuration file named "secrets.ini" with structure:


        [openweather]

        api_key=<YOUR-OPENWEATHER-API-KEY>

    """

    config = ConfigParser()

    config.read("secrets.ini")

    return config["openweather"]["api_key"]

# write a command-line input parser that takes user-provided information for a city and an optional parameter about what temperature scale to use (Celsius or Fahrenheit). If the user doesn't provide a temperature scale, default to Celsius.





def read_user_cli_args():

    """Handles the CLI user interactions.


    Returns:

        argparse.Namespace: Populated namespace object

    """


    parser = argparse.ArgumentParser(

        description="gets weather and temperature information for a city"

    )
    
    # add two arguments to the parser that you created before
    parser.add_argument(

        "city", nargs="+", type=str, help="enter the city name"

    )

    parser.add_argument(

        "-i",

        "--imperial",

        action="store_true",

        help="display the temperature in imperial units",

    )

    return parser.parse_args()

def build_weather_query(city_input, imperial=False):

    """Builds the URL for an API request to OpenWeather's weather API.


    Args:

        city_input (List[str]): Name of a city as collected by argparse

        imperial (bool): Whether or not to use imperial units for temperature


    Returns:

        str: URL formatted for a call to OpenWeather's city name endpoint

    """

    api_key = _get_api_key()

    city_name = " ".join(city_input)

    url_encoded_city_name = parse.quote_plus(city_name)

    units = "imperial" if imperial else "metric"

    url = (

        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"

        f"&units={units}&appid={api_key}"

    )

    return url


def get_weather_data(query_url):

    """Make an API request to a URL and returns the data as a Python object.


    Args:

        query_url (str): URL formatted for OpenWeather's city name endpoint


    Returns:

        dict: Weather information for a specific city

    """


    try:

        response = request.urlopen(query_url)

    except error.HTTPError as http_error:

        if http_error.code == 401:  # 401 - Unauthorized

            sys.exit("Access denied. Check your API key.")

        elif http_error.code == 404:  # 404 - Not Found

            sys.exit("Can't find weather data for this city.")

        else:

            sys.exit(f"Something went wrong... ({http_error.code})")

    data = response.read()

    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response.")
        
        
def _select_weather_display_params(weather_id):

    if weather_id in THUNDERSTORM:

        display_params = ("💥", style.RED)

    elif weather_id in DRIZZLE:

        display_params = ("💧", style.CYAN)

    elif weather_id in RAIN:

        display_params = ("💦", style.BLUE)

    elif weather_id in SNOW:

        display_params = ("⛄️", style.WHITE)

    elif weather_id in ATMOSPHERE:

        display_params = ("🌀", style.BLUE)

    elif weather_id in CLEAR:

        display_params = ("🔆", style.YELLOW)

    elif weather_id in CLOUDY:

        display_params = ("💨", style.WHITE)

    else:  # In case the API adds new weather codes

        display_params = ("🌈", style.RESET)

    return display_params






def display_weather_info(weather_data, imperial=False):

    """Prints formatted weather information about a city.


    Args:

        weather_data (dict): API response from OpenWeather by city name

        imperial (bool): Whether or not to use imperial units for temperature


    More information at https://openweathermap.org/current#name

    """

    city = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    weather_id = weather_data["weather"][0]["id"]
    temperature = weather_data["main"]["temp"]


    style.change_color(style.REVERSE)
    print(f"{city:^{style.PADDING}}", end="")
    style.change_color(style.RESET)

    color = _select_weather_display_params(weather_id)

    style.change_color(color)
    print(
        f"\t{weather_description.capitalize():^{style.PADDING}}",
        end=" ",
    )
    style.change_color(style.RESET)

    print(f"({temperature}°{'F' if imperial else 'C'})")




if __name__ == "__main__":

    
    #  capture the returned value of read_user_cli_args() in the user_args variable and added a call to print() in order to display the user-input values back to the console
    user_args = read_user_cli_args()
    #print(user_args.city, user_args.imperial)
    query_url = build_weather_query(user_args.city, user_args.imperial)
    weather_data = get_weather_data(query_url)
    display_weather_info(weather_data, user_args.imperial)
       
   
# Run the program with the following command:
# python weather.py "New York" -i
# python weather.py "New York" --imperial
# python weather.py "New York"
# python weather.py "New York" -i
# deploy the app to azure function
# https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python
# https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python
# https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#environment-variables
# https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure

# align current branch with master




