import requests
import smtplib
from datetime import datetime as dt

OWM_api = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = input("Go sign to OpenWeatherMap to get an API and enter it here : ")

MY_LATITUDE = float(input("Enter your location's Latitude : "))
MY_LONGITUDE = float(input("Enter your location's Longitude : "))

MY_EMAIL = input("Enter your Email Address : ")
MY_PASSWD = input("Enter your email's Applications' Password : ")

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY
}

response = requests.get(url=OWM_api, params=parameters)
response.raise_for_status()

current_time = dt.now().hour

for n in range(12):
    weather_status_code = response.json()["hourly"][n]["weather"][0]["id"]
    if weather_status_code < 700:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=f"{MY_EMAIL}",
                            msg="subject: Rain Alert :)\n\nToday is a rainy day, Don't forget your Umbrella.")




