from flask import Flask, request, jsonify, Blueprint, current_app

webhook_bp = Blueprint('webhook', __name__)

authorized_ip = ["52.89.214.238", "34.212.75.30", "54.218.53.128", "52.32.178.7"]

open_order_count = 0

@webhook_bp.route('/webhook', methods=['POST', 'GET'])
def webhook():
    """
    Endpoint pour recevoir des données du webhook.
    """
    data = request.json  # Récupérer les données JSON envoyées par le webhook
    if request.method == 'POST' and request.headers.get('X-Forwarded-For', request.remote_addr) in authorized_ip:
        # Extrait les données envoyées dans la requête POST (ex: {"nom": "Nouvelle stratégie"})
        data = request.json
        nom = data.get('strategy_order_name')  # Supposons que vous envoyez un champ "nom" dans le JSON
        type = data.get('type')
        position = data.get('position')
        stop_loss = data.get('stop_loss')
        actif = data.get('actif')
        time = data.get('time')
        alert_message = data.get('alert_message')

        print((f"Reçu : " , {'strategy_order_name': nom, 'actif' : actif, 'alert_message': alert_message, 'type': type, 'position' :position, 'stop_loss': stop_loss, 'time':time}))
        if actif == "BNXNEWUSDT.P":
            actif = 'BNXUSDT.P'
        elif actif == "FILECOINUSDT.P":
            actif = "FILUSDT.P"
        if position == "short":
            if type == 'sell':
                type = 'buy'
            elif type == 'buy':
                type = 'sell'
        if position == "flat":
            if "short" in alert_message :
                position = "short"
            if "long" in alert_message :
                position = "long"
            type = 'sell'

        current_app.config['current_alert'].append({'strategy_order_name': nom, 'actif' : actif, 'alert_message': alert_message, 'type': type, 'position' :position, 'stop_loss': stop_loss, 'time':time})
        print(nom)
        print(f"Reçu : " , {'strategy_order_name': nom, 'actif' : actif, 'alert_message': alert_message, 'type': type, 'position' :position, 'stop_loss': stop_loss, 'time':time})  # Afficher les données reçues dans la console
         # Répondre au service qui a envoyé le webhook
        return jsonify({"status": "success", "message": "Webhook reçu"}), 200

    else:
        return jsonify({'status': 'error', 'message': 'Données manquantes'}), 400