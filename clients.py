import csv
import os

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
        self.CLIENT_FILE = '.clients.csv'

    def _save_clients(self):
        with open(self.CLIENT_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            
            for client in self._clients:
                writer.writerow( (client.name, client.identification, client.account_number, client.number_phone, client.email, client.balance) )

    def _load_clients(self):
        with open(self.CLIENT_FILE, mode='r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue

                self.add(row[0], row[1], row[2], row[3], row[4], row[5])

    def add(self, name, identification, account_number, number_phone, email, balance = 0):
        client = Client(name, identification, account_number, number_phone, email, int(balance))
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
        