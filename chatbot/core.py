"""
Lógica principal do chatbot e integração com a API da OpenAI
"""
import os
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key=None):
        """
        Inicializa o chatbot com a chave da API da OpenAI
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        
    def get_response(self, message: str) -> str:
        """
        Obtém uma resposta do GPT-3.5 para a mensagem fornecida
        
        Args:
            message (str): A mensagem do usuário
            
        Returns:
            str: A resposta gerada pelo modelo
        """
        try:
            # Mock da resposta enquanto não há chave da API
            if not self.api_key:
                return f"Resposta mock para: {message}"
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente útil e amigável."},
                    {"role": "user", "content": message}
                ]
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Erro ao processar a mensagem: {str(e)}" 