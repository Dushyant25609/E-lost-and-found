import os
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def img_query_lost(filename):
    current_directory = os.getcwd()
    current_folder = "static/images"
    final_folder = current_directory + "/" + current_folder + "/" + str(filename)
    
    if os.path.exists(final_folder):  # Check if the file exists
        with open(final_folder, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    else:
        print(f"Error: File '{final_folder}' not found.")
        return None
    
def img_query_found(filename):
    current_directory = os.getcwd()
    current_folder = "static/images"
    final_folder = current_directory + "/" + current_folder + "/" + str(filename)
    
    if os.path.exists(final_folder):  # Check if the file exists
        with open(final_folder, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    
    else:
        print(f"Error: File '{final_folder}' not found.")
        return None
    

