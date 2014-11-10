
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
        print((a * 100)/localbitcoinLive)

    else:
        a = localbitcoinLive
        print((a * 100)/ coinbaseUSDLive)


'''Create arrays to store BitCoin Values '''
coinbaseValue = []
localbitcoinValue = []
time1 = []
spread1 = []
coinbaseValueCSV = [0]
localbitcoinValueCSV = [0]
timeCSV = [0]
spreadCSV = [0]
##
##'''Creates Array To Store Times'''
##timeKeeperUpdater = []

def timeKeeper():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    time1.append(ts)

def readableTimeKeeper():

    tk = time.time()
    kt = datetime.datetime.fromtimestamp(tk).strftime('%Y-%m-%d %H:%M:%S')
    print (kt)
    
def Spread():
    result = float(abs(coinbaseUSDLive - localbitcoinLive))
    print ("Profit = ", result)
    spread1.append(result)

    


##def exportXl():
##    with open('Almoste.csv', 'a', newline='') as csvfile:
##        spamwriter = csv.writer(csvfile, delimiter=' ',
##                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
##        spamwriter.writerow(coinbaseValueCSV + localbitcoinValueCSV + timeCSV + spreadCSV )
####        spamwriter.writerow(localbitcoinValueCSV)
####        spamwriter.writerow(timeCSV)
####        spamwriter.writerow(spreadCSV)



def exportXL():
    with open('Final.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows(zip(localbitcoinValueCSV, coinbaseValueCSV,spreadCSV, timeCSV))

def updateCSV():

    coinbaseValueCSV[0] = coinbaseValue[-1]
    localbitcoinValueCSV[0] = localbitcoinValue[-1]
    timeCSV[0] = time1[-1]
    spreadCSV[0] = spread1[-1]

while True:
    

    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print ("Coinbase Price in USD =", coinbaseUSDLive)
    print ("________________________________________")
    print ("Localbitcoin Price in USD = ", localbitcoinLive)
    print ("________________________________________")

    Spread()

    print ("________________________________________")

    print (findLarger())

    print ("________________________________________")

    profit()
                              
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    readableTimeKeeper()

    print("\n")

    coinbaseValue.append(coinbaseUSDLive)
    
    localbitcoinValue.append(localbitcoinLive)

    timeKeeper()

    updateCSV()

    exportXL()
    

    time.sleep(300)




