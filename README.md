Sicily Precipitation Data Analysis (sicily-precip)

  

Welcome to the Sicily Precipitation Data Analysis repository! 🌧️🌍 Dive into comprehensive precipitation data from Sicily's agrometeorological stations, meticulously processed and ready for your geospatial analysis and environmental monitoring projects.

Table of Contents

📖 Description

🔍 Project Structure

🚀 Getting Started

Prerequisites

Installation

Setup


⚙️ Usage

Fetching Data

Preprocessing Data


📂 Accessing the Data

🔧 Extending the Project

📚 Data Source

📄 License

🤝 Contributing

📬 Contact

🙏 Acknowledgements



---

📖 Description

The sicily-precip project is designed to retrieve, convert, and analyze precipitation data from Sicily's agrometeorological stations (SIAS). Leveraging the CKAN API from the Region Siciliana Data Portal, this repository transforms raw hourly precipitation CSV data into monthly aggregated totals. The processed data is then converted into versatile formats like JSON, GeoJSON, and SHP, organized by year for seamless integration into geospatial tools and mapping applications.


---

🔍 Project Structure

sicily-precip/
│
├── datasets/                # Raw precipitation data in CSV format
├── preprocessed_datasets/   # Cleaned and aggregated monthly data
├── geoDataframes/           # GeoDataFrames with geocoded station data
├── ee_fc/                   # JSON files for Google Earth Engine Feature Collections
│
├── scripts/
│   ├── fetch_data_sicily.py
│   ├── fetch_stations.py
│   ├── preproc_precipitations.py
│   ├── merge_geocode.py
│   ├── populate_datasets.py
│   └── testSHP.py
│
├── LICENSE
├── README.md
└── requirements.txt


---

🚀 Getting Started

Follow these steps to set up the project on your local machine for development and analysis.

Prerequisites

Ensure you have the following installed:

Python 3.x: Download Python

Conda: Install Conda


Installation

1. Clone the Repository

git clone https://github.com/fener95/sicily-precip.git
cd sicily-precip


2. Create a Conda Environment

Create and activate a new Conda environment named sicily:

conda create -n sicily python=3.x
conda activate sicily


3. Install Dependencies

Install the required Python libraries:

conda install pandas geopandas
pip install earthengine-api geemap requests

Alternatively, install all dependencies at once:

pip install -r requirements.txt



Setup

1. Authenticate Google Earth Engine (GEE)

If you plan to use GEE features, authenticate your account:

earthengine authenticate


2. Verify Directory Structure

Ensure all folders (datasets/, preprocessed_datasets/, etc.) are present. If not, create them:

mkdir datasets preprocessed_datasets geoDataframes ee_fc scripts




---

⚙️ Usage

Fetching Data

Retrieve the latest precipitation data and station information from the Region Siciliana data portal.

1. Fetch Station Information

python scripts/fetch_stations.py

This script retrieves location details of all SIAS agrometeorological stations.


2. Fetch Precipitation Data

python scripts/fetch_data_sicily.py

This script downloads raw hourly precipitation CSV files for each station.



Preprocessing Data

Aggregate and process the raw data for analysis.

1. Aggregate Precipitation Data

python scripts/preproc_precipitations.py

This script aggregates hourly data into monthly totals per station.


2. Merge and Geocode Data

python scripts/merge_geocode.py

Combines aggregated data with station locations and prepares GeoDataFrames.


3. Organize Datasets

python scripts/populate_datasets.py

Structures the processed data into yearly folders and converts them into JSON, GeoJSON, and SHP formats.


4. Test SHP Conversion

python scripts/testSHP.py

Validates the SHP file conversion process.




---

📂 Accessing the Data

Once preprocessing is complete, access the data in the following directories:

preprocessed_datasets/: Cleaned and aggregated monthly precipitation data.

geoDataframes/: Geocoded dataframes for spatial analysis.

ee_fc/: JSON files formatted for Google Earth Engine Feature Collections.


You can directly utilize these files in GIS applications, mapping tools, or integrate them into your environmental monitoring workflows.


---

🔧 Extending the Project

Enhance the repository by:

Forking the Repository: Apply similar data processing methods to other public APIs or datasets.

Adding Additional Data Types: Incorporate other meteorological data such as temperature, humidity, or wind speed.

Improving Data Visualizations: Create interactive maps or dashboards using libraries like geemap or Plotly.


Contributions are highly encouraged! See the Contributing section for more details.


---

📚 Data Source

Primary Data Provider: Region Siciliana Data Portal

SIAS Agrometeorological Stations: SIAS Network

API Access: CKAN API from Region Siciliana


Data Attribution: Region Siciliana
Data License: Creative Commons Attribution 4.0 International (CC BY 4.0)


---

📄 License

This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License. You are free to share and adapt the material for any purpose, even commercially, as long as appropriate credit is given.


---

🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, improving documentation, or adding new features, your help is appreciated.

1. Fork the Repository


2. Create a New Branch

git checkout -b feature/YourFeature


3. Commit Your Changes

git commit -m "Add your message"


4. Push to the Branch

git push origin feature/YourFeature


5. Open a Pull Request



For major changes, please open an issue first to discuss your ideas.


---

📬 Contact

Have questions or feedback? Reach out to me at:

📧 nerifederico1995@gmail.com


---

🙏 Acknowledgements

Data Provider: Thanks to the Region Siciliana for providing open access to precipitation data (2019-2022).

Libraries and Tools: Special thanks to the developers of pandas, geopandas, earthengine-api, and geemap for their invaluable tools that made this project possible.



---

Happy analyzing! 📊🌦️

