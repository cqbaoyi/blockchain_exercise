# https://coinmarketcap.com
import requests, io, json
import matplotlib.pyplot as plt
import pandas as pd

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = "https://etherscan.io/chart/etherprice?output=csv"
    response = requests.get(url, headers=headers)

    df = pd.read_table(io.StringIO(response.content.decode("UTF-8")), sep=',')
    df = df.drop(df.columns[1], axis=1)
    df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'], format="%m/%d/%Y")
    
    df.index = df["Date(UTC)"]
    df = df.drop(df.columns[0], axis=1)
    
    print(df.columns)
    print(df.info())
    print(df.head())
    print(df.tail())

    plt.plot(df)
    plt.show()


def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
