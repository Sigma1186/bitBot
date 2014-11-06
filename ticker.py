import time, json, requests, xlsxwriter, datetime, time, csv



def coinbase():
    coinBaseTick = requests.get('https://coinbase.com/api/v1/prices/buy') # replace buy with spot_rate, sell etc
    return coinBaseTick.json()['amount']

def localbitcoins():
    localbitcoinsTick = requests.get ('https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/')
    return localbitcoinsTick.json()['USD']['avg_1h']

coinbaseUSDLive = float(coinbase())
localbitcoinLive = float(localbitcoins())

def findLarger():

    if coinbaseUSDLive == localbitcoinLive:
        return "Both coins are worth the same"

    elif coinbaseUSDLive > localbitcoinLive:
        return "Coinbase is worth more"

    else:
        return "localbitcoinLive is worth more"

def findLargerUSD():

    if coinbaseUSDLive == localbitcoinLive:
        return 0

    elif coinbaseUSDLive > localbitcoinLive:
        return coinbaseUSDLive
    else:
        return localbitcoinLive

    

def profit():
    if findLargerUSD() == coinbaseUSDLive:
        a = coinbaseUSDLive
        return(a * 100)/localbitcoinLive

    else:
        a = localbitcoinLive
        return (a * 100)/ coinbaseUSDLive


'''Create arrays to store BitCoin Values '''
coinbaseValue = []
localbitcoinValue = []
##
##'''Creates Array To Store Times'''
##timeKeeperUpdater = []

def timeKeeper():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print (st)


def Export():
    with open('Trythisnew2.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        for x in coinbaseValue:
            spamwriter.writerow(coindBaseValue[x])
    


while True:
    

    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print ("Coinbase Price in USD =", coinbaseUSDLive)
    print ("________________________________________")
    print ("Localbitcoin Price in USD = ", localbitcoinLive)
    print ("________________________________________")
    print ("Spread = ", float(abs(coinbaseUSDLive - localbitcoinLive)))
    print ("________________________________________")
    print (findLarger())
    print ("________________________________________")
    print ("profit =", profit() , "%")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    timeKeeper()
    print("\n")
    Export()
##    coinbaseValue.append(coinbaseUSDLive)
##    print (coinbaseValue)
##    localbitcoinValue.append(localbitcoinLive)
##    print (localbitcoinValue)
  

    time.sleep(5)




