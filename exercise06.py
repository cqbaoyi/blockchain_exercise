# https://coinmarketcap.com
# pip install urllib3
import requests, json, time, urllib3
import pandas as pd

def main():
    url = "https://api.coinmarketcap.com/v1/ticker"
    http = urllib3.PoolManager()
    tickers_json = http.request("GET", url)
    #print(tickers_json.data)

    df = pd.read_json(url)
    print(df.head())
    print(df.info())

    df = df.sort_values(by=['symbol'])
    for i, r in df.iterrows():
        print(i, r['symbol'], r['price_usd'])

    selections = ["ETH", "BTC"]
    df = df[df["symbol"].isin(selections)]
    print(df[['id', 'price_usd']])

    # Pseudo streaming
    for n in range(0, 4):
        df = pd.read_json("https://api.coinmarketcap.com/v1/ticker/litecoin")
        print(df['price_usd'])
        time.sleep(3)

def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
