from flask import request, jsonify, render_template, Blueprint, current_app
import mexc_api as mapi

strat_bp = Blueprint('strat', __name__)

@strat_bp.route('/strat', methods=['GET'])
def strat():
    if request.method == "GET" and request.headers.get("X-Custom-Message") != None and request.headers.get("X-Custom-Message").split(".")[0] in current_app.config["list_strategy"] and request.headers.get("X-Custom-Message").split(".")[1] == "get_alert":
        strat_to_use = request.headers.get("X-Custom-Message").split(".")[0]
        strategies_to_send = [d for d in current_app.config['current_strat'] if d["strategy_order_name"] == strat_to_use]
        open_position = mapi.get_all_open_position(strat_to_use)
        return jsonify({"strategies": strategies_to_send, "time_coeff" : len(open_position)}), 200
    return render_template('strat.html', strategies = current_app.config['current_alert'])