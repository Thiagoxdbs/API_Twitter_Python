# services.py

# Importando os módulos e constantes necessários
from constants import API_URL
from secrets import API_KEY
import requests

# Função para obter dados de um serviço usando a conexão fornecida
def get_data_from_service(connection):
    # Faz uma solicitação GET à API com a chave da API nos cabeçalhos
    response = requests.get(API_URL, headers={"Authorization": f"Bearer {API_KEY}"})
    # Retorna a resposta em formato JSON
    return response.json()
