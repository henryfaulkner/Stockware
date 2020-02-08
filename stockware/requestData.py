from alpha_vantage.timeseries import TimeSeries
import json

class requestData:
    def timeSeries(stockName):
        key = 'YHFRABURSHV75JOI'
        ts = TimeSeries(key)
        stock, meta = ts.get_weekly(symbol=stockName)
        #data = json.loads(stock['2020-02-08'])
        print(stock['2020-02-07'])
