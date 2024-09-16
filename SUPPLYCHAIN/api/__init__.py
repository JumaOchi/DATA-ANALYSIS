from flask import Flask
from api.routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Register the blueprint for API routes
    app.register_blueprint(api_bp)
    
    return app


