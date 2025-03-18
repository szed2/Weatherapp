import requests

def get_weather(city):
    api_key = "5b3e97517286490e95d52618242611"  # Replace with your WeatherAPI.com API key
    base_url = "http://api.weatherapi.com/v1/current.json?"
    complete_url = base_url + "key=" + api_key + "&q=" + city + "&aqi=no"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if "error" not in data:
        current = data["current"]
        location = data["location"]
        temperature = current["temp_c"]
        pressure = current["pressure_mb"]
        humidity = current["humidity"]
        description = current["condition"]["text"]
        
        print(f"Location: {location['name']}, {location['country']}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {description}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
print("Would you like to search for another place? (yes/no)")