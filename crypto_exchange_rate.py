import json

import requests


def main():
    fsym = input('Please enter the crpto-currency code for which you want to check the exchange rate: ')
    tsyms = input('Please enter the Currency code for which you want to check the exchange rate: ')
    rate = getRate(fsym, tsyms)
    print(rate)

def getRate(fsym, tsyms):
    '''
        Getting bitcoins price
    '''
    url = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsyms}")
    rate = url.json()
    return rate[tsyms]

if __name__=="__main__":
    main()