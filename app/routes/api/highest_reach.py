from flask import request, jsonify, Blueprint, current_app
import json, os, math, re

highest_reach_bp = Blueprint('highest_reach', __name__)

@highest_reach_bp.route('/highest_reach', methods=['GET', 'POST'])
def highest_reach():
    if request.method == "GET":
        return jsonify({'highest_reach' : current_app.config['highest_reach'][0][request.args.get("strategy")]}), 200
    elif request.method == "POST":
        data = request.get_json()
        quantite = data.get("quantite")

        cleaned_num_str = re.sub(r'[^\d.]', '', quantite)
        quantite = float(cleaned_num_str)

        strategy = data.get("strategy")
        if quantite > current_app.config["highest_reach"][0][strategy]:
            print("New value for ", strategy, quantite)
            config_path = os.path.join("app/config.json")
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                current_app.config["highest_reach"] = config_data["highest_reach"]
            current_app.config["highest_reach"][0][strategy] = quantite
            with open(config_path, 'w', encoding='utf-8') as f:
                config_data["highest_reach"] = current_app.config["highest_reach"]
                json.dump(config_data, f, ensure_ascii=False, indent=4)
            return jsonify({'quantite' : math.floor(quantite/current_app.config['coeff_simu'][0][strategy])}), 200
        return jsonify({'quantite' : math.floor(current_app.config['highest_reach'][0][strategy]/current_app.config['coeff_simu'][0][strategy])}), 200
    return jsonify({'Response' : "Not good method"}), 400