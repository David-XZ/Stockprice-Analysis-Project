from twelvedata import TDClient

# api key stored on local machine and is not pushed to git
with open("twelvedata_apikey") as f:
    key = f.read()

# api initiate
td = TDClient(apikey=key)

# tdclient paramters
# - symbol: stock symbol
# - interval: interval between datapoints
# - outputsize: n most recent datapoints
ts = td.time_series(symbol="AAPL", interval="1day", outputsize=1000).with_macd().with_ema().as_pandas()

# output stock data as csv
ts.to_csv('out.csv', index=True)
