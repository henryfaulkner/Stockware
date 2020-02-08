from alpha_vantage.timeseries import TimeSeries
import json
import matplotlib.pyplot as plt
from datetime import date, timedelta

class timeSeriesPlot:

    def timeSeriesPlot(stockName):
        stockName = stockName
        key = 'YHFRABURSHV75JOI'
        ts = TimeSeries(key, output_format='pandas')
        data, meta_data = ts.get_intraday(symbol= stockName, interval ='1min', outputsize = 'full')
        data['4. close'].plot()
        plt.title('Intraday Time Series for the ' + stockName + ' stock 1 min')
        plt.show()
