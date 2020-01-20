import sys
from collections import deque
from clients import Clients

# Cola para depositos - Se guardaran los number account unicamente
deposit_queue = deque([])
# Cola para apertura de cuentas - Se guardaran los number account unicamente
account_opening_queue = deque([])


def add_to_deposit_queue(number_account, depositor_name, depositor_uid):
    deposit_queue.append({'number_account' : number_account, 'depositor_name' : depositor_name, 'depositor_uid' : depositor_uid})


def add_to_opening_account_queue(name, identification):
    account_opening_queue.append({'name' : name ,'identification' : identification})


def list_clients_queues():
    print("Fila de Deposito")
    for idx, client in enumerate(deposit_queue):
        print('idx: {} >> Nombre del depositante: {} - Identificado con C.C N° {} | Numero de cuenta a depositar: {}'.format((idx + 1), client['depositor_name'], client['depositor_uid'], client['number_account']))
    print("Fila de Apertura de Cuenta")
    for idx, client in enumerate(account_opening_queue):
        print('idx: {} >> Nombre del futuro cliente: {} - Identificado con C.C N° {}'.format((idx + 1), client['name'], client['identification']))
        

def _get_input_data(field):
    data = None

    while not data:
        data = input(f'Cual es el {field} ')

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
            depositor_name = _get_input_data('nombre del depositante')
            depositor_uid = _get_input_data('numero de identificaion del depositante')
            number_account = _get_input_data('numero de cuenta del cliente')
            found_account = clients.search(number_account)
            if found_account:
                add_to_deposit_queue(number_account, depositor_name, depositor_uid)
            else:
                print(f'La cuenta numero {number_account}, no fue encontrada')


        elif command == 'b':
            name = _get_input_data('nombre del cliente')
            identification = _get_input_data('identificacion de cliente')
            add_to_opening_account_queue(name, identification)
        elif command == 'c':
            queue = input('''
            Elije que fila deseas atender :
            [A] Fila de Depositos
            [B] Fila de Apertura de Cuenta
            ''').lower()

            print('Siguiente Cliente...')
            if queue == 'a':
                try:
                    print('Cliente a atender >> Nombre del depositante: {} - Identificado con C.C N° {} | Numero de cuenta a depositar: {}'.format(deposit_queue[0]['depositor_name'], deposit_queue[0]['depositor_uid'], deposit_queue[0]['number_account']))
                    value = _get_input_data('monto a consignar, no incluyas puntos ni comas - $ ')
                    client = clients.search(deposit_queue[0]['number_account'])

                    clients.deposit(client, value)
                    deposit_queue.popleft()

                except IndexError:
                    print('La fila de Depositos no tiene clientes')

            elif queue == 'b':
                try:
                    print('Cliente a atender >> Nombre del futuro cliente: {} - Identificado con C.C N° {}'.format(account_opening_queue[0]['name'], account_opening_queue[0]['identification']))

                    account_number = _get_input_data('numero de cuenta: ')
                    number_phone = _get_input_data('numero de telefono del cliente: ')
                    email = _get_input_data('email del cliente: ')

                    clients.add(account_opening_queue[0]['name'], account_opening_queue[0]['identification'], account_number, number_phone, email)
                    account_opening_queue.popleft()
                except IndexError:
                    print('La fila de Apertura de clientes no tiene clientes')


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