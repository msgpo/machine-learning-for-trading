#kurtosis: fat tail - more out there at end
#           skinny tail - less of unusual at the end

import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) -1
    daily_returns.ix[0, :] = 0
    return daily_returns

def test_run():
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    hist = daily_returns.hist(bins=20)

    #get mean and std deviation
    mean = daily_returns['SPY'].mean()
    print ("Mean=",mean)
    std = daily_returns['SPY'].std()
    print ("Std=",std)

    #plotting
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    
    plt.show()

    #kurtosis
    print (daily_returns.kurtosis())
if __name__ == "__main__":
    test_run()