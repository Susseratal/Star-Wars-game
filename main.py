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

def read_password():
    return getpass.getpass("Password: ", stream=None)

def save_config():
    settings["notes"]=notebook.notes
    json.dump(settings, open(configfilename, "w"))

def main():
    baseconfigfilename = os.path.join(os.path.dirname(sys.argv[0]), "savedata_")
