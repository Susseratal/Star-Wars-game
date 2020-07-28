import os
import sys
import time
import json
import random
import getpass
import os.path
import datetime
from colorama import Fore

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)
    sys.stdout.write("\n")
    sys.stdout.flush()

def save_config():
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
            break
        delay_print("You don't yet have a save file")
            
elif enter == "y":
    settings={}
    print(Fore.WHITE)
    delay_print("Your head hurts...")
    delay_print("Slowly, you open your eyes and look around at the gloomy room around you. You're in the brig.")
    delay_print("Looking at your hands, you wonder: Who... are... you?")
    username=input ("What is your name? ")
    settings["username"]=username
    configfilename = (baseconfigfilename + username)
    delay_print("You struggle to your feet and stumble to the door. Beside it are your clothes and a weapon. What are they? ")
    delay_print("1. Jedi Robes - high dodge, no defence")
    delay_print("2. Clone Armour - low dodge, high defence")
    delay_print("3. Leather Armour - mid dodge, mid defence")
    delay_print("What do you wear? ")
    armour=input("")
    if armour == "1":
        delay_print("You have chosen the Jedi Robes. You fling the cloak around your shoulders and buckle your belt around your waist.")
        settings["armour"]="Jedi Robes"
    elif armour == "2":
        delay_print("A set of armour worn by the Clone soldiers in the Clone Wars. Strong and comfortable, it's perfectly fitted to you.")
        settings["armour"]="Clone Armour"
    elif armour == "3":
        delay_print("A set of basic leather armour, comfortable, durable and light. The perfect set of armour for anyone, mercenary or assassin.")
        settings["armour"]="Leather Armour"
    elif armour == "0" or "none":
        delay_print("You disregard the clothes and remain in your loin cloth")
        settings["armour"]="None"
    else:
        delay_print("You put on your " + armour)
        settings["armour"]=armour
    delay_print("1. Lightsaber - high damage, low range")
    delay_print("2. DC-15A Rifle - high range, low damage")
    delay_print("3. E-5 Blaster - mid range, mid damage")
    delay_print("What do you use? ")
    weapon=input("")
    if weapon == "1":
        delay_print("This is the weapon of a Jedi Knight. Not as clumsy or random as a blaster; an elegant weapon for a more civilized age.")
        settings["weapon"]="Lightsaber"
    elif weapon == "2":
        delay_print("A fairly large rifle with a good range and high damage output at the cost of a low rate of fire.")
        settings["weapon"]="DC-15A Rifle"
    elif weapon == "3":
        delay_print("A cheap, typical pistol. Despite it's low price tag, this weapon won't let you down. Ammo is cheap too.")
        settings["weapon"]="E-5 Blaster"
    elif weapon == "0" or "none":
        delay_print("You bypass the weapons in favour of fighting with your fists.")
    else:
        delay_print("You fasten your " + weapon + " into your belt.")
        settings["weapon"]=weapon
    save_config()

    delay_print("Now that you are ready, you look around at your surroundings more closely. In the darkness, you can see three corridors stretching away from you. ")
