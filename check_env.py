"""
Script para verificar a configuração do ambiente
"""
import os
from dotenv import load_dotenv

def check_env():
    """
    Verifica se o arquivo .env está configurado corretamente
    """
    print("Verificando configuração do ambiente...")
    
    # Verifica se o arquivo .env existe
    if not os.path.exists(".env"):
        print("ERRO: Arquivo .env não encontrado!")
        print("Por favor, crie um arquivo .env baseado no .env.example")
        return False
        
    # Carrega as variáveis de ambiente
    load_dotenv()
    
    # Verifica a chave da API
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERRO: OPENAI_API_KEY não encontrada no arquivo .env!")
        return False
    elif api_key == "your_api_key_here":
        print("ERRO: OPENAI_API_KEY não foi configurada!")
        print("Por favor, substitua 'your_api_key_here' pela sua chave real da API")
        return False
        
    print("✓ Arquivo .env encontrado")
    print("✓ OPENAI_API_KEY configurada")
    print("\nConfiguração do ambiente está correta!")
    return True

if __name__ == "__main__":
    check_env() 