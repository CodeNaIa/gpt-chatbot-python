"""
Rotas para o endpoint de chat
"""
from flask import Blueprint, request, jsonify
from chatbot.core import ChatBot

chat_bp = Blueprint("chat", __name__)
chatbot = ChatBot()

@chat_bp.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint para processar mensagens do chat
    
    Request:
        {
            "message": "Sua mensagem aqui"
        }
        
    Response:
        {
            "response": "Resposta do chatbot"
        }
    """
    try:
        data = request.get_json()
        
        if not data or "message" not in data:
            return jsonify({"error": "Mensagem não fornecida"}), 400
            
        message = data["message"]
        response = chatbot.get_response(message)
        
        return jsonify({"response": response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500 