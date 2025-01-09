from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import logging

authorized_ip = ["52.89.214.238", "34.212.75.30", "54.218.53.128", "52.32.178.7"]

app = Flask(__name__)
run_with_ngrok(app)  # Active Ngrok pour rendre l'app accessible publiquement

@app.route('/home')
def home():
    # Sert la page HTML avec le tableau
    return render_template('data.html')

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    """
    Endpoint pour recevoir des données du webhook.
    """
    data = request.json  # Récupérer les données JSON envoyées par le webhook
    if request.method == 'POST' and request.headers.get('X-Forwarded-For', request.remote_addr) in authorized_ip:
        # Extrait les données envoyées dans la requête POST (ex: {"nom": "Nouvelle stratégie"})
        data = request.json
        nom = data.get('order_strategy_name')  # Supposons que vous envoyez un champ "nom" dans le JSON

        return '', 200  # Réponse vide avec statut OK
    print(f"Reçu : {data}")  # Afficher les données reçues dans la console
    
    # Répondre au service qui a envoyé le webhook
    return jsonify({"status": "success", "message": "Webhook reçu"}), 200

if __name__ == '__main__':
    print("Application Flask en cours d'exécution...")
    app.run()  # Lance l'application Flask
