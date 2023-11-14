import pickledb
from utils import log, basepath

history = pickledb.load(basepath() + "/history.db", True)
try:
    history.lget("events", 0)
except:
    log("History doesn't exist, creating!", "warn")
    history.lcreate("events")

log("Loaded history with " + str(history.llen("events")) + " events!")

def saveEvent(event):
    history.ladd("events", event)

def fetchEvents(count):
    length = history.llen("events")
    return history.lrange("events", length-count, length)