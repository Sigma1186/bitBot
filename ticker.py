import time, json, requests

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
    print("\n")
    
    time.sleep(2)
