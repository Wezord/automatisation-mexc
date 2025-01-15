from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import logging

authorized_ip = ["52.89.214.238", "34.212.75.30", "54.218.53.128", "52.32.178.7"]

#current_alert = [{'strategy_order_name': 'moving', 'type': 'buy', 'position': 'long', 'alert_message': 'Entry long', 'actif': 'UNIUSDT.P', 'stop_loss': '0', 'time': '2025-01-14T15:20:00Z'},
 #                {'strategy_order_name': 'moving', 'type': 'buy', 'position': 'long', 'alert_message': 'Entry long', 'actif': 'CELRUSDT.P', 'stop_loss': '0', 'time': '2025-01-14T15:20:00Z'}]

current_alert = []

app = Flask(__name__)
run_with_ngrok(app)  # Active Ngrok pour rendre l'app accessible publiquement

@app.route('/home')
def home():
    # Sert la page HTML avec le tableau
    return render_template('data.html', strategies = current_alert)

@app.route('/rsi')
def larry():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_alert if d["strategy_order_name"] == "rsi"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('rsi.html', strategies = current_alert)

@app.route('/moving')
def moving():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_alert if d["strategy_order_name"] == "moving"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('moving.html', strategies = current_alert)

@app.route('/x3')
def x3():
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_alert if d["strategy_order_name"] == "x3"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('x3.html', strategies = current_alert)

@app.route('/bollinger')
def bollinger():
    global current_alert
    if request.method == "GET" and request.headers.get("X-Custom-Message") == "get_alert":
        strategies_to_send = [d for d in current_alert if d["strategy_order_name"] == "bollinger"]
        return jsonify({"strategies": strategies_to_send}), 200
    return render_template('bollinger.html', strategies = current_alert)

@app.route('/delete_alert', methods=['POST'])
def delete_alert():
    global current_alert
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Données manquantes ou mal formatées"}), 400
        
        action = data.get("action")
        value = data.get("alerte")

        if action == "delete":
            current_alert = [d for d in current_alert if not (d["actif"] == value["actif"] and d["strategy_order_name"] == value["strategy_order_name"] and d["stop_loss"] == value["stop_loss"])]

        return jsonify({"message": "Alerte supprimé"}), 200

@app.route('/alert', methods=['GET'])
def alert():
    if request.method == "GET":
        return jsonify({"strategies": current_alert}), 200


@app.route('/webhook', methods=['POST', 'GET'])
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
        if "Exit" in alert_message:
            type = 'sell'
        current_alert.append({'strategy_order_name': nom, 'actif' : actif, 'alert_message': alert_message, 'type': type, 'position' :position, 'stop_loss': stop_loss, 'time':time})
        print(nom)
        print(f"Reçu : " , {'strategy_order_name': nom, 'actif' : actif, 'alert_message': alert_message, 'type': type, 'position' :position, 'stop_loss': stop_loss, 'time':time})  # Afficher les données reçues dans la console
         # Répondre au service qui a envoyé le webhook
        return jsonify({"status": "success", "message": "Webhook reçu"}), 200

    else:
        return jsonify({'status': 'error', 'message': 'Données manquantes'}), 400

if __name__ == '__main__':
    print("Application Flask en cours d'exécution...")
    app.run()  # Lance l'application Flask