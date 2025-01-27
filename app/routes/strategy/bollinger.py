from flask import Flask, request, jsonify, render_template, Blueprint, current_app
import mexc_api as mapi;

bollinger_bp = Blueprint('bollinger', __name__)

@bollinger_bp.route('/bollinger', methods=['GET'])
def bollinger():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "bollinger"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('bollinger.html', strategies = current_app.config['current_alert'])