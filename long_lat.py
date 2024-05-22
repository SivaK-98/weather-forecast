import requests
import os
from requests.structures import CaseInsensitiveDict

geo_api = os.environ['geo_location']
address = "Puducherry"


def get_location(address, geo_api):
  url = f"https://api.geoapify.com/v1/geocode/search?text={address}&apiKey={geo_api}"

  headers = CaseInsensitiveDict()
  headers["Accept"] = "application/json"

  resp = requests.get(url, headers=headers)
  data = resp.json()
  properties = data["features"][0]["properties"]
  latitude = properties["lat"]
  longitude = properties["lon"]
  return [latitude, longitude]



