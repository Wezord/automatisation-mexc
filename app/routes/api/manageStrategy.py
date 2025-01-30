from flask import request, jsonify, Blueprint, current_app
import json, os

add_strategy_bp = Blueprint('add_strategy', __name__)
del_strategy_bp = Blueprint('del_strategy', __name__)

from flask import jsonify, current_app, request
import json

@add_strategy_bp.route('/add_strategy', methods=['GET'])
def add_strategy():
    if request.method == "GET" and request.args.get('strategy') is not None:
        list_strategy = current_app.config["list_strategy"]
        list_strategy.append(request.args.get('strategy'))
        current_app.config["list_strategy"] = list_strategy
        strategy = [
            {"value": strat, "label": strat} for strat in list_strategy
        ]
        config_path = os.path.join("app/config.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump({"strategy": strategy}, f, ensure_ascii=False, indent=4)
        return jsonify({"message": "Strategy ajouté"}), 200
    return jsonify({"message": "Erreur"}), 500

@add_strategy_bp.route('/del_strategy', methods=['GET'])
def del_strategy():
    if request.method == "GET" and request.args.get('strategy') != None:
        strategy = [
        {"value": strat , "label": strat} for strat in current_app.config["list_strategy"] if not strat == request.args.get('strategy')
        ]
        current_app.config["list_strategy"] = [
            strat for strat in current_app.config["list_strategy"] if not strat == request.args.get('strategy')
        ]
        config_path = os.path.join("app/config.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(strategy, f, ensure_ascii=False, indent=4)
        return jsonify({"message": "Strategy ajouté"}), 200
    
    return jsonify({"message": "Erreur"}), 500