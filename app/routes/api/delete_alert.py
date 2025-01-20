from flask import Flask, request, jsonify, render_template, Blueprint, current_app

delete_alert_bp = Blueprint('delete_alert', __name__)

@delete_alert_bp.route('/delete_alert', methods=['POST'])
def delete_alert():
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Données manquantes ou mal formatées"}), 400
        
        action = data.get("action")
        value = data.get("alerte")

        if action == "delete":
            current_app.config['current_alert'] = [d for d in current_app.config['current_alert'] if not (d["actif"] == value["actif"] and d["strategy_order_name"] == value["strategy_order_name"] and d["alert_message"] == value["alert_message"])]
        
        elif action == "delete_all":
            current_app.config['current_alert'] = [d for d in current_app.config['current_alert'] if not d["strategy_order_name"] == value]

        return jsonify({"message": "Alerte supprimé"}), 200