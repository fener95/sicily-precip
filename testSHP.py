import os
import geopandas as gpd

output_dir = 'geoDataframes'

for year_folder in os.listdir(output_dir):
    year_path = os.path.join(output_dir, year_folder)
    
    if os.path.isdir(year_path):
        for shp_file in os.listdir(year_path):
            if shp_file.endswith('.shp'):
                shp_path = os.path.join(year_path, shp_file)
                
                # Load the Shapefile
                gdf = gpd.read_file(shp_path)
                
                # Print basic information to confirm the file is correct
                print(f"File: {shp_file}")
                print(gdf.info())  # Summary of the dataframe
                print(gdf.head())  # Display first few rows
                print("\n")