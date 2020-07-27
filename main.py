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
enter=input("Do you have a save game? Y/N: ")
enter=enter.lower()
if enter == "y":
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
        elif choosesave == "cancel":
            delay_print("quitting...")
            time.sleep(0.5)
            sys.exit()
        else:
            delay_print("You don't yet have a save file yet")
            sys.exit()
elif enter == "n":
    settings={}
    settings["notes"]=notebook.notes
    username=input ("Choose a username: ")
    settings["username"]=username
    configfilename = (baseconfigfilename + username)
    print("1. Jedi Robes - high dodge, no defence")
    print("2. Clone Armour - low dodge, high defence")
    print("3. Leather Armour - mid dodge, mid defence")
    armour=input("Please choose either robes, clone armour or leather armour: ")
    if armour == "1":
        settings["armour"]="Jedi Robes"
    elif armour == "2":
        settings["armour"]="Clone Armour"
    elif armour == "3":
        settings["armour"]="Leather Armour"
    else:
        settings["armour"]=armour
    print("1. Lightsaber - high damage, low range")
    print("2. DC-15A Rifle - high range, low damage")
    print("3. E-5 Blaster - mid range, mid damage")
    weapon=input("Please choose either a lightsaber, rifle or blaster: ")
    if weapon == "1":
        settings["weapon"]="Lightsaber"
    elif weapon == "2":
        settings["weapon"]="DC-15A Rifle"
    elif weapon == "3":
        settings["weapon"]="E-5 Blaster"
    else:
        settings["weapon"]=weapon
    save_config()

#print (Fore.WHITE)
#delay_print("Your head hurts...")
#delay_print("Slowly, you open your eyes and look around you at the gloomy environment. You're definitely in the brig. ")
#delay_print("You look at your hands. Who are you? ")
#username = input (" ")
#settings["username"]=username
