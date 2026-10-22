import requests

def get_weather(city_name, api_key):
    # Base URL for OpenWeather API (using metric units for Celsius)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        # REST API integration via requests
        response = requests.get(url)
        response.raise_for_status()
        
        # JSON response parsing
        data = response.json()
        
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        
        # Clean CLI user display
        print(f"\n--- Weather in {city_name.title()} ---")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_desc.capitalize()}")
        print("-" * 35)
        
    except requests.exceptions.HTTPError as err:
        if response.status_code == 401:
            print("Error: Invalid API Key. Please check your OpenWeather API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city_name}' not found.")
        else:
            print(f"HTTP Error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("=== Live Weather App ===")
    
    # IMPORTANT: Replace the string below with your actual OpenWeather API key
    API_KEY = "87d967b09ead960dc5ab99a0b65cadad"

    
    if API_KEY == "YOUR_OPENWEATHER_API_KEY_HERE":
        print("Wait! You need to add your OpenWeather API key to the script.")
        print("Sign up at https://openweathermap.org/ to get a free key.")
        return
        
    while True:
        city = input("Enter a city name (or 'quit' to exit): ")
        if city.lower() == 'quit':
            print("Exiting Weather App. Goodbye!")
            break
            
        get_weather(city, API_KEY)

if __name__ == "__main__":
    main()