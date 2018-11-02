import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

#plotting
def plot_data(df, title="Stock Prices", xlabel="Date", ylabel="Price"):
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

#get data from a symbol and set of dates
def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',parse_dates=True,usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        df = df.dropna()

    return df

def test_run():
    dates = pd.date_range('2010-01-01', '2010-01-31')
    symbols = ['SPY', 'AAPL']
    df = get_data(symbols, dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

def compute_daily_returns(df):
    daily_returns = df.copy()
    #compute daily returns for row 1 onwards
    # daily_returns[1:] = (df[1:] / df[:-1].values) -1
    # daily_returns.ix[0, :] = 0  #set daily returns for row 0 to 0
    daily_returns = (df/df.shift(1)) - 1
    daily_returns.ix[0, :] = 0  #set daily returns for row 0 to 0 otherwise pandas will leave these values as NaN
    return daily_returns

if __name__ == "__main__":
    test_run()