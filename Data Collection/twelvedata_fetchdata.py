from twelvedata import TDClient

# api key
with open("twelvedata_apikey") as f:
    key = f.read()
print(key)
# api initiate
td = TDClient(apikey=key)

# symbol: stock symbol
# interval: interval between datapoints
# outputsize: n most recent datapoints
ts = td.time_series(symbol="AAPL", interval="1day", outputsize=30).as_pandas()

# output as csv
ts.to_csv('out.csv', index=False)
