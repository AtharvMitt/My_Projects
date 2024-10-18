import requests
from twilio.rest import Client

api_key = "9d3d8850b93537cb3c629d3ef3c6dac3"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC54ce041a162d19e1e21109885b2827ee"
auth_token = "2c7f0aa12a27b00c3a99a1a74e0cf931"

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_="+12564641869",
        to="+919412117773"
    )
    print(message.status)
