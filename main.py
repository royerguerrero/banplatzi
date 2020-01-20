import sys
from collections import deque
from clients import Clients

# Cola para depositos - Se guardaran los number account unicamente
deposit_queue = deque([])
# Cola para apertura de cuentas - Se guardaran los number account unicamente
account_opening_queue = deque([])

def add_to_deposit_queue(number_account):
    deposit_queue.append(number_account)

def add_to_opening_account_queue(name, identification):
    account_opening_queue.append({'name' : name ,'identification' : identification})

def serve_client():
    pass

def list_clients_queues():
    print("Fila de Deposito")
    print(account_opening_queue)
    print("Fila de Apertura de Cuenta")
    print(account_opening_queue)

def _get_input_data(field):
    data = None

    while not data:
        data = input(f'¿Cual es el {field} del cliente?: ')

    return data

def run():

    clients = Clients()
    clients._load_clients()

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
            number_account = _get_input_data('numero de cuenta')
            found = clients.search(number_account)
            if found:
                add_to_deposit_queue(number_account)
            else:
                print(f'EL cliente con numero de cuenta {number_account} no fue encontrado')

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