from flask import request, jsonify, Blueprint, current_app
import mexc_api as mapi

check_doublon_bp = Blueprint('check_doublon', __name__)

@check_doublon_bp.route('/check_doublon', methods=['POST'])
def check_doublon():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        doublon = mapi.checkDoublon(data.get("strategy"), int(data.get("quantite")))
        strategies_to_send = []
        for actif in doublon :
            if actif.split(".")[0] == "BNXNEWUSDT":
                actif = 'BNXUSDT.' + actif.split(".")[1]
            elif actif.split(".")[0] == "FILECOINUSDT":
                actif = "FILUSDT." + actif.split(".")[1]
            elif actif.split(".")[0] == "LUNANEWUSDT":
                actif = "LUNAUSDT." + actif.split(".")[1]
            print(actif)
            strategies_to_send.append({'strategy_order_name': data.get("strategy"), 'type': 'sell', 'position': "long" if actif.split(".")[1] == "1" else "short" ,'alert_message': 'Force Exit', 'actif': actif.split(".")[0], 'stop_loss': '0', 'time': '2025-01-11T17:54:00Z'})
        return jsonify({"strategies": strategies_to_send}), 200