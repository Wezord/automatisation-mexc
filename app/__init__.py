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

    app.config['current_alert'] = []

    # Faire l'auto pour ça
    app.config['open_position_count'] = {
        "bollinger" : len(mapi.get_all_open_position("bollinger")),
        "rsi" : len(mapi.get_all_open_position("rsi")),
        "x3" : len(mapi.get_all_open_position("x3")),
        "moving" : len(mapi.get_all_open_position("moving")),
        "x3_uni" : len(mapi.get_all_open_position("x3_uni"))
    }

    app.config['crypto_status'] = {
        'x3' : {},
        'x3_uni' : {},
        'bollinger' : {},
        'moving' : {},
        'rsi' : {}
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