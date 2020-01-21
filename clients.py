import csv
import random

class Client:

    def __init__(self, name, identification, account_number, number_phone, email, balance):
        self.name = name
        self.identification = identification
        self.account_number = account_number
        self.number_phone = number_phone
        self.email = email
        self.balance = balance

class Clients:

    def __init__(self):
        self._clients = []
        self.CLIENT_FILE = '.clients.csv'

    def _save_clients(self):
        with open(self.CLIENT_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            
            for client in self._clients:
                writer.writerow( (client.name, client.identification, client.account_number, client.number_phone, client.email, client.balance) )

    def _load_clients(self):
        with open(self.CLIENT_FILE, mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self._add_with_account_number(row[0], row[1], row[2], row[3], row[4], row[5])

    def _generate_account_number(self):
        account_number = random.randint(11111, 99999)

        validate_existence = self.search(account_number)

        if not validate_existence:
            return account_number
        else:
            self._generate_account_number()

    def _add_with_account_number(self, name, identification, account_number, number_phone, email, balance = 0):
        client = Client(name, identification, account_number, number_phone, email, int(balance))
        self._clients.append(client)
        self._save_clients()

    def add(self, name, identification, number_phone, email, balance = 0):
        account_number = self._generate_account_number()
        client = Client(name, identification, account_number, number_phone, email, int(balance))
        self._clients.append(client)
        self._save_clients()

    def show_all(self):
        for client in self._clients:
            print(f'Account Number: {client.account_number} >> Client Name: {client.name} | Client Identificacion: {client.identification} | Client Balance: {client.balance} | Client Number Phone: {client.number_phone} | Client Email: {client.email}')


    def _print_client(self, client):
            print(' --- ' * 10)
            print(f'Account Number: {client.account_number} >> Client Name: {client.name} | Client Identificacion: {client.identification} | Client Balance: {client.balance} | Client Number Phone: {client.number_phone} | Client Email: {client.email}')
            print(' --- ' * 10)


    def search(self, account_number):
        for client in self._clients:
            if client.account_number == account_number:
                #self._print_client(client)  
                return client
        
        else:
            return False


    def delete(self, account_number):
        client = self.search(account_number)
        self._clients.remove(client)

    
    def update(self, client, name, identification, number_phone, email):
        client.name = name
        client.identification = identification
        client.number_phone = number_phone
        client.email = email
    

    def deposit(self, client, value):
        client.balance += int(value)
        self._save_clients()

    def withdraw(self, client, value):
        
        withdraw = client.balance - int(value)
        
        if withdraw >= 0:
            client.balance = withdraw
        else:
            print('Underfunding')
        