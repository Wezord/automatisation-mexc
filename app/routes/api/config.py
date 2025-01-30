from flask import request, jsonify, Blueprint, current_app

config_bp = Blueprint('config', __name__)

@config_bp.route('/config', methods=['GET'])
def config():
    if request.method == "GET":
        return jsonify({"strategies": current_app.config["list_strategy"]}), 200