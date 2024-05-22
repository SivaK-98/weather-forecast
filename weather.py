import requests
import os


def get_weather(location, choice):
  weather_api = os.environ['WEATHER_API']
  if choice == "recent_history":
    url = f"https://api.tomorrow.io/v4/weather/history/recent?location={location}&apikey={weather_api}"
  elif choice == "realtime":
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={weather_api}"
  else:
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={weather_api}"

  headers = {"accept": "application/json"}
  response = requests.get(url, headers=headers)
  data = response.json()
  time = data["data"]["time"]
  result = data["data"]["values"]
  return (time, result)


location = "chennai"
choice = "realtime"
result = get_weather(location, choice)
print(result)
