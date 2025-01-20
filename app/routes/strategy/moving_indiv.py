from flask import Flask, request, jsonify, render_template, Blueprint, current_app

moving_indiv_bp = Blueprint('moving_indiv', __name__)

@moving_indiv_bp.route('/moving_indiv', methods=['GET'])
def moving_indiv():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "moving_indiv"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('moving_indiv.html', strategies = current_app.config['current_alert'])