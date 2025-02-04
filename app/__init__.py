from flask import Flask
import mexc_api as mapi
from app.routes.home import home_bp
from app.routes.strategy.strat import strat_bp
from app.routes.strategy.rsi_storj import rsi_storj_bp
from app.routes.api.alert import get_alert_bp, get_all_alert_bp
from app.routes.api.delete_alert import delete_alert_bp
from app.routes.api.config import config_bp
from app.routes.api.webhook import webhook_bp
from app.routes.api.checkDoublon import check_doublon_bp
from app.routes.api.manageStrategy import add_strategy_bp
from app.routes.api.manageStrategy import del_strategy_bp
import json
import os


def create_app():
    app = Flask(__name__)

    app.config['current_alert'] = [
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ZRXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "YGGUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "XRPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "WOOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "WAXPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "UNIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "TRXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "TLMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "THETAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SXPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SUSHIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "STORJUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "STGUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SPELLUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SOLUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SNXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SHIBUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SFPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "SANDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "RUNEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "RSRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ROSEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "RLCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "QTUMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "PEOPLEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "OPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "OGNUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "NKNUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "NEARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "MKRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "METISUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "MASKUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "MAGICUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "LUNAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "LTCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "LPTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "LOOKSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "LINKUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "LDOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "KSMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "KNCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "KLAYUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "JOEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "IOTAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "IMXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ICPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "HOTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "GRTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "GMTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "GALAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "FXSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "FLOKIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "FILECOINUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ETHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ETCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "EOSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ENSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ENJUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "DYDXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "DOTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "DOGEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "DENTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "DARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "CRVUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "COTIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "COMPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "CHZUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "CHRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "CELRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "CELOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "CAKEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "C98USDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "BNXNEWUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "BNTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "BNBUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "BCHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "BATUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "BANDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "AXSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "AVAXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ATOMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ARPAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "APEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ANKRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "ALGOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "AGLDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "AAVEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_storj",
        "actif": "1INCHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ZRXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "YGGUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "XRPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "WOOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "WAXPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "UNIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "TRXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "TLMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "THETAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SXPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SUSHIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "STORJUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "STGUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SPELLUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SOLUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SNXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SHIBUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SFPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "SANDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "RUNEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "RSRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ROSEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "RLCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "QTUMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "PEOPLEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "OPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "OGNUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "NKNUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "NEARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "MKRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "METISUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "MASKUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "MAGICUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "LUNAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "LTCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "LPTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "LOOKSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "LINKUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "LDOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "KSMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "KNCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "KLAYUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "JOEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "IOTAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "IMXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ICPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "HOTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "GRTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "GMTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "GALAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "FXSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "FLOKIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "FILECOINUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ETHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ETCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "EOSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ENSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ENJUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "DYDXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "DOTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "DOGEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "DENTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "DARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "CRVUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "COTIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "COMPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "CHZUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "CHRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "CELRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "CELOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "CAKEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "C98USDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "BNXNEWUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "BNTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "BNBUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "BCHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "BATUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "BANDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "AXSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "AVAXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ATOMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ARPAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "APEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ANKRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "ALGOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "AGLDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "AAVEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_atom",
        "actif": "1INCHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ZRXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "YGGUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "XRPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "WOOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "WAXPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "UNIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "TRXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "TLMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "THETAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SXPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SUSHIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "STORJUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "STGUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SPELLUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SOLUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SNXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SHIBUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SFPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "SANDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "RUNEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "RSRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ROSEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "RLCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "QTUMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "PEOPLEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "OPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "OGNUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "NKNUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "NEARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "MKRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "METISUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "MASKUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "MAGICUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "LUNAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "LTCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "LPTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "LOOKSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "LINKUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "LDOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "KSMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "KNCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "KLAYUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "JOEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "IOTAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "IMXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ICPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "HOTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "GRTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "GMTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "GALAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "FXSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "FLOKIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "FILECOINUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ETHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ETCUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "EOSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ENSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ENJUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "DYDXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "DOTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "DOGEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "DENTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "DARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "CRVUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "COTIUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "COMPUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "CHZUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "CHRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "CELRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "CELOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "CAKEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "C98USDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "BNXNEWUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "BNTUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "BNBUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "BCHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "BATUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "BANDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "AXSUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "AVAXUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ATOMUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ARUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ARPAUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "APEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ANKRUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "ALGOUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "AGLDUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "AAVEUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    },
    {
        "strategy_order_name": "rsi_dyd",
        "actif": "1INCHUSDT.P",
        "alert_message": "Entry short",
        "type": "buy",
        "position": "short",
        "stop_loss": "0",
        "time": "2025-02-04T11:00:00Z"
    }
]

    app.config['open_position_count'] = {
        "bollinger" : len(mapi.get_all_open_position("bollinger")),
        "rsi" : len(mapi.get_all_open_position("rsi")),
        "x3" : len(mapi.get_all_open_position("x3")),
        "moving" : len(mapi.get_all_open_position("moving")),
        "rsi_storj" : len(mapi.get_all_open_position("rsi_storj"))
    }

    app.config["list_strategy"] = []

    try:
        # Assure-toi que le chemin du fichier est correct
        config_path = os.path.join("app/config.json")  # Chemin absolu vers config.json
        
        # Ouvre et charge le contenu du fichier config.json
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
            for strategy in config_data["strategy"]:
                app.config["list_strategy"].append(strategy["value"])
        print(app.config["list_strategy"])
    except Exception as e:
        print(e)

    # Enregistrer les blueprints
    app.register_blueprint(get_alert_bp)
    app.register_blueprint(get_all_alert_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(strat_bp)
    app.register_blueprint(delete_alert_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(check_doublon_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(rsi_storj_bp)
    app.register_blueprint(add_strategy_bp)
    app.register_blueprint(del_strategy_bp)

    return app