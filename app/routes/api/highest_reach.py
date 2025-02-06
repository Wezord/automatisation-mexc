from flask import request, jsonify, Blueprint, current_app
import json, os

highest_reach_bp = Blueprint('highest_reach', __name__)

@highest_reach_bp.route('/highest_reach', methods=['GET', 'POST'])
def highest_reach():
    if request.method == "GET":
        return jsonify({'highest_reach' : current_app.config['highest_reach'][request.args.get("strategy")]}), 200
    elif request.method == "POST":
        data = request.get_json()
        quantite = data.get("quantite")
        strategy = data.get("strategy")
        if quantite > current_app.config["highest_reach"]:
            print("New value for ", strategy, quantite)
            config_path = os.path.join("app/config.json")
            with open(config_path, 'w', encoding='utf-8') as f:
                config_data = json.load(f)
                config_data["highest_reach"] = current_app.config["highest_reach"]
                json.dump(config_data, f, ensure_ascii=False, indent=4)