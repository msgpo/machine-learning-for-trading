import pandas as pd
import matplotlib.pyplot as plt

def get_price(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    #return df['Volume'].mean()
    return df['Close'].max()


def graph_data(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol), parse_dates=True, usecols=["Date", "Close"])
    df['Close'].plot()
    plt.show()

if __name__ == "__main__":
    print (get_price("AMZN"))
    graph_data("AMZN")