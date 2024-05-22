import requests
import os


def get_weather(location, choice):
    weather_api = "YFjyDQulK1fIpgqZokNXGa6PdUfqVKHM"
    print(weather_api)
    if choice == "recent_history":
        url = f"https://api.tomorrow.io/v4/weather/history/recent?location={location}&apikey={weather_api}"
    elif choice == "realtime":
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={weather_api}"
    else:
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={weather_api}"

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    time = data["data"]["time"]
    result = data["data"]["values"]
    send = (time,result)
    return send


