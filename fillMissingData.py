#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html

import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

#get data from a symbol and set of dates
def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',parse_dates=True,usecols=['Date', 'Adj Close'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    return df

def test_run():
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['FAKE']
    df = get_data(symbols, dates)
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)

    df.plot()
    plt.show()

if __name__ == "__main__":
    test_run()