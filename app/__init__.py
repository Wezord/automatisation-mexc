from flask import Flask
from app.routes.home import home_bp
from app.routes.strategy.bollinger import bollinger_bp
from app.routes.strategy.rsi import rsi_bp
from app.routes.strategy.moving import moving_bp
from app.routes.strategy.x3 import x3_bp
from app.routes.api.alert import alert_bp
from app.routes.api.delete_alert import delete_alert_bp
from app.routes.api.webhook import webhook_bp

def create_app():
    app = Flask(__name__)

    app.config['current_alert'] = []
    app.config['open_position_count'] = {
        "bollinger" : 0,
        "rsi" : 0,
        "x3" : 0,
        "moving" : 0
    }

    # Enregistrer les blueprints
    app.register_blueprint(alert_bp)
    app.register_blueprint(delete_alert_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(rsi_bp)
    app.register_blueprint(x3_bp)
    app.register_blueprint(moving_bp)
    app.register_blueprint(bollinger_bp)

    return app