# weather

# create an app that asks for input of city in the usa
# then display that cities weather report

API_KEY = "90b9a569fa1fcc107ef5413c2762b097"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

import requests

city = input('Please enter a city: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = 

