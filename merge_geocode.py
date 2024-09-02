import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Define the main directories
data_dir = 'preprocessed_datasets'
stations_file = 'preprocessed_datasets/elenco-sensori-meteo_csv_rsd.csv'
output_dir = 'geoDataframes'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load the station data with coordinates
stations_df = pd.read_csv(stations_file, delimiter=';', dtype={'ID_STAZ': str})

# Iterate over each year directory
for year_folder in os.listdir(data_dir):
    year_path = os.path.join(data_dir, year_folder)
    
    # Ensure it is a directory
    if os.path.isdir(year_path):
        
        # Create corresponding year directory in output_dir
        output_year_dir = os.path.join(output_dir, year_folder)
        os.makedirs(output_year_dir, exist_ok=True)
        
        # Create subdirectories for Shapefiles and GeoJSON files
        esri_shp_dir = os.path.join(output_year_dir, 'esri_shp')
        geojson_dir = os.path.join(output_year_dir, 'geoJSON')
        os.makedirs(esri_shp_dir, exist_ok=True)
        os.makedirs(geojson_dir, exist_ok=True)
        
        # Iterate over each CSV file in the year directory
        for csv_file in os.listdir(year_path):
            if csv_file.endswith('.csv'):
                csv_path = os.path.join(year_path, csv_file)
                
                # Load the CSV file
                data_df = pd.read_csv(csv_path, delimiter=';', dtype={'ID_STAZ': str})
                
                # Merge with the station data to get coordinates and altitude
                merged_df = pd.merge(data_df, stations_df, on='ID_STAZ', how='left')
                
                # Create a GeoDataFrame with a geometry column (using X_LON and Y_LAT)
                merged_df['geometry'] = merged_df.apply(lambda row: Point(float(row['X_LON']), float(row['Y_LAT'])), axis=1)
                geo_df = gpd.GeoDataFrame(merged_df, geometry='geometry')
                
                # Define the output file paths for Shapefile and GeoJSON
                output_shp_path = os.path.join(esri_shp_dir, os.path.splitext(csv_file)[0] + '.shp')
                output_geojson_path = os.path.join(geojson_dir, os.path.splitext(csv_file)[0] + '.geojson')
                
                # Save the GeoDataFrame as a Shapefile
                geo_df.to_file(output_shp_path, driver="ESRI Shapefile")
                print(f"Saved GeoDataFrame to {output_shp_path}")

                # Save the GeoDataFrame as a GeoJSON file
                geo_df.to_file(output_geojson_path, driver="GeoJSON")
                print(f"Saved GeoDataFrame to {output_geojson_path}")