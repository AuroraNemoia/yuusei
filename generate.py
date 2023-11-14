import requests
import os
import json

# constants
base_path = (os.path.abspath(__file__).rsplit('\\', 1)[0] + "\\").replace("\\", "/")
api_base = "https://api.perplexity.ai"
pplx_key = open(base_path + "/pplx_key", "r").read()

def generateText(prompt, temperature, tokens, model):
    payload = {
        "temperature": temperature,
        "max_tokens": tokens,
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": ""
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        'Authorization': 'Bearer ' + pplx_key
    }
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()["choices"][0]["message"]["content"]
    return result