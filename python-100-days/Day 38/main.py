import requests

NUTRITIONIX_APP_ID = "e3948a2e"
NUTRITIONIX_APP_KEY = "1adc441cc5fc77840a65594e171fe003"
SHEETY_API_KEY = "eeb125472f6554fd09efd7ac73b77480"

sheety_url = "https://api.sheety.co"
nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': "e3948a2e",
    'x-app-key': "1adc441cc5fc77840a65594e171fe003"
}
body = {
    "query": input('What have you done today? ')
}

response = requests.post(url=nutritionix_url, headers=headers, json=body)
response.raise_for_status()

exercises = response.json()["exercises"]

# print(exercises)
data_to_write = [{"exersice": exercise["name"], "duration": exercise["duration_min"], "calories": exercise["nf_calories"]} for exercise in exercises]
# print(data_to_write)

full_url = f"{sheety_url}/{SHEETY_API_KEY}/pythonLearning/page1"

for data in data_to_write:
    body = {
        "page1": data
    }
    response = requests.post(url=full_url, json=body)
    response.raise_for_status()
    print(f"Exersice {data["exersice"]} noted")


