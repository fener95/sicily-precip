import requests
import json
import os
import zipfile
from io import BytesIO

def fetch_dataset_details(dataset_id):
    url = f"https://dati.regione.sicilia.it/api/3/action/package_show?id={dataset_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dataset_details = response.json()
        print(f"Details fetched successfully for dataset: {dataset_id}")
        return dataset_details
    else:
        print(f"Failed to fetch details for dataset: {dataset_id}")
        return None

def download_and_extract_csv(details, download_path):
    # Loop through the resources in the dataset details to find the ZIP file containing the CSV
    for resource in details['result']['resources']:
        if resource['format'] == 'CSV' and resource['mimetype'] == 'application/zip':
            zip_url = resource['url']
            zip_name = resource['name'] + '.zip'
            zip_path = os.path.join(download_path, zip_name)

            # Download the ZIP file
            response = requests.get(zip_url)
            if response.status_code == 200:
                # Unzip the file and save the CSV
                with zipfile.ZipFile(BytesIO(response.content)) as z:
                    z.extractall(download_path)
                print(f"CSV file extracted and saved in: {download_path}")
                return download_path
            else:
                print(f"Failed to download ZIP file from: {zip_url}")
                return None

    print("No ZIP file containing a CSV was found in the dataset.")
    return None

if __name__ == "__main__":
    # Dataset ID for the station data
    dataset_id = 'elenco-sensori-meteo'  # The dataset you found

    # Fetch details for the selected dataset
    details = fetch_dataset_details(dataset_id)

    # Save the details to a JSON file
    if details:
        json_file_path = 'elenco_sensori_meteo_details.json'
        with open(json_file_path, 'w') as f:
            json.dump(details, f, indent=4)
        print(f"Details saved to {json_file_path}")

        # Define the path to save the extracted CSV file
        download_path = 'preprocessed_datasets'  # Folder within the main directory

        # Create the folder if it doesn't exist
        os.makedirs(download_path, exist_ok=True)

        # Download and extract the CSV file from the ZIP
        download_and_extract_csv(details, download_path)
    else:
        print("Failed to fetch dataset details.")