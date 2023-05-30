# lets build a web app that will take in a city name and return the weather
# Import the required modules
from flask import Flask, request
import requests
from azure.appconfiguration import AzureAppConfiguration
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Create the Flask app

app = Flask(__name__)

# Create the route for the home page
@app.route('/')
def home():
    return "Welcome to the Weather Forecast App!"

# Create the route for the weather page

@app.route('/weather')
def get_weather():
    city_name = request.args.get('city')
    
# Retrieve OpenWeatherMap API key from Azure Key Vault
    credential = DefaultAzureCredential()
    key_vault_url = 'https://VaishMudaliar.vault.azure.net'  # Replace with your Key Vault URL
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    api_key = secret_client.get_secret('OpenWeatherMapAPIKey').value
    
    # Construct url name with city name and api key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    # Make request to the api

    response = requests.get(url)
    data = response.json()

    # Check if response is successful

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        weather_text = f"Weather forecast for {city_name}:\n"
        weather_text += f"Description: {weather_description}\n"
        weather_text += f"Temperature: {temperature}°C\n"
        weather_text += f"Humidity: {humidity}%"

        return weather_text
# Print out error message if response is not successful
    return f"Error: {data['message']}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
