from flask import request, jsonify, Blueprint, current_app
import mexc_api as mapi

get_alert_bp = Blueprint('get_alert', __name__)
get_all_alert_bp = Blueprint('get_all_alert', __name__)

@get_alert_bp.route('/get_alert', methods=['GET'])
def get_alert():
    if request.method == "GET" and request.args.get('strategy') != None and request.args.get('strategy') in current_app.config["list_strategy"]:
        strategy = request.args.get('strategy')
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == strategy]
        open_position = mapi.get_all_open_position(strategy)
        return jsonify({"strategies": strategies_to_send, "time_coeff" : len(open_position)}), 200
    return jsonify({"error" : "hehe"}), 500

@get_all_alert_bp.route('/get_all_alert', methods=['GET'])
def get_all_alert():
    if request.method == "GET":
        return jsonify({"strategies": current_app.config['current_alert']}), 200