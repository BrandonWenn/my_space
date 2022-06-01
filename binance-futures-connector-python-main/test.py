from tkinter import N
from binance.futures import Futures 
import json

start_time = Futures().time()

# open an AIP file
with open('api-keys.json') as file:
    dicts = json.load(file)
    key = dicts["binance_02"]["key"]
    secret = dicts["binance_02"]["secret"]
    
# connecting Exchange
client = Futures(key=key, secret=secret)

# Get wallet balance 
for item in client.balance():
    if item["asset"] == str('USDT'):
        print(item["balance"])




# # Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.002,
#     'price': 59808
# }

# response = client.new_order(**params)
# print(response)