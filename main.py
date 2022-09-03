# Eskom Loadshedding API for Embedded Systems
# Author: S2K
# This wraps the HTTP GET requests into simple function calls
# that we can use on embedded boards e.g. OrangePi, RPi, etc
#---------------------------------------------------------------


import requests
from playsound import playsound
import simpleaudio as sa

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
    stage = int(response.text)
    if stage == 1:
        playsound('fanfare-short.wav')
    if stage > 1:
        playsound('sounds/smw_gameover.wav')

    if stage == -1:
        print("  Method returned -1: Looks like Eskom's web interface is down")
        filename = 'cough3.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing

else:
    print("       HTTPS Error or no response")
