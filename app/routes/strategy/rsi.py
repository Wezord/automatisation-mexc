from flask import Flask, request, jsonify, render_template, Blueprint, current_app

rsi_bp = Blueprint('rsi', __name__)

@rsi_bp.route('/rsi', methods=['GET'])
def rsi():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "rsi"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('rsi.html', strategies = current_app.config['current_alert'])