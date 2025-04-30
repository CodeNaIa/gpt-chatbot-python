"""
Lógica principal do chatbot e integração com a API da OpenAI
"""
import os
import openai
from openai.error import APIError, RateLimitError, APIConnectionError

class ChatBot:
    def __init__(self, api_key=None):
        """
        Inicializa o chatbot com a chave da API da OpenAI
        
        Args:
            api_key (str, optional): Chave da API da OpenAI. Se não fornecida, 
                                   será buscada da variável de ambiente OPENAI_API_KEY
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "A chave da API da OpenAI deve ser fornecida através do parâmetro api_key "
                "ou da variável de ambiente OPENAI_API_KEY"
            )
        openai.api_key = self.api_key
        
    def get_response(self, message: str) -> str:
        """
        Obtém uma resposta do GPT-3.5 para a mensagem fornecida
        
        Args:
            message (str): A mensagem do usuário
            
        Returns:
            str: A resposta gerada pelo modelo
            
        Raises:
            Exception: Se houver erro na comunicação com a API
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um assistente útil, amigável e conciso. "
                                 "Responda sempre em português do Brasil."
                    },
                    {"role": "user", "content": message}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
            
        except RateLimitError:
            raise Exception(
                "Limite de uso da API atingido. Por favor, verifique seus créditos na OpenAI "
                "ou aguarde o reset do limite."
            )
        except APIConnectionError:
            raise Exception(
                "Erro de conexão com a API da OpenAI. Por favor, verifique sua conexão com a internet."
            )
        except APIError as e:
            raise Exception(f"Erro na API da OpenAI: {str(e)}")
        except Exception as e:
            raise Exception(f"Erro ao processar a mensagem: {str(e)}") 