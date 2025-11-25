from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Import and register blueprints
    from .views import bp
    app.register_blueprint(bp)

    return app
