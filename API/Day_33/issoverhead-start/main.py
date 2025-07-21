import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = ''
MY_PASSWORD = ''

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #hour of sunrise
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) #hour of sunset

time_now = datetime.now()
hour = time_now.hour


while sunrise < hour or hour > sunset: # and it is currently dark
    time.sleep(60) # BONUS: run the code every 60 seconds.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5: #Your position is within +5 or -5 degrees of the ISS position.
        # Then send me an email to tell me to look up.
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='email@email.com',
                            msg='Subject: Solar\n\nLook out the window')


