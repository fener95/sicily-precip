import os
import pandas as pd

def read_and_preprocess_data(data_directory, output_directory):
    """
    Reads all CSV files in the specified directory, processes them,
    and saves the aggregated precipitation data to year-specific subfolders.

    Args:
    data_directory (str): Path to the directory containing CSV files.
    output_directory (str): Path to the directory where processed files will be saved.

    Returns:
    pd.DataFrame: A DataFrame containing the aggregated precipitation data.
    """
    dataframes = []

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through each file in the directory
    for filename in os.listdir(data_directory):
        if filename.endswith('.csv'):
            # Construct the full file path
            file_path = os.path.join(data_directory, filename)
            
            # Read the CSV file
            monthly_precipitation = pd.read_csv(file_path, sep=';')

            # Print the columns and the first few rows to understand the structure
            print(f"Columns in {filename}: {monthly_precipitation.columns.tolist()}")

            if not monthly_precipitation.empty:
                # Convert 'DATARIL' to datetime
                monthly_precipitation['DATARIL'] = pd.to_datetime(monthly_precipitation['DATARIL'])
                
                # Create 'Year' and 'Month' columns
                monthly_precipitation['Year'] = monthly_precipitation['DATARIL'].dt.year
                monthly_precipitation['Month'] = monthly_precipitation['DATARIL'].dt.month
                
                # Aggregate the data by 'ID_STAZ' and 'Year', 'Month'
                aggregated_data = (monthly_precipitation
                                   .groupby(['ID_STAZ', 'Year', 'Month'])['VALORE']
                                   .sum()
                                   .reset_index())

                # Create a year-specific subfolder
                year_folder = os.path.join(output_directory, str(aggregated_data['Year'].iloc[0]))
                os.makedirs(year_folder, exist_ok=True)

                # Save the aggregated data to a new CSV file in the year-specific folder
                output_file_path = os.path.join(year_folder, f'aggregated_{filename}')
                aggregated_data.to_csv(output_file_path, index=False, sep=';')
                print(f"Saved aggregated data to {output_file_path}")

                dataframes.append(aggregated_data)
            else:
                print(f"Warning: {filename} is empty.")

    # Combine all DataFrames into one
    if dataframes:
        combined_data = pd.concat(dataframes, ignore_index=True)
        return combined_data
    else:
        print("No valid data found.")
        return pd.DataFrame()  # Return an empty DataFrame if no valid data is found

# Test the function
if __name__ == "__main__":
    data_directory = r'C:/Users/Utente/Desktop/sicily_data/sicily-precip/datasets'  # Update with your actual path
    output_directory = r'C:/Users/Utente/Desktop/sicily_data/sicily-precip/preprocessed_datasets'  # New folder path
    result = read_and_preprocess_data(data_directory, output_directory)

    # Print the resulting DataFrame
    print(result.head())  # Display the first few rows of the combined DataFrame