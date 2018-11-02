
#Pandas Read CSV:
import pandas as pd

df = pd.read_csv("data/AAPL.csv")
print(df.head()) # just top 5 lines
print(df.tail()) # just last 5 lines
print(df.tail(6)) # just last 6 lines
print(df[10:21]) # data between 10 to 20

#find max close for symbol
def get_max_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    #return df['Volume'].mean()
    return df['Close'].max()


#Plot with matplot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/AAPL.csv")
df['Adj Close'].plot()
plt.show()  #call this to show plots

#plotting two columns
df[['Close', 'Adj Close']].plot()


# Plot Multiple range, multiple stocks, align dates and put dates in proper order
import os
import pandas as pd
import matplotlib.pyplot as plt

#join multiple dataframes

start_date='2010-01-22'
end_date='2010-01-26'
dates=pd.date_range(start_date, end_date) # returns a list

#create empty data frame
df1=pd.DataFrame(index=dates) #use dates as index instead of 0...x

dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

#only those roles from dfSPY that is present in df1 will be joined, those rows that do not have a value will be returned null
#how='inner' will join rows that are common in both dfs
df1 = df1.join(dfSPY, how='inner')

symbols = ['GOOG', 'IBM', 'GLD']
for symbo in symbols:
    df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col='Date',parse_dates=True,usecols=['Date', 'Adj Close'], na_values=['nan'])
    #rename the column on the fly when they dont match
    df_temp = df_temp.rename(columns={'Adj Close': symbol})
    df1=df1.join(df_tmp) #defaults to 'left' join

#drop nan values
df1 = df1.dropna()
print(df1)


#util func to reutrn path of csv file for a stock symbol
def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

#get data from a symbol and set of dates
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

#slicing data

#row slicing, this will only show data for jan
print(df.ix['2010-01-01':'2010-01-31'])

#column slicing
print(df['GOOG'])
print(df['IBM', 'GLD'])

#slice by column and row, displays SPY and IBM over the specified date range
print(df.ix['2010-03-10':'2010-03-15', ['SPY', 'IBM']])


#plotting
def plot_data(df, title="Stock Prices"):
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

#plot specific parts of a data set
def plot_selected(df, columns, start_index, end_index):
    df = df.ix[start_index:end_index, columns]
    df.plot()
    plt.show()

#normalization, using first row of data set
def normalize_data(df):
    return df/df.ix[0,:]