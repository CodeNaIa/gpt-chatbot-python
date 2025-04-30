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
        
    Erros:
        400: Mensagem não fornecida ou inválida
        500: Erro interno do servidor
    """
    try:
        # Validação do JSON
        if not request.is_json:
            return jsonify({"error": "O conteúdo deve ser JSON"}), 400
            
        data = request.get_json()
        
        # Validação da mensagem
        if not data or "message" not in data:
            return jsonify({"error": "O campo 'message' é obrigatório"}), 400
            
        message = data["message"].strip()
        if not message:
            return jsonify({"error": "A mensagem não pode estar vazia"}), 400
            
        # Processamento da mensagem
        response = chatbot.get_response(message)
        
        return jsonify({
            "response": response,
            "status": "success"
        })
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({
            "error": "Erro interno do servidor",
            "details": str(e)
        }), 500 