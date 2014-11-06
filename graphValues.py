import time, json, requests, xlsxwriter, datetime, time, csv

def coinbase():
    coinBaseTick = requests.get('https://coinbase.com/api/v1/prices/buy') # replace buy with spot_rate, sell etc
    return coinBaseTick.json()['amount']

def localbitcoins():
    localbitcoinsTick = requests.get ('https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/')
    return localbitcoinsTick.json()['USD']['avg_1h']

coinbaseUSDLive = int(float(coinbase()))
localbitcoinLive = int(float(localbitcoins()))
coinbaseValue = []
localbitcoinValue = []

def Export():
    with open('Try.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        x=0
        for x in coinbaseValue:
            spamwriter.writer(["sdfsdf"])

while True:
    coinbaseValue.append(coinbaseUSDLive)
    print (coinbaseValue)
    localbitcoinValue.append(localbitcoinLive)
    print (localbitcoinValue)
    Export()
    time.sleep(5)
d
