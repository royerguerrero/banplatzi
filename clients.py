class Client:

    def __init__(self, name, identification, account_number, number_phone, email):
        self.name = name
        self.identification = identification
        self.account_number = account_number
        self.number_phone = number_phone
        self.email = email

class ClientBook:

    def __init__(self):
        self._clients = []

    def add(self, name, identification, account_number, number_phone, email):
        client = Client(name, identification, account_number, number_phone, email)
        self._clients.append(client)

    def show_all(self):
        for client in self._clients:
            print(f'Account Number: {client.account_number} >> Client Name: {client.name} | Client Identificacion: {client.identification} | Client Number Phone: {client.number_phone} | Client Email: {client.email}')


    def _print_client(self, client):
            print(' --- ' * 10)
            print(f'Account Number: {client.account_number} >> Client Name: {client.name} | Client Identificacion: {client.identification} | Client Number Phone: {client.number_phone} | Client Email: {client.email}')


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

    # TODO: La funcion no esta remplazando esta añadiendo el cliente???
    def update(self, account_number, updated_name, updated_identification, updated_account_number, updated_number_phone, updated_email):
        client = self.search(account_number)

        client.name = updated_name
        client.identification = updated_identification
        client.account_number = updated_account_number
        client.number_phone = updated_number_phone
        client.email = updated_email



book = ClientBook()
book.add('Jon', '123', '000', '854278945', 'jfdask@jidfkal')
book.add('Cristian', '456', '159', '854278945', 'jfdask@jidfkal')
book.add('Royer', '798', '753', '854278945', 'jfdask@jidfkal')
book.add('Juan', '014', '486', '854278945', 'jfdask@jidfkal')
book.add('Andres', '025', '777', '854278945', 'jfdask@jidfkal')

book.show_all()


book.update('000', 'Peter', '132', '123', '789', 'peter@mail.com')

book.show_all()