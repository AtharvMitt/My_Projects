import requests
import datetime as dt

MY_LAT = 12.990654
MY_LONG = 77.702426

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#
# data = response.json()
# print(data)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Indian/Maldives"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset)
print(sunrise)

time_now = dt.datetime.now()
print(time_now.hour)