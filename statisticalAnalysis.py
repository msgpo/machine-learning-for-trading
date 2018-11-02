import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

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
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    #Basic stats
    print(df.mean())    #avg
    print(df.median())  #value in middle when all sorted
    print(df.std()) #square root of variance, measure of deviation from the mean the higher the more vary from medium

    #Rolling statistics (Moving average), sma, bollinger

    #calculate rolling mean using 20 day window
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    #calculate rolling standard deviation in 20 day window
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    #passing ax=ax second param will add to existing plot
    #rollingMeanSpy.plot(label="Rolling Mean", ax=ax)

    ax = df['SPY'].plot(title="SPY Bollinger Band", label="SPY")
    rm_SPY.plot(label="Moving Average", ax=ax)
    upper_band.plot(label="upper band", ax=ax)
    lower_band.plot(label="lower band", ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()


def get_rolling_mean(values, window):
    return values.rolling(window=window).mean()

def get_rolling_std(values, window):
    return values.rolling(window=window).std()

def get_bollinger_bands(rm, rstd):
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band


def calculate_daily_return():
    
if __name__ == "__main__":
    test_run()