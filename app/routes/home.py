from flask import render_template, Blueprint, current_app

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    return render_template('home.html', strategies = current_app.config['current_alert'])