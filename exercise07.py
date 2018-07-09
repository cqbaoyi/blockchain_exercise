# https://coinmarketcap.com
import requests, io
import pandas as pd

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = "https://etherscan.io/chart/etherprice?output=csv"
    response = requests.get(url, headers=headers)

    df = pd.read_table(io.StringIO(response.content.decode("UTF-8")), sep=',')
    print(df.columns)
    print(df.info())
    print(df.head())
    print(df.tail())


def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
