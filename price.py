import requests
import time
btc=.03
while(True):
    r = requests.get('https://blockchain.info/ticker')
    price = r.json()["USD"]['last']
    print("bitcoin price = $ "+str(price))
    print(str(btc)+"btc       = $ "+str(format(price*btc,'.2f')))
    time.sleep(20)
