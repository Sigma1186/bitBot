import coinbase

coinbase = coinbase.Coinbase.with_api_key('y83RJLRHTjp52yD2', 'rLwtU2WxE5iHZp8HsrQutVX35mKvZ7kW')

balance = coinbase.get_balance()
print('Balance is ' + balance + ' BTC')

rates = coinbase.get_exchange_rate()
print(rates['btc_to_usd'])

print(coinbase.get_buy_price(1))
print(coinbase.get_sell_price(1))
