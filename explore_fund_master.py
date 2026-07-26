import pandas as pd

# Read the CSV file
df = pd.read_csv("data/raw/01_fund_master.csv")

print("CSV Loaded Successfully!")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())