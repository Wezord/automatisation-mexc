from flask import Flask, request, jsonify, render_template, Blueprint, current_app

x3_bp = Blueprint('x3', __name__)

@x3_bp.route('/x3', methods=['GET'])
def x3():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "x3"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('x3.html', strategies = current_app.config['current_alert'])