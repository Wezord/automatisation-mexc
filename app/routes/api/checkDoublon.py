from flask import request, jsonify, Blueprint, current_app
import mexc_api as mapi

check_doublon_bp = Blueprint('check_doublon', __name__)

@check_doublon_bp.route('/check_doublon', methods=['POST'])
def check_doublon():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        doublon = mapi.checkDoublon(data.get("strategy"), int(data.get("quantite")))
        strategies_to_send = [
            {'strategy_order_name': data.get("strategy"), 'type': 'sell', 'position': "long" if actif.split(".")[1] == "2" else "short" ,'alert_message': 'Force Exit', 'actif': actif.split(".")[0] if actif.split(".")[0] != "LUNANEWUSDT.P" else "LUNAUSDT" , 'stop_loss': '0', 'time': '2025-01-11T17:54:00Z'} 
            for actif in doublon
        ]
        return jsonify({"strategies": strategies_to_send}), 200