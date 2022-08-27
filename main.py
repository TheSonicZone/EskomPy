# Eskom Loadshedding API for Embedded Systems
# Author: S2K
# This wraps the HTTP GET requests into simple function calls
# that we can use on embedded boards e.g. OrangePi, RPi, etc
#---------------------------------------------------------------


import requests

# Get Method Definitions (see API documentation techrad.co.za)
GET_STATUS = "https://loadshedding.eskom.co.za/LoadShedding/GetStatus"


# Program begin
print("Program start...")

# Let's perform the request
print("   Requesting the status from Eskom")
response = requests.get(GET_STATUS)
if response.ok:
    print("       HTTPS Response OK")
    # Let's unpack the data and print it
    print("           >>> Raw Response: " + response.text)
else:
    print("       HTTPS Error or no response")
