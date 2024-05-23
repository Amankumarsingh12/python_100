import requests
from datetime import datetime
import smtplib


MY_LAT = 28.565602 # Your latitude
MY_LONG = 77.321239 # Your longitude
my_email = "aksinghn97@gmail.com"
passWord = "bvmg vzku npsz mtpg"

def is_night_my_pos():
    parameters = {

        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset =  int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    

if is_iss_overhead() and is_night_my_pos():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=passWord)

    connection.sendmail(from_addr=my_email, to_addrs="amansinghas1536610@gmail.com", msg="Subject:hello\n\nhi ji")
    connection.close()
    