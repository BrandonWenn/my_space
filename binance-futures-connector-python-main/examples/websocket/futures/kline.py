#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.futures.websocket_client import FuturesWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client()
my_client.start()

my_client.kline(
    symbol="btcusdt",
    id=12,
    interval='1d',
    callback=message_handler,
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()