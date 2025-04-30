"""
Entrypoint da aplicação Flask
"""
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente antes de qualquer importação
load_dotenv()

from flask import Flask
from routes.chat import chat_bp
from chatbot.config import load_config

def create_app():
    """
    Cria e configura a aplicação Flask
    """
    app = Flask(__name__)
    
    # Carrega as configurações
    config = load_config()
    app.config.update(config)
    
    # Registra os blueprints
    app.register_blueprint(chat_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(
        host=app.config["APP_HOST"],
        port=app.config["APP_PORT"],
        debug=app.config["FLASK_DEBUG"]
    ) 