import os
import json
from pgadmin.utils import get_storage_directory
from pgadmin.utils.crypto import decrypt
from pgadmin.model import Server

# Carrega os servers do arquivo JSON
def load_servers():
    with open('/pgadmin4/servers.json', 'r') as f:
        servers_data = json.load(f)
    
    storage_dir = get_storage_directory()

    # Adiciona cada servidor
    for server_id, server in servers_data['Servers'].items():
        try:
            new_server = Server(
                name=server['Name'],
                group=server['Group'],
                host=server['Host'],
                port=server['Port'],
                maintenance_db=server['MaintenanceDB'],
                username=server['Username'],
                password=decrypt(server['Password']), # Descriptografar a senha
                ssl_mode=server['SSLMode']
            )
            new_server.save()

            print(f"Servidor '{server['Name']}' adicionado com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar o servidor: {e}")

# Executa a inicialização do pgAdmin
if __name__ == '__main__':
    load_servers()
