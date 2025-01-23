from flask_ngrok import run_with_ngrok
from app import create_app

app = create_app()
run_with_ngrok(app)  # Active Ngrok pour rendre l'app accessible publiquement

if __name__ == '__main__':
    print("Application Flask en cours d'exécution...")
    app.run()  # Lance l'application Flask