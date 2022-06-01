#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.futures import Futures as Client
from binance.websocket.futures.websocket_client import FuturesWebsocketClient

config_logging(logging, logging.DEBUG)

def message_handler(message):
    print(message)

api_key = ""
client = Client(api_key)
response = client.new_listen_key()

logging.info("Receving listen key : {}".format(response["listenKey"]))

ws_client = FuturesWebsocketClient()
ws_client.start()

ws_client.user_data(
    listen_key=response["listenKey"],
    id=1,
    callback=message_handler,
)

time.sleep(30)

logging.debug("closing ws connection")
ws_client.stop()
