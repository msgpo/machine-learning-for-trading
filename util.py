import pandas as pd
import matplotlib.pyplot as plt
import os

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: #add SPY for reference if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',parse_dates=True,usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        df = df.dropna()
    return df

def plot_data(df, title="Stock Prices",  xlabel="Date", ylabel="Price"):
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()
