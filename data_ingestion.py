import os
import pandas as pd

# Folder containing CSV files
data_folder = "data/raw"

# Check if the folder exists
if not os.path.exists(data_folder):
    print(f"Folder '{data_folder}' not found.")
    exit()

# Get all CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

if not csv_files:
    print("No CSV files found in data/raw")
    exit()

# Read each CSV file
for file in csv_files:
    file_path = os.path.join(data_folder, file)

    print("=" * 60)
    print(f"File: {file}")

    try:
        df = pd.read_csv(file_path)

        print("Shape:", df.shape)
        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")