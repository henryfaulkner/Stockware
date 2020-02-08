from alpha_vantage.timeseries import TimeSeries
import json
from datetime import date, timedelta

class requestData:
    #self.daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    alphavantageKeys = ['2XDB1PE5CFMB5KQY', 'YHFRABURSHV75JOI', 'ONARBE6F0V0XGOPV']

    def weekly_OLH_Data(stockName):
        key = 'YHFRABURSHV75JOI'
        ts = TimeSeries(key)
        reverseWeekList = [] # holds json of previous 7 days in decrementing order 
        stock, meta = ts.get_daily(symbol=stockName)
        y = 0
        openList = []
        lowList = []
        highList = []
        closeList = []
        for i in range(1,8+y):
            day = date.today() - timedelta(days=i)
            while day.strftime('%a') == 'Sat' or day.strftime('%a') =='Sun':
                y += 1
                i += 1
                day = date.today() - timedelta(days=i)
            strDay = day.strftime('%Y-%m-%d')
            openList = stock[strDay]['1. open']
            highList = stock[strDay]['2. high']
            lowList = stock[strDay]['3. low']
            closeList = stock[strDay]['4. close']

        return openList, lowList, highList, closeList

    def timeSeries(stockName):
        key = 'YHFRABURSHV75JOI'
        ts = TimeSeries(key)
        stock, meta = ts.get_daily(symbol=stockName)
        #data = json.loads(stock['2020-02-08'])
        print(stock)
