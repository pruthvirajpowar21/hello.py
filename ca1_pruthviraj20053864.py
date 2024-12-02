# -*- coding: utf-8 -*-
"""CA1_Pruthviraj20053864.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ypqU1gAyf-K0D7AHO_DDj7hPpoGKJRDr
"""

import requests
import json
import pandas as pd

url= 'https://scanner.tradingview.com/america/scan?label-product=markets-screener'

data= '{"columns":["name","description","logoid","update_mode","type","typespecs","close","pricescale","minmov","fractional","minmove2","currency","change","volume","relative_volume_10d_calc","market_cap_basic","fundamental_currency_code","price_earnings_ttm","earnings_per_share_diluted_ttm","earnings_per_share_diluted_yoy_growth_ttm","dividends_yield_current","sector.tr","market","sector","recommendation_mark"],"ignore_unknown_fields":false,"options":{"lang":"en"},"range":[0,50],"sort":{"sortBy":"name","sortOrder":"asc","nullsFirst":false},"preset":"all_stocks"}'

headers={'accept':'application/json',
'accept-encoding':'gzip, deflate',
'accept-language':'en-US,en;q=0.9,hi;q=0.8,mr;q=0.7',
'content-length':'563',
'content-type':'text/plain;charset=UTF-8',
'cookie':'_sp_ses.cf1a=*; cookiesSettings={"analytics":false,"advertising":false}; cookiePrivacyPreferenceBannerProduction=accepted; __eoi=ID=aac7aee3a2a2b9c5:T=1732972096:RT=1732980356:S=AA-Afjaey0UBmZBkAIPVIRvylCcQ; _sp_id.cf1a=.1732552509.1.1733017659..41c9660c-6040-48e8-bbe1-b4913fa6ba3a..9dbb7a43-a83a-44ca-85e4-ea6c0de51b10.1732552509323.72',
'origin':'https://www.tradingview.com',
'priority':'u=1, i',
'referer':'https://www.tradingview.com/',
'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

r=requests.post(url,data=data,headers=headers)

r

r.content

j=json.loads(r.content)

j.keys()

pd.json_normalize(j['data'])

df=pd.json_normalize(j['data'])
df

for index in range(len(df)):
    print(df.at[index, 'd'])

df.rename(columns={'d': 'Stock Details'}, inplace=True)
df

df[['market','stock']] = df['s'].str.split(':',expand=True)
df

df = df.drop(columns=['s'])
df

# Assuming your DataFrame is named 'df' and has a column 'Stock Details'

# Split the 'Stock Details' column into multiple columns
# Handling cases where the number of splits might vary
split_details = df['Stock Details'].str.split(',', expand=True)

# Create new columns, filling with None if not enough splits
num_new_cols = 7  # Number of expected columns: streaming_type, asset_class, etc.
new_cols = ["Ticker", "Company Name", "Slug", "Stream Type", "Asset Type", "Stock Category",
    "Last Price", "Volume", "Lot Size", "Is Active", "Dividend", "Currency",
    "Price Change", "Market Volume", "Volatility", "Market Cap", "Market Cap Currency",
    "PE Ratio", "EPS", "Book Value", "Dividend Yield",
    "Industry", "Region", "Sector", "Beta"]

for i, col_name in enumerate(new_cols):
    if i < split_details.shape[1]:
        df[col_name] = split_details[i]
    else:
        df[col_name] = None  # Or any other default value



# Display the DataFrame with the new columns
print(df)

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    # If any of the new columns have NaN values for this row
    if row[["Ticker", "Company Name", "Slug", "Stream Type", "Asset Type", "Stock Category",
    "Last Price", "Volume", "Lot Size", "Is Active", "Dividend", "Currency",
    "Price Change", "Market Volume", "Volatility", "Market Cap", "Market Cap Currency",
    "PE Ratio", "EPS", "Book Value", "Dividend Yield",
    "Industry", "Region", "Sector", "Beta"]].isnull().any():
        # Check if 'Stock Details' is a string before splitting
        if isinstance(row['Stock Details'], str):
            details = row['Stock Details'].split(',')
        else: # If not a string, assume it's already a list
            details = row['Stock Details']

        # Assign the split values to the corresponding columns
        for i, col_name in enumerate(["Ticker", "Company Name", "Slug", "Stream Type", "Asset Type", "Stock Category",
    "Last Price", "Volume", "Lot Size", "Is Active", "Dividend", "Currency",
    "Price Change", "Market Volume", "Volatility", "Market Cap", "Market Cap Currency",
    "PE Ratio", "EPS", "Book Value", "Dividend Yield",
    "Industry", "Region", "Sector", "Beta"]):
            if i < len(details):
                df.loc[index, col_name] = details[i]
            else:
                # If there are fewer values in 'Stock Details' than columns, keep NaN or assign a default value
                df.loc[index, col_name] = None  # Or any other default value

# Display the updated DataFrame
print(df)

# Before the loop, explicitly set the data type of relevant columns to 'object'
for col in ["Ticker", "Company Name", "Slug", "Stream Type", "Asset Type", "Stock Category",
    "Last Price", "Volume", "Lot Size", "Is Active", "Dividend", "Currency",
    "Price Change", "Market Volume", "Volatility", "Market Cap", "Market Cap Currency",
    "PE Ratio", "EPS", "Book Value", "Dividend Yield",
    "Industry", "Region", "Sector", "Beta"]:  # Add other string columns as needed
    df[col] = df[col].astype(object)

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    # If any of the new columns have NaN values for this row
    if row[["Ticker", "Company Name", "Slug", "Stream Type", "Asset Type", "Stock Category",
    "Last Price", "Volume", "Lot Size", "Is Active", "Dividend", "Currency",
    "Price Change", "Market Volume", "Volatility", "Market Cap", "Market Cap Currency",
    "PE Ratio", "EPS", "Book Value", "Dividend Yield",
    "Industry", "Region", "Sector", "Beta"]].isnull().any():
        # Check if 'Stock Details' is a string before splitting
        if isinstance(row['Stock Details'], str):
            details = row['Stock Details'].split(',')
        else:  # If not a string, assume it's already a list
            details = row['Stock Details']

        # Assign the split values to the corresponding columns
        for i, col_name in enumerate(["Ticker", "Company Name", "Slug", "Stream Type", "Asset Type", "Stock Category",
    "Last Price", "Volume", "Lot Size", "Is Active", "Dividend", "Currency",
    "Price Change", "Market Volume", "Volatility", "Market Cap", "Market Cap Currency",
    "PE Ratio", "EPS", "Book Value", "Dividend Yield",
    "Industry", "Region", "Sector", "Beta"]):
            if i < len(details):
                df.loc[index, col_name] = details[i]
            else:
                # If there are fewer values in 'Stock Details' than columns, keep NaN or assign a default value
                df.loc[index, col_name] = None  # Or any other default value

# Display the updated DataFrame
print(df)

df

df.rename(columns={'Ticker': 'Symbol'}, inplace=True)

df = df.drop(columns=['Slug'])

df

# Assuming your DataFrame is named 'df'
import pandas as pd

# 1. Debt-to-Equity Ratio Score (using 'PE Ratio' as a proxy)
# Higher PE Ratio can sometimes indicate higher growth potential, but also higher risk
# Adjust bins and labels according to your risk tolerance
df['Debt_to_Equity_Score'] = pd.cut(df['PE Ratio'].astype(float, errors='ignore'),
                                     bins=[-float('inf'), 15, 30, float('inf')],
                                     labels=[3, 2, 1])  # Lower PE ratios get higher scores

# 2. Market Capitalization Score (using 'Market Cap' as a proxy for stability)
# Larger market cap companies are generally considered more stable
df['Market_Cap_Score'] = pd.cut(df['Market Cap'].astype(float, errors='ignore'),
                                  bins=[-float('inf'), 1e9, 1e10, float('inf')],  # Adjust bins as needed
                                  labels=[1, 2, 3])  # Larger market caps get higher scores

# 3. Dividend Yield Score (using 'Dividend Yield' as a proxy for income potential)
# Higher dividend yields can be attractive for long-term investors
df['Dividend_Yield_Score'] = pd.cut(df['Dividend Yield'].astype(float, errors='ignore'),
                                     bins=[-float('inf'), 0.02, 0.04, float('inf')],  # Adjust bins as needed
                                     labels=[1, 2, 3])  # Higher yields get higher scores

# 4. Volatility Score (using 'Beta' as a proxy for risk)
# Lower beta indicates lower volatility compared to the market
df['Volatility_Score'] = pd.cut(df['Beta'].astype(float, errors='ignore'),
                                  bins=[-float('inf'), 0.5, 1.0, float('inf')],  # Adjust bins as needed
                                  labels=[3, 2, 1])  # Lower betas get higher scores


# 5. Combine scores with weights (example)
# Convert categorical columns to numerical using .cat.codes before performing calculations
df['Long_Term_Investment_Potential'] = (df['Debt_to_Equity_Score'].cat.codes.astype(int) * 0.3 +  # 30% weight
                                        df['Market_Cap_Score'].cat.codes.astype(int) * 0.3 +  # 30% weight
                                        df['Dividend_Yield_Score'].cat.codes.astype(int) * 0.2 +  # 20% weight
                                        df['Volatility_Score'].cat.codes.astype(int) * 0.2  # 20% weight
                                        )

# 6. Categorize the score
df['Long_Term_Investment_Potential'] = pd.cut(df['Long_Term_Investment_Potential'],
                                               bins=[-float('inf'), 2, 2.5, float('inf')],
                                               labels=['Low', 'Medium', 'High'])

df

df.dropna(inplace=True)
df

df.dtypes

df = df.drop(columns=['Stock Details','Stream Type','Stock Category'])

df

import sqlite3
connection = sqlite3.connect('stock.db', check_same_thread=False)
df.to_sql('stock_data', connection, if_exists='append', index=False)
cursor = connection.cursor()

cursor.execute("SELECT * FROM stock_data")
rows = cursor.fetchall()
rows

!pip install Flask

from flask import Flask
from flask import render_template
from flask import request
!pip install flask_cors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/getStock", methods=['GET']) #Get Shoes
def get_stock_data():
  cursor.execute("SELECT * FROM stock_data")
  rows = cursor.fetchall()
  Results=[]
  for row in rows: #Format the Output Results and get to return string
    Result={}
    Result['market']=row[0]
    Result['stock']=row[1]
    Result['Symbol']=row[2]
    Result['Company Name']=row[3]
    Result['Asset Type']=row[4]
    Result['Last Price']=row[5]
    Result['Volume']=row[6]
    Result['Lot Size']=row[7]
    Result['Is Active']=row[8]
    Result['Dividend']=row[9]
    Result['currency']=row[10]
    Results['Price Change']=row[11]
    Result['Market Volume']=row[12]
    Result['Volatility']=row[13]
    Result['Market Cap']=row[14]
    Result['Market Cap Currency']=row[15]
    Result['PE Ratio']=row[16]
    Result['EPS']=row[17]
    Result['Book Value']=row[18]
    Result['Dividend Yield']=row[19]
    Result['Industry']=row[20]
    Result['Region']=row[21]
    Result['Sector']=row[22]
    Result['Beta']=row[23]
    Result['Debt_to_Equity_Score']=row[24]
    Result['Market_Cap_Score']=row[25]
    Result['Dividend_Yield_Score']=row[26]
    Result['Volatility_Score']=row[27]
    Result['Long_Term_Investment_Potential']=row[28]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format

if __name__ == "__main__":
  #app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  app.run(host='0.0.0.0',port='5000', debug=True) #Run the flask app at port 8080
  #app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080