import requests
import json
import jstyleson
import os
import time
import random
import generate
from utils import log, basepath, tokenize
import history

# Constants
config = jstyleson.loads(open(basePath() + "/config.json", "r").read())

# Initialize self
self_name = config["personality"]["name"]
self_persona = config["personality"]["persona"]
self_instruct_pre = config["personality"]["pre"]
self_instruct_post = config["personality"]["post"]
use_chat_completions = config["settings"]["use_chat_completions"]
force_pre = config["settings"]["force_pre"]

# Have self reply to the current situation.
def answer():
    # What is the current situation?
    prompt = buildPrompt()

def buildPrompt():
    # Build the prompt frontmatter.
    if use_chat_completions == True or force_pre == True:
        frontmatter = self_instruct_pre + self_persona + self_instruct_post
    else: # When using TextCompletions, we do not need to instruct the model, the response prompt does it for us.
        frontmatter = self_persona + self_instruct_post
    frontmatter_length = tokenize(frontmatter)

    # What is our budget for message history?
    history_token_budget = config["settings"]["context_size"] - config["settings"]["max_new_tokens"] - frontmatter_length

    # Let's query messages until we hit the token limit.
    message_event_stack = []
    # TODO: implement checking max_history_items
    event_stack = history.fetchEvents(6)
    token_length = 0
    for event in event_stack:
        if event["event_type"] == "message":
            token_length += tokenize(event["content"])
            if token_length > history_token_budget:
                break
            message_event_stack.append(event)

    # Build the message stack as a string.
    message_stack = ""
    for message in message_event_stack:
        message_stack += (message["name"] + ": " + message["content"] + "\n")

    # Build response prompt (unused in ChatCompletions).
    response_prompt = self_name + ": "
    prompt = frontmatter + message_stack
    if use_chat_completions == False:
        prompt += response_prompt
    
    log(prompt)
    return prompt
answer()