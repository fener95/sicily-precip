Attribution to: Region Siciliana, link at: https://dati.regione.sicilia.it
license: Creative Commons Attribution 4.0 International (CC BY 4.0).

Sicily Ground Precipitation Data Conversion and Analysis

Description

This project retrieves and processes raw precipitation data from Sicily, obtained via the CKAN API from the Region Siciliana data portal. The data, originally in CSV format, includes hourly precipitation values, which are then aggregated into monthly totals for each agrometeorological station (only SIAS stations network:http://www.sias.regione.sicilia.it/ ). The project converts these CSV files into various formats (JSON, GeoJSON, and SHP) and organizes them into yearly folders, making them readily available for geospatial analysis and mapping.

Project Structure
The repository is organized as follows:

datasets/: Contains the raw precipitation data in CSV format.

preprocessed_datasets/: Contains cleaned and preprocessed data.

geoDataframes/: Contains GeoDataFrames with merged and geocoded data.

ee_fc/: Contains JSON files formatted for export as Feature Collection assets in Google Earth Engine (GEE).

Main Scripts
fetch_data_sicily.py: Fetches the raw precipitation data from the CKAN API.

fetch_stations.py: Retrieves station location information using the CKAN API.

preproc_precipitations.py: Aggregates the raw data into monthly totals and processes it by station.

merge_geocode.py: Merges station locations with the aggregated data and geocodes the information.

populate_datasets.py: Manages the organization of datasets into appropriate folders.

testSHP.py: Tests the conversion of data into SHP files.

Motivation

The primary goal of this project is to make geospatial data on precipitation in Sicily easily accessible and ready for analysis. By providing the data in multiple formats and organizing it by year, this repository simplifies the process for researchers and analysts working on geospatial analysis, mapping, and environmental monitoring.

Installation
Prerequisites
Ensure you have the following libraries installed in your environment:

Python 3.x
conda (for environment management)
pandas
geopandas
earthengine-api (ee)
geemap
requests
json
os
zipfile

//------------------------------------------------------------//
To replicate the environment, you can create a conda environment and install the necessary libraries:

/bash/ /WINDOWS powershell/

conda create -n sicily python=3.x
conda activate sicily
conda install pandas geopandas
pip install earthengine-api geemap requests
Setup
Clone the repository and navigate to the project directory:

/bash/------------UNDER REVISION

git clone https://github.com/fener95/sicily-precip.git
cd sicily-precip
/*
Usage
Fetching Data

To fetch the precipitation data and station details, run:
*/
/bash/------------UNDER REVISION

python fetch_stations.py
python fetch_data_sicily.py
Preprocessing Data
To preprocess and aggregate the data, run:

/bash/------------UNDER REVISION

python preproc_precipitations.py
python merge_geocode.py

//--------------------------------------------------------------------------------------------//
Accessing the Data
Processed data can be accessed in the preprocessed_datasets/ and geoDataframes/ directories. Depending on your needs, you can directly use these files for geospatial analysis or mapping.

Extending the Project
You can fork the repository and apply similar methods to other public APIs or add additional data types (e.g., temperature data). Contributions are welcome!

Data Source
The precipitation data is sourced from the CKAN API provided by the Region Siciliana:

Data Attribution: Region Siciliana

Data License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Data Portal: Region Siciliana Data Portal (https://dati.regione.sicilia.it/)

SIAS agro-meteo stations: http://www.sias.regione.sicilia.it/

License
This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

Contact
For any questions or feedback, please reach out via nerifederico1995@gmail.com.

Acknowledgements
Thanks to the Region Siciliana for providing open access to some(2019-2022) of the precipitation data.

Special mention to the developers of the libraries and tools used in this project, including pandas, geopandas, earthengine-api, and geemap.
