from flask import Flask, request, jsonify, render_template, Blueprint, current_app

moving_bp = Blueprint('moving', __name__)

@moving_bp.route('/moving', methods=['GET'])
def moving():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_app.config['current_alert'] if d["strategy_order_name"] == "moving"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('moving.html', strategies = current_app.config['current_alert'])