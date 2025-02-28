from flask import request, jsonify, Blueprint, current_app
import mexc_api as mapi

check_doublon_bp = Blueprint('check_doublon', __name__)

@check_doublon_bp.route('/check_doublon', methods=['POST'])
def check_doublon():
    if request.method == "POST":
        data = request.get_json()
        doublon = mapi.checkDoublon(int(data.get("quantite")), current_app.config['apiKey'][0][data.get('strategy')], current_app.config['secretKey'][0][data.get('strategy')])
        current_crypto = mapi.get_all_open_position(current_app.config['apiKey'][0][data.get('strategy')], current_app.config['secretKey'][0][data.get('strategy')])
        strategies_to_send = []
        temp_crypt = []
        for actif in current_crypto:
            actif_name = actif.split(".")[0]
            if actif_name == "BNXNEWUSDT":
                actif_name = 'BNXUSDT.' + actif.split(".")[1]
            elif actif_name == "FILECOINUSDT":
                actif_name = "FILUSDT." + actif.split(".")[1]
            elif actif_name == "LUNANEWUSDT":
                actif_name = "LUNAUSDT." + actif.split(".")[1]
            if temp_crypt != [] and actif_name in temp_crypt:
                strategies_to_send.append({'strategy_order_name': data.get("strategy"), 'type': 'sell', 'position': "short" ,'alert_message': 'Force Exit pas lieu detre', 'actif': actif_name, 'stop_loss': '0', 'take_profit' : '0', 'time': '2025-01-11T17:54:00Z'})
                strategies_to_send.append({'strategy_order_name': data.get("strategy"), 'type': 'sell', 'position': "long"  ,'alert_message': 'Force Exit pas lieu detre', 'actif': actif_name, 'stop_loss': '0', 'time': '2025-01-11T17:54:00Z'})
            temp_crypt.append(actif_name)
            if actif in current_app.config['crypto_status'][data.get('strategy')]:
                if current_app.config['crypto_status'][data.get('strategy')][actif] == 0:
                    strategies_to_send.append({'strategy_order_name': data.get("strategy"), 'type': 'sell', 'position': "long" if actif.split(".")[1] == "1" else "short" ,'alert_message': 'Force Exit pas lieu detre', 'actif': actif_name, 'stop_loss': '0', 'take_profit' : '0', 'time': '2025-01-11T17:54:00Z'})
        print(doublon)
        for actif in doublon :
            actif_name = actif.split(".")[0]
            if actif_name == "BNXNEWUSDT":
                actif_name = 'BNXUSDT.' + actif.split(".")[1]
            elif actif_name == "FILECOINUSDT":
                actif_name = "FILUSDT." + actif.split(".")[1]
            elif actif_name == "LUNANEWUSDT":
                actif_name = "LUNAUSDT." + actif.split(".")[1]
            strategies_to_send.append({'strategy_order_name': data.get("strategy"), 'type': 'sell', 'position': "long" if actif.split(".")[1] == "1" else "short" ,'alert_message': 'Force Exit Doublon', 'actif': actif_name, 'stop_loss': '0', 'take_profit' : '0', 'time': '2025-01-11T17:54:00Z'})
        return jsonify({"strategies": strategies_to_send}), 200