from flask import request, render_template, Blueprint, current_app
import mexc_api as mapi

strat_bp = Blueprint('strat', __name__)

@strat_bp.route('/strat', methods=['GET'])
def strat():
    if request.method == "GET":
        strategy = request.args.get('strategy')
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == strategy]
        return render_template('strat.html', strategies = strategies_to_send)