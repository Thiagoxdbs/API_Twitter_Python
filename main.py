# main.py

# Importando a função create_connection do módulo connection
from connection import create_connection
# Importando a função get_data_from_service do módulo services
from services import get_data_from_service

# Função principal para executar a lógica principal do programa
def main():
    # Cria uma conexão com o serviço
    connection = create_connection()
    # Obtém dados usando a conexão criada
    data = get_data_from_service(connection)
    # Imprime os dados obtidos no console
    print(data)

# Verifica se este script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    main()
