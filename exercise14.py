import requests, io, json, time
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

def main():
    blotter, col_names = initialize_blotter()
    data = pd.DataFrame([[dt.datetime.now(), "ETH", 1.223, 541.33]], columns = col_names)
    blotter = blotter.append(data, ignore_index = True)
    data = pd.DataFrame([[dt.datetime.now(), "ETH", 1.3, 542.33]], columns = col_names)
    blotter = blotter.append(data, ignore_index = True)
    data = pd.DataFrame([[dt.datetime.now(), "ETH", 1.4, 541.23]], columns = col_names)
    blotter = blotter.append(data, ignore_index = True)
    print(blotter)



def initialize_blotter():
    col_names = ["Timestamp", "Pair", "Quantity", "Executed Price"]
    df = pd.DataFrame(columns = col_names)
    return df, col_names

def get_trades_for_product(product_id):
    return load("https://api.gdax.com/products/" + product_id + "/trades", printout = False)


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
