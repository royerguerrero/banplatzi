import sys
from collections import deque
from clients import Clients

# Cola para depositos - Se guardaran los number account unicamente
deposit_queue = deque([])
# Cola para apertura de cuentas - Se guardaran los number account unicamente
account_opening_queue = deque([])

def add_to_deposit_queue():
    pass

def add_to_opening_account_queue(name, identification):
    account_opening_queue.append({'name' : name ,'identification' : identification})

def serve_client():
    pass

def list_clients_queues():
    print("Fila de Deposito")
    print("Fila de Apertura de Cuenta")
    print(account_opening_queue)

def _get_input_data(field):
    data = None

    while not data:
        data = input(f'¿Cual es el {field} del cliente?: ')

    return data

def run():
    while True:
        command = str(input('''
        Bienvenido, a BanPlatzi tu app de gestion de filas de tu banco

        [A]Agregar cliente a fila de deposito
        [B]Agregar cliente a fila de apertura de cuenta
        [C]Atender cliente
        [D]Listar clientes en fila
        [S]Salir
        ''')).lower()
    
        if command == 'a':
            pass
        elif command == 'b':
            name = _get_input_data('nombre')
            identification = _get_input_data('identificacion')
            add_to_opening_account_queue(name, identification)
        elif command == 'c':
            pass
        elif command == 'd':
            list_clients_queues()
        elif command == 's':
            print('Saliendo...')
            sys.exit()
        else:
            print('Comando invalido, vuelve a intentar.')
    

    

if __name__ == "__main__":
    print('''
__________              __________.__          __         .__ 
\______   \_____    ____\______   \  | _____ _/  |________|__|
 |    |  _/\__  \  /    \|     ___/  | \__  \\   __\___   /  |
 |    |   \ / __ \|   |  \    |   |  |__/ __ /|  |  /  __/|  |
 |______  /(____  /___|  /____|   |____(____  /__| /_____ \__|
        \/      \/     \/                   \/           \/       
    
    ''')
    run()