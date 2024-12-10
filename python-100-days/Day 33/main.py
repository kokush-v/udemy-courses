import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.json())

parameters = {
    'lat': 48.618252,
    'lng': 22.289391,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)