import requests

api_key = "23875a6891a428de7c18b6a3d4814dfb"

city = input("Enter city name: ").strip()

if city == "":
    print("Please enter a valid city name.")

else:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
    response = requests.get(url)

    try:
        data = response.json()
    except ValueError:
        print("Failed to parse weather response. Please check your internet connection and API key.")
        data = None

    if not data or str(data.get("cod")) != "200":
        message = data.get("message") if data else None
        if message:
            print(f"Failed to find city {city}: {message}")
        else:
            print(f"City {city} not found. Please check the city name and try again.")
    else:
        main = data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        feels_like = main["feels_like"]

        weather_description = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")