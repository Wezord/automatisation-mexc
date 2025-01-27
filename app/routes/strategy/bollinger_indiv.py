from flask import Flask, request, jsonify, render_template, Blueprint, current_app
import mexc_api as mapi;

bollinger_indiv_bp = Blueprint('bollinger_indiv', __name__)

@bollinger_indiv_bp.route('/bollinger_indiv', methods=['GET'])
def bollinger_indiv():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        if current_app.config["current_alert"] == []:
            print("Vide sur bollinger_indiv")
            return jsonify({"strategies": []}), 200
        else :
            open_position = mapi.get_all_open_position("bollinger_indiv")
            print("Nombre d'ordre ouvert", len(open_position))
            print(current_app.config["open_position_count"]["bollinger_indiv"])
            if len(open_position) > current_app.config["open_position_count"]["bollinger_indiv"]:
                strategies_to_send = [
                    {'strategy_order_name': "bollinger_indiv", 'type': 'sell', 'position': "long" if actif.split(".")[1] == "2" else "short" ,'alert_message': 'Force Exit', 'actif': actif, 'stop_loss': '0', 'time': '2025-01-11T17:54:00Z'} 
                    for actif in open_position]
                return jsonify({"strategies": strategies_to_send}), 200
            strategies_to_send = []
            for d in current_app.config['current_alert']:
                if d["strategy_order_name"] == "bollinger_indiv":

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
                            current_app.config['open_position_count']["bollinger_indiv"] = current_app.config['open_position_count']["bollinger_indiv"] - 1
                        elif d["type"] == "buy":
                            current_app.config['open_position_count']["bollinger_indiv"] = current_app.config['open_position_count']["bollinger_indiv"] + 1
                    else:
                        current_app.config['current_alert'] = [i for i in current_app.config['current_alert'] if not (d["actif"] == i["actif"] and d["strategy_order_name"] == i["strategy_order_name"] and d["alert_message"] == i["alert_message"])]
                        print("Requête supprimé")
            return jsonify({"strategies": strategies_to_send, "time_coeff" : len(open_position)}), 200
    return render_template('bollinger_indiv.html', strategies = current_app.config['current_alert'])