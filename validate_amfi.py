import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Replace 'scheme_code' with your actual column name if different
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in NAV History.")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)