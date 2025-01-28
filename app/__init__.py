from flask import Flask
import mexc_api as mapi
from app.routes.home import home_bp
from app.routes.strategy.bollinger import bollinger_bp
from app.routes.strategy.rsi import rsi_bp
from app.routes.strategy.moving import moving_bp
from app.routes.strategy.x3 import x3_bp
from app.routes.strategy.rsi_storj import rsi_storj_bp
from app.routes.api.alert import alert_bp
from app.routes.api.delete_alert import delete_alert_bp
from app.routes.api.webhook import webhook_bp
from app.routes.api.checkDoublon import check_doublon_bp

def create_app():
    app = Flask(__name__)

    app.config['current_alert'] = [
        {'strategy_order_name': 'rsi_storj', 'actif': 'AGLDUSDT.P', 'alert_message': 'Entry long', 'type': 'buy', 'position': 'long', 'stop_loss': '0', 'time': '2025-01-27T18:50:10Z'},
        {'strategy_order_name': 'rsi_storj', 'actif': 'ZRXUSDT.P', 'alert_message': 'Entry long', 'type': 'buy', 'position': 'long', 'stop_loss': '0', 'time': '2025-01-27T18:50:10Z'},
        {'strategy_order_name': 'rsi_storj', 'actif': 'AGLDUSDT.P', 'alert_message': 'Entry long', 'type': 'buy', 'position': 'long', 'stop_loss': '0', 'time': '2025-01-27T18:50:10Z'},
        {'strategy_order_name': 'rsi_storj', 'actif': 'GALAUSDT.P', 'alert_message': 'Entry long', 'type': 'buy', 'position': 'long', 'stop_loss': '0', 'time': '2025-01-27T18:50:10Z'},
        {'strategy_order_name': 'rsi_storj', 'actif': 'GALAUSDT.P', 'alert_message': 'Entry long', 'type': 'buy', 'position': 'long', 'stop_loss': '0', 'time': '2025-01-27T18:50:10Z'},
        {'strategy_order_name': 'rsi_storj', 'actif': 'DOGEUSDT.P', 'alert_message': 'Exit long', 'type': 'sell', 'position': 'long', 'stop_loss': '0', 'time': '2025-01-27T18:50:10Z'}
    ]
    app.config['open_position_count'] = {
        "bollinger" : len(mapi.get_all_open_position("bollinger")),
        "rsi" : len(mapi.get_all_open_position("rsi")),
        "x3" : len(mapi.get_all_open_position("x3")),
        "moving" : len(mapi.get_all_open_position("moving")),
        "rsi_storj" : len(mapi.get_all_open_position("rsi_storj"))
    }

    # Enregistrer les blueprints
    app.register_blueprint(alert_bp)
    app.register_blueprint(delete_alert_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(check_doublon_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(rsi_bp)
    app.register_blueprint(x3_bp)
    app.register_blueprint(moving_bp)
    app.register_blueprint(bollinger_bp)
    app.register_blueprint(rsi_storj_bp)

    return app