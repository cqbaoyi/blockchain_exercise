# obtain BTC-USD rate and convert the Ether historical price as a function of spot BTC price and chart it
#
#
# https://www.coindesk.com/api
# Create a single pandas DF that joins BTC and USD with date as index and a fourth column that is the price of ETH in units of BTC. Chart last column

import requests, io, json, urllib3
import matplotlib.pyplot as plt
import pandas as pd

url_0 = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2018-05-28"
http = urllib3.PoolManager()
tickers_json = http.request("GET", url_0)
df_0 = pd.read_json(url_0)
#btc_rate = float(json.loads(tickers_json.data)['bpi']['USD']['rate'])

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://etherscan.io/chart/etherprice?output=csv"
response = requests.get(url, headers=headers)

df = pd.read_table(io.StringIO(response.content.decode("UTF-8")), sep=',')
df = df.drop(df.columns[1], axis=1)
df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'], format="%m/%d/%Y")
df['Value'] = df['Value'] / btc_rate

df.index = df["Date(UTC)"]
df = df.drop(df.columns[0], axis=1)

#plt.plot(df)
#plt.show()

#if __name__ = "__main__":
#    main()
