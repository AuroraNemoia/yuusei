import requests
import json
import os
import time
import random
import generate
from utils import log, basepath
import history

# constants
config = json.loads(open(basepath() + "/config.json", "r").read())

# initialize self
self_name = config["personality"]["name"]
self_persona = config["personality"]["persona"]

# Have self reply to the current situation
def answer():
    log("Testing logs.")
    log("Testing logs.", "error")
    log("Testing logs.", "warn")
    log("Testing logs.", "quiet")

answer()

history.fetchEvents(3)