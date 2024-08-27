import requests
import json

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

if __name__ == "__main__":
    # Fetch the list of datasets
    data = fetch_data()
    
    # Fetch details for the 'sias-precipitazioni' dataset
    dataset_id = 'sias-precipitazioni'  # Specify the dataset you want to explore
    details = fetch_dataset_details(dataset_id)

    # Save the details to a JSON file
    if details:
        with open('dataset_details.json', 'w') as f:
            json.dump(details, f, indent=4)
        print("Details saved to dataset_details.json")
    else:
        print("Failed to fetch details.")
