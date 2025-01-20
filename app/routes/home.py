from flask import Flask, request, jsonify, render_template, Blueprint, current_app

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    # Sert la page HTML avec le tableau
    return render_template('data.html', strategies = current_app.config['current_alert'])