from flask import Flask, request, jsonify, render_template, Blueprint, current_app

bollinger_indiv_bp = Blueprint('bollinger_indiv', __name__)

@bollinger_indiv_bp.route('/bollinger_indiv', methods=['GET'])
def bollinger_indiv():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "bollinger_indiv"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('bollinger_indiv.html', strategies = current_app.config['current_alert'])