import json
from utils import log

def dispatch(json):
    event_type = json["eventType"]
    match event_type:
        # case "some type":
        #     function_that_handels_some_type()
        case _:
            log("This type is not implemented in the dispatcher.", "error")