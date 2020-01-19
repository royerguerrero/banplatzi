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

        print(command)

    

if __name__ == "__main__":
    print('''
__________              __________.__          __         .__ 
\______   \_____    ____\______   \  | _____ _/  |________|__|
 |    |  _/\__  \  /    \|     ___/  | \__  \\   __\___   /  |
 |    |   \ / __ \|   |  \    |   |  |__/ __ \|  |  /    /|  |
 |______  /(____  /___|  /____|   |____(____  /__| /_____ \__|
        \/      \/     \/                   \/           \/       
    
    ''')
    run()
    