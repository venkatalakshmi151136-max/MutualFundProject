import pandas as pd

# Load CSV files
fund = pd.read_csv("Data/raw/01_fund_master.csv")
nav = pd.read_csv("Data/raw/02_nav_history.csv")
transactions = pd.read_csv("Data/raw/08_investor_transactions.csv")
performance = pd.read_csv("Data/raw/07_scheme_performance.csv")
aum = pd.read_csv("Data/raw/03_aum_by_fund_house.csv")

# ==========================
# STEP 5: Clean NAV
# ==========================

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()

invalid = nav[nav["nav"] <= 0]
print(invalid)

nav.to_csv("Data/processed/02_nav_history.csv", index=False)

# ==========================
# STEP 6: Clean Investor Transactions
# ==========================

# See first rows
print(transactions.head())

# Standardize Transaction Type
transactions["transaction_type"] = transactions["transaction_type"].replace({
    "sip": "SIP",
    "SIP": "SIP",
    "Redeem": "Redemption",
    "Lump Sum": "Lumpsum"
})

# Remove Invalid Amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Convert Transaction Date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Validate KYC Status
bad = transactions[
    ~transactions["kyc_status"].isin(
        ["Verified", "Pending", "Rejected"]
    )
]

print("Invalid KYC records:")
print(bad)

# Save cleaned file
transactions.to_csv(
    "Data/processed/08_investor_transactions.csv",
    index=False
)

print("Investor transactions cleaned successfully.")

performance = pd.read_csv("Data/raw/07_scheme_performance.csv")

# Remove leading/trailing spaces from column names
performance.columns = performance.columns.str.strip()

# Print all column names
print(performance.columns.tolist())

# Print the first 5 rows
print(performance.head())
print(performance.columns.tolist())
# Convert returns to numeric
performance["return_1yr_pct"] = pd.to_numeric(
    performance["return_1yr_pct"],
    errors="coerce"
)

performance["return_3yr_pct"] = pd.to_numeric(
    performance["return_3yr_pct"],
    errors="coerce"
)

performance["return_5yr_pct"] = pd.to_numeric(
    performance["return_5yr_pct"],
    errors="coerce"
)

# Convert expense ratio to numeric
performance["expense_ratio_pct"] = pd.to_numeric(
    performance["expense_ratio_pct"],
    errors="coerce"
)

# Validate expense ratio
bad = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records:")
print(bad)

# Save cleaned file
performance.to_csv(
    "Data/raw/07_scheme_performance.csv",
    index=False
)

print("Scheme Performance cleaned successfully.")
# ==============================
# STEP 8: Save All Cleaned Files
# ==============================

# Save Fund Master
fund.to_csv(
    "Data/raw/01_fund_master.csv",
    index=False
)

# Save NAV History
nav.to_csv(
    "Data/raw/02_nav_history.csv",
    index=False
)

# Save AUM
aum.to_csv(
    "Data/raw/03_aum_by_fund_house.csv",
    index=False
)

# Save Scheme Performance
performance.to_csv(
    "Data/raw/07_scheme_performance.csv",
    index=False
)

# Save Investor Transactions
transactions.to_csv(
    "Data/raw/08_investor_transactions.csv",
    index=False
)

print("All cleaned datasets saved successfully!")