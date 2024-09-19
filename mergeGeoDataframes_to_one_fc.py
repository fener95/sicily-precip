import os
import geopandas as gpd
import pandas as pd

# Path to the folder containing subfolders (each corresponding to a year)
base_path = r'C:\Users\Utente\Desktop\sicily_data\sicily-precip\geoDataframes'  # Use raw string for Windows paths

# List to store all the GeoDataFrames for each year
gdf_list = []

# Loop over each year folder
for year_folder in os.listdir(base_path):
    year_path = os.path.join(base_path, year_folder)
    
    # Check if the path is indeed a directory (to avoid files in the base path)
    if os.path.isdir(year_path):
        # Construct the path to the geojson subfolder
        geojson_folder = os.path.join(year_path, 'geojson')
        
        # Check if the geojson subfolder exists
        if os.path.isdir(geojson_folder):
            # Get the list of GeoJSON files in the geojson folder
            for file in os.listdir(geojson_folder):
                if file.endswith(".geojson"):
                    # Construct the full path of the GeoJSON file
                    geojson_path = os.path.join(geojson_folder, file)
                    
                    # Load the GeoJSON into a GeoDataFrame
                    gdf = gpd.read_file(geojson_path)
                    
                    # Add a new column to indicate the year (based on the folder name)
                    gdf['year'] = year_folder
                    
                    # Append the GeoDataFrame to the list
                    gdf_list.append(gdf)
                else:
                    print(f"File skipped (not GeoJSON): {file}")
        else:
            print(f"GeoJSON folder not found for year: {year_folder}")

# Check if any GeoDataFrames were loaded
if not gdf_list:
    print("No GeoDataFrames were loaded. Check the file paths and formats.")
else:
    # Concatenate all the GeoDataFrames into one
    final_gdf = pd.concat(gdf_list, ignore_index=True)

    # Define the path to save the merged GeoDataFrame
    save_path = r'C:\Users\Utente\Desktop\sicily_data\sicily-precip\SPP_downscaling\mergedStations_geojson.geojson'
    
    # Save the combined GeoDataFrame as a GeoJSON
    final_gdf.to_file(save_path, driver='GeoJSON')

    # You can also check the first few rows to ensure everything was merged correctly
    print("GeoDataFrame saved successfully at:", save_path)
    print(final_gdf.head())
    print(final_gdf.info())