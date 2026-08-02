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

# Check result
print(transactions.head())
bad = transactions[
    ~transactions["kyc_status"].isin(
        ["Verified", "Pending", "Rejected"]
    )
]

print("Invalid KYC Status Records:")
print(bad)

# Save cleaned transactions
transactions.to_csv(
    "Data/processed/08_investor_transactions.csv",
    index=False
)

print("Investor transactions saved successfully.")
performance = pd.read_csv("Data/raw/07_scheme_performance.csv")

# Remove leading/trailing spaces from column names
performance.columns = performance.columns.str.strip()

# Check column names
print(performance.columns)

# View first rows
print(performance.head())
# Convert Returns to numeric
performance["1Y Return"] = pd.to_numeric(
    performance["1Y Return"],
    errors="coerce"
)

performance["3Y Return"] = pd.to_numeric(
    performance["3Y Return"],
    errors="coerce"
)

performance["5Y Return"] = pd.to_numeric(
    performance["5Y Return"],
    errors="coerce"
)

# Validate Expense Ratio
bad = performance[
    (performance["expense_ratio"] < 0.1) |
    (performance["expense_ratio"] > 2.5)
]

print("Invalid Expense Ratio Records:")
print(bad)

# Save cleaned file
performance.to_csv(
    "Data/processed/07_scheme_performance.csv",
    index=False
)

print("Scheme Performance cleaned successfully.")
# Save Fund Master
fund.to_csv(
    "Data/processed/01_fund_master.csv",
    index=False
)

# Save NAV History
nav.to_csv(
    "Data/processed/02_nav_history.csv",
    index=False
)

# Save AUM by Fund House
aum.to_csv(
    "Data/processed/03_aum_by_fund_house.csv",
    index=False
)

# Save Scheme Performance
performance.to_csv(
    "Data/processed/07_scheme_performance.csv",
    index=False
)

# Save Investor Transactions
transactions.to_csv(
    "Data/processed/08_investor_transactions.csv",
    index=False
)

print("All cleaned datasets have been saved successfully!")