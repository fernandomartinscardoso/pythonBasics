# 100 Days of Python
# Day 33 - Application Programming Interfaces
# ISS Overhead API

'''
This program checks if the International Space Station (ISS) is currently overhead your location and if it is dark outside. If both conditions are met, it sends you an email notification to look up at the sky.
If the ISS is close to your current position and it is currently dark, then it sends you an email to tell you to look up.
The program rechecks every 60 seconds to see if the conditions are met.'''

import config
from time import sleep

MY_LAT = -5.139530 # Your latitude
MY_LONG = 45.570392 # Your longitude

while True:
    if config.is_iss_overhead(MY_LAT, MY_LONG) and config.is_dark(MY_LAT, MY_LONG):
        config.send_email("<receiver_email>@gmail.com", f"The ISS is currently overhead at {config.iss_position}. Look up!")
    else:
        print("The ISS is not overhead or it is not dark yet.")
        print(f"Current ISS position: {config.iss_position}")
        print(config.is_dark(MY_LAT, MY_LONG))
    sleep(60)  # Check every 60 seconds
