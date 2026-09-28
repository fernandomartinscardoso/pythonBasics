import smtplib
import requests
from datetime import datetime

# Creating a function to send email
def send_email(receiver_email, receiver_msg):
    my_email = "<your_email>@gmail.com"   # Replace with your email address
    my_password = "<your_app_password>"   # Replace with your app password (not your regular email password)

    with smtplib.SMTP("smtp.gmail.com") as connection: # Change the SMTP server if using a different email provider
        connection.starttls() # start TLS encryption for security
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{receiver_email}",
            msg=f"Subject:'Look up for ISS!'\n\n{receiver_msg}."
    )

def is_iss_overhead(my_lat, my_long):
    global iss_position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    is_iss_overhead = (my_lat - 5 <= iss_latitude <= my_lat + 5) and (my_long - 5 <= iss_longitude <= my_long + 5)
    return is_iss_overhead

def is_dark(my_lat, my_long):
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False