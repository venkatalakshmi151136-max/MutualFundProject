# Data Dictionary

## dim_fund

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI Code |
| fund_name | TEXT | Name of Mutual Fund |
| category | TEXT | Fund Category |

## fact_nav

| Column | Type | Description |
|--------|------|-------------|
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |