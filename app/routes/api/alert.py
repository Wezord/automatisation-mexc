from flask import Flask, request, jsonify, render_template, Blueprint, current_app

alert_bp = Blueprint('alert', __name__)

@alert_bp.route('/alert', methods=['GET'])
def alert():
    if request.method == "GET":
        return jsonify({"strategies": current_app.config['current_alert']}), 200