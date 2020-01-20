class Client:

    def __init__(self, name, identification, account_number, number_phone, email, balance):
        self.name = name
        self.identification = identification
        self.account_number = account_number
        self.number_phone = number_phone
        self.email = email
        self.balance = balance

class ClientBook:

    def __init__(self):
        self._clients = []

    def add(self, name, identification, account_number, number_phone, email, balance = 0):
        client = Client(name, identification, account_number, number_phone, email, balance)
        self._clients.append(client)

    def show_all(self):
        for client in self._clients:
            print(f'Account Number: {client.account_number} >> Client Name: {client.name} | Client Identificacion: {client.identification} | Client Balance: {client.balance} | Client Number Phone: {client.number_phone} | Client Email: {client.email}')


    def _print_client(self, client):
            print(' --- ' * 10)
            print(f'Account Number: {client.account_number} >> Client Name: {client.name} | Client Identificacion: {client.identification} | Client Number Phone: {client.number_phone} | Client Email: {client.email}')
            print(' --- ' * 10)


    def search(self, account_number):
        for client in self._clients:
            if client.account_number == account_number:
                self._print_client(client)  
                return client
        
        else:
            print(f'The client with account number {account_number} are not found')


    def delete(self, account_number):
        client = self.search(account_number)
        self._clients.remove(client)

    
    def update(self, client, name, identification, account_number, number_phone, email):

        client.name = name
        client.identification = identification
        client.account_number = account_number
        client.number_phone = number_phone
        client.email = email
    

    def deposit(self, client, value):
        client.balance += int(value)

    def withdraw(self, client, value):
        
        withdraw = client.balance - int(value)
        
        if withdraw >= 0:
            client.balance = withdraw
        else:
            print('Underfunding')
        


book = ClientBook()
book.add('Jon', '123', '000', '854278945', 'jfdask@jidfkal')
book.add('Cristian', '456', '159', '854278945', 'jfdask@jidfkal')
book.add('Royer', '798', '753', '854278945', 'jfdask@jidfkal')
book.add('Juan', '014', '486', '854278945', 'jfdask@jidfkal')
book.add('Andres', '025', '777', '854278945', 'jfdask@jidfkal')

book.show_all()

client = book.search('000')

book.deposit(client, 1000)

book.withdraw(client, 100)

book.show_all()