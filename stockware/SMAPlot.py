import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p

class SMAPlot:
    
    def SMAPlot(stockName):
        ticker = stockName
        timeframe = '1y'

        c = p.client.Client('pk_cdd78e399db34cd5ad08525a8c05d2b5')
        df = c.chartDF(ticker, timeframe)
        df=df[['close']]
        df.reset_index(level=0, inplace = True)
        df.columns=['ds', 'y']
        
        plt.plot(df.ds, df.y)

        
        rolling_mean = df.y.rolling(window=20).mean()
        rolling_mean2 = df.y.rolling(window=50).mean()
        
        plt.plot(df.ds, df.y, label=ticker)
        plt.plot(df.ds, rolling_mean, label = ticker + ' 20 Day SMA', color='orange')
        plt.plot(df.ds, rolling_mean2, label = ticker + ' 50 Day SMA', color='magenta')
        plt.legend(loc='upper left')
        
        exp1 = df.y.ewm(span=20, adjust=False).mean()
        exp2 = df.y.ewm(span=50, adjust=False).mean()
        
        plt.plot(df.ds, df.y, label= ticker)
        plt.plot(df.ds, exp1, label= ticker + ' 20 Day EMA')
        plt.plot(df.ds, exp2, label= ticker + ' 50 Day EMA')
        plt.legend(loc='upper left')
        plt.show()
