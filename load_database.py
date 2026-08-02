import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

fund = pd.read_csv("Data/raw/01_fund_master.csv")
nav = pd.read_csv("Data/raw/02_nav_history.csv")
transactions = pd.read_csv("Data/raw/08_investor_transactions.csv")
performance = pd.read_csv("Data/raw/07_scheme_performance.csv")
aum = pd.read_csv("Data/raw/03_aum_by_fund_house.csv")

fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("Database Loaded Successfully")