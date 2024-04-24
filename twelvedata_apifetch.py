from twelvedata import TDClient

# api initiate
td = TDClient(apikey="6963c70f85ea4721a62af79975aedc12")

# symbol: stock symbol
# interval: interval between datapoints
# outputsize: n most recent datapoints
ts = td.time_series(symbol="AAPL", interval="1day", outputsize=30).as_pandas()

# output as csv
ts.to_csv('out.csv', index=False)
