import requests
import os
import json

# constants
base_path = (os.path.abspath(__file__).rsplit('\\', 1)[0] + "\\").replace("\\", "/")
api_base = "https://api.perplexity.ai"
pplx_key = open(base_path + "/pplx_key", "r").read()

def generateTextPerplexity(prompt, temperature, tokens, model):
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
    response = requests.post(api_base + "/chat/completions", json=payload, headers=headers)
    result = response.json()["choices"][0]["message"]["content"]
    return result

def generateTextLlamacpp(prompt, temperature, tokens):
    payload = {
        "temperature": temperature,
        "n_predict": tokens,
        "prompt": prompt,
        "stop": ['\n'],
    }

    url = "https://127.0.0.1:8080/completion"
    response = requests.post(url, json=payload)
    result = response.json()["content"]
    return result