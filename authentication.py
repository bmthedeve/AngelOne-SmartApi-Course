import urllib.request
from SmartApi import SmartConnect
import pyotp
from logzero import logger
import urllib
import requests
import json
import pandas as pd

key_secret = open("key.txt","r").read().split()
api_key = key_secret[0]
username = key_secret[2]
pwd = key_secret[3]
smartApi = SmartConnect(api_key)
try:
    token = key_secret[4]
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

data = smartApi.generateSession(username, pwd, totp)

instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())
print(type(instrument_list))

def token_lookup(ticker, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if (instrument["name"] == ticker and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[-1] == "EQ"):
            return instrument["token"]
# print(token_lookup("FUSION", instrument_list,exchange="NSE"))

def ticker_lookup(token, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if (instrument["token"] == token and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[-1] == "EQ"):
            return instrument["name"]
        
params = {
     "exchange": "NSE",
     "symboltoken": token_lookup("INFY",instrument_list),
     "interval": "ONE_MINUTE",
     "fromdate": "2024-04-12 09:15",
     "todate": "2024-04-12 13:30"
}
        
hist_data = smartApi.getCandleData(params)

