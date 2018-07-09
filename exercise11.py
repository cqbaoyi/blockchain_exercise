import requests, io, json, time
import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = load("https://api.gdax.com/products", printout = True)
    for i, r in df.iterrows():
        print(r["id"])


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
