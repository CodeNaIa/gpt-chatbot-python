"""
Configurações do chatbot e carregamento de variáveis de ambiente
"""
import os
from dotenv import load_dotenv

def load_config():
    """
    Carrega as configurações do arquivo .env
    
    Returns:
        dict: Dicionário com as configurações carregadas
        
    Raises:
        ValueError: Se a chave da API não estiver configurada
    """
    # Garante que o .env seja carregado
    load_dotenv()
    
    # Verifica se a chave da API está configurada
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "A chave da API da OpenAI (OPENAI_API_KEY) não foi encontrada no arquivo .env. "
            "Por favor, verifique se o arquivo .env existe e contém a chave correta."
        )
    
    return {
        "OPENAI_API_KEY": api_key,
        "FLASK_APP": os.getenv("FLASK_APP", "app.py"),
        "FLASK_ENV": os.getenv("FLASK_ENV", "development"),
        "FLASK_DEBUG": os.getenv("FLASK_DEBUG", "1") == "1",
        "APP_HOST": os.getenv("APP_HOST", "0.0.0.0"),
        "APP_PORT": int(os.getenv("APP_PORT", "5000")),
    } 