# Eskom Loadshedding API for Embedded Systems
# Author: S2K
# This wraps the HTTP GET requests into simple function calls
# that we can use on embedded boards e.g. OrangePi, RPi, etc
#---------------------------------------------------------------


import requests
import simpleaudio as sa
import os, platform, subprocess, re


# Get Method Definitions (see API documentation techrad.co.za)
GET_STATUS = "https://loadshedding.eskom.co.za/LoadShedding/GetStatus"


def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    return ""






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
        # Testing different sound library
        # https://realpython.com/playing-and-recording-sound-python/
        filename = 'fanfare-short.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
    if stage > 1:
        # Testing different sound library
        # https://realpython.com/playing-and-recording-sound-python/
        filename = 'smw_gameover.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing

    if stage == -1:
        print("  Method returned -1: Looks like Eskom's web interface is down")
        filename = 'babycrying.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing

else:
    print("       HTTPS Error or no response")
