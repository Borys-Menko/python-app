from flask import Blueprint
from flask import jsonify, current_app, request

main = Blueprint("main", __name__)


@main.route("/status", methods=["GET"])
def get_data():
    redis_client = current_app.extensions['redis_client']
    status = redis_client.get('status').decode("utf-8")
    return jsonify({
        'status': status
    })


@main.route("/status", methods=["POST"])
def set_data():
    redis_client = current_app.extensions['redis_client']
    data = request.get_json()

    redis_client.set('status', str(data['status']))
    return jsonify({'status': 'ok'})


@main.route("/health")
def get_health():
    return jsonify({'status': 'ok'})
