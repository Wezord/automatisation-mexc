from flask import Flask, request, jsonify, render_template, Blueprint, current_app
import mexc_api as mapi;

bollinger_bp = Blueprint('bollinger', __name__)

@bollinger_bp.route('/bollinger', methods=['GET'])
def bollinger():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        if current_app.config["current_alert"] == []:
            return jsonify({"strategies": []}), 200
        else :
            open_position = mapi.get_all_open_position("bollinger")
            if open_position > current_app.config["open_position_count"]:
                strategies_to_send = [
                    {'strategy_order_name': "bollinger", 'type': 'sell', 'position': "long" if actif.split("_USDT")[1] == "2" else "short" ,'alert_message': 'Force Exit', 'actif': actif, 'stop_loss': '0', 'time': '2025-01-11T17:54:00Z'} 
                    for actif in open_position]
                return jsonify({"strategies": strategies_to_send}), 200
            strategies_to_send = [
                d for d in current_app.config['current_alert']
                if d["strategy_order_name"] == "bollinger" and not (
                    (d["type"] == "buy" and d["actif"].split(".")[0] in open_position)
                    or 
                    (d["type"] == "sell" and d["actif"].split(".")[0] not in open_position)
                )
            ]
            return jsonify({"strategies": strategies_to_send}), 200
    return render_template('bollinger.html', strategies = current_app.config['current_alert'])