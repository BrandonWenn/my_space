#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.delivery.websocket_client import DeliveryWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client()
my_client.start()

my_client.pair_mark_price(
    pair="BTCUSD",
    id=1,
    speed=1,
    callback=message_handler,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
