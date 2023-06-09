from flask import Flask

from flask_redis import FlaskRedis


# https://github.com/underyx/flask-redis/
redis_client = FlaskRedis()


def create_app():
    app = Flask(__name__)

    redis_client = FlaskRedis()
    redis_client.init_app(app)

    app.extensions['redis_client'] = redis_client

    from project.routes import main
    app.register_blueprint(main)

    return app
