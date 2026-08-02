CREATE TABLE dim_fund(

fund_id INTEGER PRIMARY KEY,

amfi_code INTEGER,

fund_name TEXT,

category TEXT,

sub_category TEXT

);

CREATE TABLE dim_date(

date_id INTEGER PRIMARY KEY,

date DATE,

year INTEGER,

month INTEGER,

day INTEGER

);

CREATE TABLE fact_nav(

id INTEGER PRIMARY KEY,

amfi_code INTEGER,

date DATE,

nav REAL,

FOREIGN KEY(amfi_code)

REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_transactions(

id INTEGER PRIMARY KEY,

amfi_code INTEGER,

transaction_type TEXT,

amount REAL,

date DATE,

FOREIGN KEY(amfi_code)

REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_performance(

id INTEGER PRIMARY KEY,

amfi_code INTEGER,

expense_ratio REAL,

return_1y REAL,

return_3y REAL,

return_5y REAL,

FOREIGN KEY(amfi_code)

REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_aum(

id INTEGER PRIMARY KEY,

fund_house TEXT,

aum REAL

);
-- Top 5 Funds by AUM
SELECT * FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV by Month
SELECT strftime('%Y-%m', date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- Total SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio Below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;