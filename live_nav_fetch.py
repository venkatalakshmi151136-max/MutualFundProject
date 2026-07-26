import requests
import pandas as pd
import os

# Create output folder
os.makedirs("data/raw", exist_ok=True)

# AMFI Codes
amfi_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in amfi_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching NAV data for {code}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{code}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    else:

        print(f"Failed to fetch data for {code}")