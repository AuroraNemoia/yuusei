import os
import json
import jstyleson
from sys import platform
from transformers import AutoTokenizer

def log(text, type="normal"):
    types = {
        "quiet": "\x1b[33;90m",
        "warn": "\x1b[33;20m⚠️ WARN: ",
        "error": "\x1b[31;1m❌ ERROR: ",
        "normal": "\x1b[33;0m"
    }
    print(types.get(type, types["normal"]) + text + "\x1b[0m")

def basePath():
    match platform:
        case "windows":
            return (os.path.abspath(__file__).rsplit('\\', 1)[0] + "\\").replace("\\", "/")
        case _:
            return os.path.dirname(os.path.abspath(__file__).rsplit('\\', 1)[0] + "\\").replace("\\", "/")

config = jstyleson.loads(open(basepath() + "/config.json", "r").read())

log("Using tokenizer from: " + basepath() + "/" + config["settings"]["tokenizer"])
tokenizer = AutoTokenizer.from_pretrained(basepath() + "/" + config["settings"]["tokenizer"])

def tokenize(text):
    tokens = tokenizer.tokenize(text)
    return len(tokens)