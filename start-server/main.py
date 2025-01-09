from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import logging

app = Flask(__name__)
run_with_ngrok(app)  # Active Ngrok pour rendre l'app accessible publiquement

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    """
    Endpoint pour recevoir des données du webhook.
    """
    data = request.json  # Récupérer les données JSON envoyées par le webhook
    print(f"Reçu : {data}")  # Afficher les données reçues dans la console
    
    # Répondre au service qui a envoyé le webhook
    return jsonify({"status": "success", "message": "Webhook reçu"}), 200

if __name__ == '__main__':
    print("Application Flask en cours d'exécution...")
    app.run()  # Lance l'application Flask
