from collections import deque
from clients import Clients

# Cola para depositos
deposit_queue = deque([])
# Cola para apertura de cuentas
account_opening_queue = deque([])

def add_to_deposit_queue():
    pass

def add_to_opening_account_queue():
    pass

def serve_client():
    pass

def list_clients_queues():
    pass


def run():
    while True:
        command = str(input('''
Bienvenido, a BanPlatzi tu app de gestion de filas de tu banco

    [A]Agregar cliente a fila de depósito
    [B]Agregar cliente a fila de apertura de cuenta
    [C]Atender cliente
    [D]Listar clientes en fila
    [S]Salir
    ''')).lower()
    
    return command

    

if __name__ == "__main__":
    print('''
__________              __________.__          __         .__ 
\______   \_____    ____\______   \  | _____ _/  |________|__|
 |    |  _/\__  \  /    \|     ___/  | \__  \\   __\___   /  |
 |    |   \ / __ \|   |  \    |   |  |__/ __ /|  |  /  __/|  |
 |______  /(____  /___|  /____|   |____(____  /__| /_____ \__|
        \/      \/     \/                   \/           \/       
    
    ''')
    command = run()

    if command == 'a':
        pass
    elif command == 'b':
        pass
    elif command == 'c':
        pass
    elif command == 'd':
        pass
    else:
        print('Comando invalido, vuelve a intentar.')
    