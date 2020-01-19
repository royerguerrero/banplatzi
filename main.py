from collections import deque

# Cola para depositos
deposit_queue = deque([])

# Cola para apertura de cuentas

account_opening_queue = deque([])


clients = [
    {
        name: 'Andres Garcia',
        identification: '5328373',
        account_number: '032451453'
    }
    {
        name : 'Royer Guerrero'
        identification : '12359812',
        account_number: '153020'
    }
]

# El parametro por defecto es el, por si se desea preguntar un valor que sea 'la' se le debe pasar a la funcion
def _get_input(placeholder, syntax = 'el'):

    data = input(f'Cual es {syntax} {placeholder}: ')
    return data

def _get_all_client_schema():
    client = {}
    client['name'] = _get_input('nombre')
    client['']


#Función de agregar cliente a fila de depósito
def add_client():
    pass

def delete_client()
    pass

#Función de agregar cliente a fila de apertura de cuenta
def move_client_account_opening():
    pass

#Función de atender cliente
def attend_client():
    pass

#Función de listar clientes en fila
def list_clients():
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
        
    elif command == 'b':
        pass
    elif command == 'c':
        pass
    elif command == 'd':
        pass
    else:
        print('Comando invalido, vuelve a intentar.')
    