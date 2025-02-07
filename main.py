from flask_ngrok import run_with_ngrok
from app import create_app

app = create_app()
run_with_ngrok(app)  # Active Ngrok pour rendre l'app accessible publiquement

# Planificateur de tâche pour vider la temp alerte toutes les X minutes
from apscheduler.schedulers.background import BackgroundScheduler
import time

def emptyCache():
    app.config['temp_current_alert'] = []

# Initialiser le planificateur de tâches en arrière-plan
scheduler = BackgroundScheduler()

# Ajouter la tâche planifiée (exécuter toutes les X minutes, par exemple 5 minutes)
scheduler.add_job(emptyCache, 'interval', minutes=30)

# Assurez-vous que le planificateur s'arrête correctement lorsque l'application s'arrête
# push context manually to app
with app.app_context():
    if not scheduler.running:
        scheduler.start()

@app.teardown_appcontext
def shutdown_scheduler(exception=None):
    # Vérifiez si le planificateur est en cours d'exécution avant d'essayer de l'arrêter
    if scheduler.running:
        scheduler.shutdown()

if __name__ == '__main__':
    print("Application Flask en cours d'exécution...")
    app.run()  # Lance l'application Flask