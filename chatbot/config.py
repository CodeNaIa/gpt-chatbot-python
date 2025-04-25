"""
Configurações do chatbot e carregamento de variáveis de ambiente
"""
import os
from dotenv import load_dotenv

def load_config():
    """
    Carrega as configurações do arquivo .env
    """
    load_dotenv()
    
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "FLASK_APP": os.getenv("FLASK_APP", "app.py"),
        "FLASK_ENV": os.getenv("FLASK_ENV", "development"),
        "FLASK_DEBUG": os.getenv("FLASK_DEBUG", "1") == "1",
        "APP_HOST": os.getenv("APP_HOST", "0.0.0.0"),
        "APP_PORT": int(os.getenv("APP_PORT", "5000")),
    } 