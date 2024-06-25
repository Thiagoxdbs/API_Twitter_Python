# responses.py

# Função para criar uma resposta de sucesso com os dados fornecidos
def success_response(data):
    return {"status": "success", "data": data}

# Função para criar uma resposta de erro com uma mensagem fornecida
def error_response(message):
    return {"status": "error", "message": message}
