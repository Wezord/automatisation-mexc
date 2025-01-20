from flask import Flask, request, jsonify, render_template, Blueprint, current_app

x3_indiv_bp = Blueprint('x3_indiv', __name__)

@x3_indiv_bp.route('/x3_indiv', methods=['GET'])
def x3_indiv():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "x3_indiv"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('x3_indiv.html', strategies = current_app.config['current_alert'])