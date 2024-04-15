import requests
import re

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}


def clean_query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    json_data = response.json()
    
    generated_text = json_data[0]['generated_text'] if json_data else ''
    return generated_text


def prompt(Ques):
    prompt = f"Just give only the main key description of the main item in the given input like what is the item, its color and model and just give the neccessary details and dont give the location or position of the item briefly in one line only contain the description.{Ques}\n\n"
    return prompt
