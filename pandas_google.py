"""
This small script helps to check if we can get data
with pandas-datareader from google or yahoo! 
"""
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2000, 1, 1)
end = datetime.date.today()

google = True

if google:
    f = web.DataReader("ETR:SIE", 'google', start, end)
else:
    f = web.DataReader("SIE.DE", 'yahoo', start, end)

print(f.Close)

print("\nDone. {}".format(datetime.datetime.now()))
