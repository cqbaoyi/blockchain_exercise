import requests, io, json, time
import matplotlib.pyplot as plt
import pandas as pd

def main():
    startdate = "2018-01-01"
    enddate = "2018-05-28"
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=" + startdate + "&end=" + enddate
    df = load(url, printout = True, remove_bottom_rows = 2, remove_columns = ["disclaimer"])

    df = df['bpi']


def load(url, printout = False, delay = 0, remove_bottom_rows = 0, remove_columns = []):
    time.sleep(delay)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    df = pd.read_json(response.text)
    if remove_bottom_rows > 0:
        df.drop(df.tail(remove_bottom_rows).index, inplace = True)
    df.drop(columns = remove_columns, axis = 1, inplace = True)
    df = df.dropna(axis = 1)
    if printout:
        print(df.head())
        print(df.shape)
    
    return df


if __name__ == "__main__":
    main()
