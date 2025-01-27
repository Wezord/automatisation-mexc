from flask import request, jsonify, render_template, Blueprint, current_app
import mexc_api as mapi;

rsi_storj_bp = Blueprint('rsi_storj', __name__)

@rsi_storj_bp.route('/rsi_storj', methods=['GET'])
def rsi_storj():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        if current_app.config["current_alert"] == []:
            print("Vide sur rsi_storj")
            return jsonify({"strategies": []}), 200
        else :
            open_position = mapi.get_all_open_position("rsi_storj")
            print("Nombre d'ordre ouvert", len(open_position))
            print(current_app.config["open_position_count"]["rsi_storj"])
            if len(open_position) > current_app.config["open_position_count"]["rsi_storj"]:
                strategies_to_send = [
                    {'strategy_order_name': "rsi_storj", 'type': 'sell', 'position': "long" if actif.split(".")[1] == "2" else "short" ,'alert_message': 'Force Exit', 'actif': actif, 'stop_loss': '0', 'time': '2025-01-11T17:54:00Z'} 
                    for actif in open_position]
                return jsonify({"strategies": strategies_to_send}), 200
            strategies_to_send = []
            for d in current_app.config['current_alert']:
                if d["strategy_order_name"] == "rsi_storj":

                    if  not (
                        (d["type"] == "buy" and  d["position"] == "long" and (d["actif"].split(".")[0] + ".2") in open_position)
                        or 
                        (d["type"] == "buy" and  d["position"] == "short" and (d["actif"].split(".")[0] + ".1") in open_position)
                        or
                        (d["type"] == "sell" and  d["position"] == "long" and (d["actif"].split(".")[0] + ".2") not in open_position)
                        or
                        (d["type"] == "sell" and d["position"] == "short" and (d["actif"].split(".")[0] + ".1") not in open_position)
                    ):
                        strategies_to_send.append(d)
                        if d["type"] == "sell":
                            current_app.config['open_position_count']["rsi_storj"] = current_app.config['open_position_count']["rsi_storj"] - 1
                        elif d["type"] == "buy":
                            current_app.config['open_position_count']["rsi_storj"] = current_app.config['open_position_count']["rsi_storj"] + 1
                    else:
                        current_app.config['current_alert'] = [i for i in current_app.config['current_alert'] if not (d["actif"] == i["actif"] and d["strategy_order_name"] == i["strategy_order_name"] and d["alert_message"] == i["alert_message"])]
                        print("Requête supprimé")
            return jsonify({"strategies": strategies_to_send, "time_coeff" : len(open_position)}), 200
    return render_template('rsi_storj.html', strategies = current_app.config['current_alert'])