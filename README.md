# Sicily Precipitation Data Analysis (sicily-precip)

Welcome to the Sicily Precipitation Data Analysis repository! 🌧️🌍 Dive into comprehensive precipitation data from Sicily's agrometeorological stations, meticulously processed and ready for your geospatial analysis and environmental monitoring projects.

## Table of Contents

- 📖 [Description](#-description)
- 🔍 [Project Structure](#-project-structure)
- 🚀 [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setup](#setup)
- ⚙️ [Usage](#-usage)
  - [Fetching Data](#fetching-data)
  - [Preprocessing Data](#preprocessing-data)
  - [SPP Downscaling](#spp-downscaling)
- 📂 [Accessing the Data](#-accessing-the-data)
- 🔧 [Extending the Project](#-extending-the-project)
- 📚 [Data Source](#-data-source)
- 📄 [License](#-license)
- 🤝 [Contributing](#-contributing)
- 📬 [Contact](#-contact)
- 🙏 [Acknowledgements](#-acknowledgements)

---

## 📖 Description

The `sicily-precip` project is designed to retrieve, convert, and analyze precipitation data from Sicily's agrometeorological stations (SIAS). Leveraging the CKAN API from the Region Siciliana Data Portal, this repository transforms raw hourly precipitation CSV data into monthly aggregated totals. The processed data is then converted into versatile formats like JSON, GeoJSON, and SHP, organized by year for seamless integration into geospatial tools and mapping applications.

Additionally, the repository includes methodologies for downscaling Satellite Precipitation Products (SPP) to a finer resolution, enhancing the granularity and usability of precipitation data for detailed environmental analyses.

---

## 🔍 Project Structure

```plaintext
sicily-precip/
│
├── datasets/                # Raw precipitation data in CSV format
├── preprocessed_datasets/   # Cleaned and aggregated monthly data
├── geoDataframes/           # GeoDataFrames with geocoded station data
├── ee_fc/                   # JSON files for Google Earth Engine Feature Collections
├── SPP_downscaling/         # Downscaling of Satellite Precipitation Products
│   ├── charts/              # Generated charts from downscaling analysis
│   ├── maps/                # Maps visualizing downscaled precipitation data
│   └── scripts_ipynb/       # Jupyter notebooks for downscaling processes
│       └── SPP_downscaling_1Km.ipynb  # Notebook for 1 km resolution downscaling
├── scripts/
│   ├── fetch_data_sicily.py
│   ├── fetch_stations.py
│   ├── preproc_precipitations.py
│   ├── merge_geocode.py
│   ├── populate_datasets.py
│   └── testSHP.py
├── LICENSE
├── README.md
└── requirements.txt
```
---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine for development and analysis.

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Conda**: [Install Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/fener95/sicily-precip.git
    cd sicily-precip
    ```

2. **Create a Conda Environment**

    Create and activate a new Conda environment named `sicily`:

    ```bash
    conda create -n sicily python=3.x
    conda activate sicily
    ```

3. **Install Dependencies**

    Install the required Python libraries:

    ```bash
    conda install pandas geopandas
    pip install earthengine-api geemap requests
    ```

    Alternatively, install all dependencies at once:

    ```bash
    pip install -r requirements.txt
    ```

### Setup

1. **Authenticate Google Earth Engine (GEE)**

    If you plan to use GEE features, authenticate your account:

    ```bash
    earthengine authenticate
    ```

2. **Verify Directory Structure**

    Ensure all folders (`datasets/`, `preprocessed_datasets/`, etc.) are present. If not, create them:

    ```bash
    mkdir datasets preprocessed_datasets geoDataframes ee_fc scripts SPP_downscaling charts maps scripts_ipynb
    ```

---

## ⚙️ Usage

### Fetching Data

Retrieve the latest precipitation data and station information from the Region Siciliana data portal.

1. **Fetch Station Information**

    ```bash
    python scripts/fetch_stations.py
    ```

    This script retrieves location details of all SIAS agrometeorological stations.

2. **Fetch Precipitation Data**

    ```bash
    python scripts/fetch_data_sicily.py
    ```

    This script downloads raw hourly precipitation CSV files for each station.

### Preprocessing Data

Aggregate and process the raw data for analysis.

1. **Aggregate Precipitation Data**

    ```bash
    python scripts/preproc_precipitations.py
    ```

    This script aggregates hourly data into monthly totals per station.

2. **Merge and Geocode Data**

    ```bash
    python scripts/merge_geocode.py
    ```

    Combines aggregated data with station locations and prepares GeoDataFrames.

3. **Organize Datasets**

    ```bash
    python scripts/populate_datasets.py
    ```

    Structures the processed data into yearly folders and converts them into JSON, GeoJSON, and SHP formats.

4. **Test SHP Conversion**

    ```bash
    python scripts/testSHP.py
    ```

    Validates the SHP file conversion process.

### SPP Downscaling

Enhance precipitation data resolution using the downscaling methodology outlined in the `SPP_downscaling_1Km.ipynb` notebook.

#### **Objective:**
Perform **downscaling of Satellite Precipitation Products (SPP)** to a 1 km resolution using **Google Earth Engine (GEE)**. The end result is an ImageCollection representing monthly precipitation data for Sicily, providing high-resolution insights into rainfall patterns over the past two decades.

#### **Methodology and Steps:**

1. **Setup and Authentication**
    - Initialize GEE and authenticate the environment within the notebook.
    - Import necessary libraries (`geemap`, `ee`).

    ```python
    import ee
    ee.Authenticate(auth_mode='notebook')
    ee.Initialize(project='mapping-applications')
    import geemap
    ```

2. **Define the Study Area**
    - Define Sicily by filtering the FAO GAUL dataset.
    - Specify a polygon geometry for processing.

    ```python
    gaul = ee.FeatureCollection('FAO/GAUL/2015/level2')
    region = gaul.filter(ee.Filter.eq('ADM1_NAME', 'Sicilia'))
    geometry = region.geometry()
    ```

3. **Data Source and Precipitation Product Selection**
    - Utilize a long-term precipitation dataset (e.g., CHIRPS, ERA5) available through GEE.
    - Set the temporal range to 2001-2020.

4. **Downscaling Methodology**
    - **Spatial Downscaling**: Resample or reproject precipitation data to 1 km resolution using interpolation or statistical methods.
    - **Temporal Aggregation**: Aggregate data monthly to derive long-term precipitation patterns.

5. **Processing Workflow**
    - **Filtering by Date and Region**: Filter the dataset for 2001-2020 and clip to Sicily.
    - **Resampling and Interpolation**: Use `reduceResolution` or `resample` methods for finer-grained estimates.
    - **Conversion to ImageCollection**: Convert downscaled data to an ImageCollection for analysis in GEE.

6. **Export and Visualization**
    - Export the downscaled ImageCollection to Google Drive or display directly using `geemap`.

    ```python
    Map = geemap.Map()
    Map.centerObject(region, 7)
    ```

#### **Output:**
- A **Google Earth Engine ImageCollection** representing **20 years of monthly precipitation data** for Sicily, downscaled to **1 km resolution**.
- Useful for:
  - Hydrological modeling
  - Agricultural planning
  - Climate studies and environmental monitoring

#### **Key Takeaways:**
- **Use of GEE for Downscaling**: Leveraging GEE’s computing resources and geospatial data.
- **Focus on Sicily**: Targeting detailed analysis for Sicily.
- **Comprehensive 20-Year Period**: Providing long-term precipitation insights.

For detailed methodology and code, refer to the [SPP_downscaling_1Km.ipynb](SPP_downscaling/scripts_ipynb/SPP_downscaling_1Km.ipynb) notebook.

---

## 📂 Accessing the Data

Once preprocessing is complete, access the data in the following directories:

- **`preprocessed_datasets/`**: Cleaned and aggregated monthly precipitation data.
- **`geoDataframes/`**: Geocoded dataframes for spatial analysis.
- **`ee_fc/`**: JSON files formatted for Google Earth Engine Feature Collections.
- **`SPP_downscaling/`**:
  - **`charts/`**: Generated charts from downscaling analysis.
  - **`maps/`**: Maps visualizing downscaled precipitation data.
  - **`scripts_ipynb/`**: Jupyter notebooks for downscaling processes.

You can directly utilize these files in GIS applications, mapping tools, or integrate them into your environmental monitoring workflows.

---

## 🔧 Extending the Project

Enhance the repository by:

- **Forking the Repository**: Apply similar data processing methods to other public APIs or datasets.
- **Adding Additional Data Types**: Incorporate other meteorological data such as temperature, humidity, or wind speed.
- **Improving Data Visualizations**: Create interactive maps or dashboards using libraries like `geemap` or `Plotly`.
- **Expanding Downscaling Methods**: Implement advanced downscaling techniques or explore different spatial resolutions.

Contributions are highly encouraged! See the [Contributing](#-contributing) section for more details.

---

## 📚 Data Source

- **Primary Data Provider**: Region Siciliana Data Portal
- **SIAS Agrometeorological Stations**: SIAS Network
- **API Access**: CKAN API from Region Siciliana

**Data Attribution**: Region Siciliana  
**Data License**: Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 📄 License

This project is licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE) License. You are free to share and adapt the material for any purpose, even commercially, as long as appropriate credit is given.

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, improving documentation, or adding new features, your help is appreciated.

1. **Fork the Repository**

2. **Create a New Branch**

    ```terminal
    git checkout -b feature/YourFeature
    ```

3. **Commit Your Changes**

    ```terminal
    git commit -m "Add your message"
    ```

4. **Push to the Branch**

    ```terminal
    git push origin feature/YourFeature
    ```

5. **Open a Pull Request**

For major changes, please open an issue first to discuss your ideas.

---

## 📬 Contact

Have questions or feedback? Reach out to me at:

📧 [nerifederico1995@gmail.com](mailto:nerifederico1995@gmail.com)

---

## 🙏 Acknowledgements

- **Data Provider**: Thanks to the Region Siciliana for providing open access to precipitation data (2019-2022).
- **Libraries and Tools**: Special thanks to the developers of `pandas`, `geopandas`, `earthengine-api`, and `geemap` for their invaluable tools that made this project possible.
- **Google Earth Engine**: For providing a robust platform for geospatial analysis and downscaling methodologies.

---

Happy analyzing! 📊🌦️


