from flask import Flask, request, jsonify, render_template, Blueprint, current_app

rsi_indiv_bp = Blueprint('rsi_indiv', __name__)

@rsi_indiv_bp.route('/rsi_indiv', methods=['GET'])
def rsi_indiv():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "rsi_indiv"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('rsi_indiv.html', strategies = current_app.config['current_alert'])