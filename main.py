import random
import time
import sys
import json
import os.path
import os
import datetime
import time
import getpass
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

def main():
    baseconfigfilename = os.path.join(os.path.dirname(sys.argv[0]), "savedata_")
    enter = input ("Do you have a save game? Y/N: ")
    enter = enter.lower()
    if enter == "y":
        while True:
            choosesave = input ("Please enter your username: ")
            configfilename = (baseconfigfilename + choosesave)
            if os.path.isfile(configfilename):
                settings=json.load(open(configfilename))
                username=settings["username"]
                notebook.notes=settings["notes"]
            elif choosesave == "cancel":
                delay_print ("quitting...")
                time.sleep(0.5)
                sys.exit()
            else:
                delay_print ("You don't yet have a save file yet")
                sys.exit()
    elif enter == "n":
        settings={}
        username = input ("Please choose a username: ")
        settings["username"]=username
        settings["notes"]=notebook.notes
        configfilename = (baseconfigfilename + username)
        print ("1. Jedi Robes - high dodge, no defence")
        print ("2. Clone Armour - low dodge, high defence")
        print ("3. Leather Armour - mid dodge, mid defence")
        armour = input ("Please choose either robes, clone armour or leather armour: ")
        notebook.addnote(armour)
        print ("1. Lightsaber - high damage, low range")
        print ("2. DC-15A Rifle - high range, low damage")
        print ("3. E-5 Blaster - mid range, mid damage")
        weapon = input ("Please choose either a lightsaber, rifle or blaster: ")
        notebook.addnote(weapon)
        save_config()

    while True:
        enemy=random.randint(1,3)
        if enemy == "1":
            print ("Before you, wrapped in black robes, is a Sith Lord. ")
        elif enemy == "2":
            print ("You find yourself facing off against a battle droid weilding a rifle")
        elif enemy == "3":
            print ("Before you is a tusken raider with a laser rifle.")
        health=100
        enemyhealth=100
        while enemyhealth >= 1:
            if health <= 0:
                delay_print ("You have been slain by your foe. You now lie face down in the dirt where the vultures may pick at your bones. ")
                sys.exit()

main()
