#!/usr/bin/env python
import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

futures_client = Client()

logging.info(futures_client.index_price_klines("BTCUSDT", "1d", **{"limit": 500}))