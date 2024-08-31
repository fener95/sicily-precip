import os
import json
import requests
import zipfile
from io import BytesIO

def download_and_extract_zip(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with zipfile.ZipFile(BytesIO(response.content)) as z:
            z.extractall(save_path)
        print(f"Downloaded and extracted {url} to {save_path}")
    except Exception as e:
        print(f"Failed to download or extract {url}: {e}")

# Load the JSON data
json_file_path = "dataset_details.json"
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Directory to save the extracted CSV files
datasets_dir = "datasets"
os.makedirs(datasets_dir, exist_ok=True)

# Loop through the resources in the JSON file
for resource in data['result']['resources']:
    if resource['format'].upper() == 'CSV':
        file_url = resource['url']
        download_and_extract_zip(file_url, datasets_dir)