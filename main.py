import os
import sys
import time
import json
import random
import getpass
import os.path
import datetime
from colorama import Fore
from notes import Notebook
notebook = Notebook()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)
    sys.stdout.write("\n")
    sys.stdout.flush()

def save_config():
    settings["notes"]=notebook.notes
    json.dump(settings, open(configfilename, "w"))

baseconfigfilename = os.path.join(os.path.dirname(sys.argv[0]), "savedata_")
print (Fore.WHITE)
enter=input("Would you like to start a new game? Y/N: ")
enter=enter.lower()
if enter == "n":
    while True:
        choosesave=input("Please enter your username: ")
        configfilename=(baseconfigfilename + choosesave)
        if os.path.isfile(configfilename):
            settings=json.load(open(configfilename))
            username=settings["username"]
            armour=settings["armour"]
            weapon=settings["weapon"]
            notebook.notes=settings["notes"]
            break
        delay_print("You don't yet have a save file")
            
elif enter == "y":
    settings={}
    settings["notes"]=notebook.notes
    print(Fore.WHITE)
    delay_print("Your head hurts...")
    delay_print("Slowly, you open your eyes and look around at the gloomy room around you. You're in the brig.")
    delay_print("You look at your hands. Who... are... you?")
    username=input (" ")
    settings["username"]=username
    configfilename = (baseconfigfilename + username)
    delay_print("You struggle to your feet and stumble to the door. Beside it are your clothes and a weapon. What are they? ")
    delay_print("1. Jedi Robes - high dodge, no defence")
    delay_print("2. Clone Armour - low dodge, high defence")
    delay_print("3. Leather Armour - mid dodge, mid defence")
    delay_print("Please choose either robes, clone armour or leather armour: ")
    armour=input(" ")
    if armour == "1":
        settings["armour"]="Jedi Robes"
    elif armour == "2":
        settings["armour"]="Clone Armour"
    elif armour == "3":
        settings["armour"]="Leather Armour"
    else:
        settings["armour"]=armour
    delay_print("1. Lightsaber - high damage, low range")
    delay_print("2. DC-15A Rifle - high range, low damage")
    delay_print("3. E-5 Blaster - mid range, mid damage")
    delay_print("Please choose either a lightsaber, rifle or blaster: ")
    weapon=input(" ")
    if weapon == "1":
        settings["weapon"]="Lightsaber"
    elif weapon == "2":
        settings["weapon"]="DC-15A Rifle"
    elif weapon == "3":
        settings["weapon"]="E-5 Blaster"
    else:
        settings["weapon"]=weapon
    save_config()

    delay_print("Now that you are dressed, you look around at your surroundings more closely. In the darkness, you can see three corridors stretching away from you. ")
