import requests, io, json
import matplotlib.pyplot as plt
import pandas as pd

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    startdate = "2018-01-01"
    enddate = "2018-05-28"
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=" + startdate + "&end=" + enddate
    response = requests.get(url, headers=headers)

    df = pd.read_json(response.content)
    df = df['bpi']
    df.drop(df.tail(2).index, inplace=True)
    print(df.head())
    print(df.shape)


def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
