import requests
import json
import os

def fetch_data():
    url = "https://dati.regione.sicilia.it/api/3/action/package_list"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully.")
        return data
    else:
        print("Failed to fetch data.")
        return None

def fetch_dataset_details(dataset_id):
    url = f"https://dati.regione.sicilia.it/api/3/action/package_show?id={dataset_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dataset_details = response.json()
        return dataset_details
    else:
        print(f"Failed to fetch details for dataset: {dataset_id}")
        return None

def save_precipitation_data(details):
    if details:
        resources = details.get('result', {}).get('resources', [])
        if not resources:
            print("No resources found for the dataset.")
            return
        
        os.makedirs('datasets', exist_ok=True)

        for resource in resources:
            resource_url = resource.get('url')
            resource_name = resource.get('name')

            if resource_url:
                resource_response = requests.get(resource_url)
                if resource_response.status_code == 200:
                    file_name = f"datasets/{resource_name}.json"
                    with open(file_name, 'w') as f:
                        json.dump(resource_response.json(), f, indent=4)
                    print(f"Saved dataset: {file_name}")
                else:
                    print(f"Failed to download dataset: {resource_name}")
            else:
                print(f"No URL found for resource: {resource_name}")
    else:
        print("No details available to save data.")

if __name__ == "__main__":
    # Fetch the list of datasets
    data = fetch_data()
    
    # Fetch details for the 'sias-precipitazioni' dataset
    dataset_id = 'sias-precipitazioni'  # Specify the dataset you want to explore
    details = fetch_dataset_details(dataset_id)
    
    # Save precipitation datasets
    save_precipitation_data(details)
