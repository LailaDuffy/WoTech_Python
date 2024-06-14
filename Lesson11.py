import datetime
import json

class Client:
  pass # means nothing happens
  number_of_clients = 0

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.accounts = []
    Client.number_of_clients += 1

  # adding an account for a client method
  def add_account(self, account):
    self.accounts.append(account)

  # method to add data to dictionary
  def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'accounts': [account.to_dict() for account in self.accounts]
        }

class Account:
  def __init__(self, number, currency, balance = 0.0): # balance = 0.0 gives a defualt value and makes the argument optional
    self.number = number
    self.currency = currency
    self.balance = balance
    self.transactions = []

  def make_deposit(self, amount, note):
    self.transactions.append(Transaction(self.currency, amount, note))
    self.balance += amount

  def make_withdrawal(self, amount, note):
    self.transactions.append(Transaction(self.currency, -amount, note))
    if (self.balance > amount):
      self.balance -= amount
    else:
      print('Insufficient balance!')
    
  def to_dict(self):
        return {
            'number': self.number,
            'currency': self.currency,
            'balance': self.balance,
            'transactions': [transaction.to_dict() for transaction in self.transactions]
        }

class Transaction:
  def __init__(self, currency, amount, note):
    self.currency = currency
    self.amount = amount
    self.note = note
    self.time_stamp = datetime.datetime.now()

  def to_dict(self):
        return {
            'currency': self.currency,
            'amount': self.amount,
            'note': self.note,
            'time_stamp': self.time_stamp.isoformat()
        }

# creating a list for clients and adding new clients
clients = []
clients.append(Client('100001', 'Anna'))
clients.append(Client('100002', 'Oskars'))
clients.append(Client('100003', 'Jennifer'))

print(f'The total number of clients: {Client.number_of_clients}')

# accessing Oskars id
print(f'Client Oskars ID: {clients[1].id}')

# accessing every clients name
for client in clients:
  print(f'Client name: {client.name}')

# creating and adding an account for a each client
clients[0].add_account(Account('EE547852366654', 'EUR', 1000.00))
clients[0].add_account(Account('JP568768458466', 'JPY', 25000.00))
clients[0].add_account(Account('US447589005252', 'USD'))

clients[1].add_account(Account('PL444400010016', 'PLN', 47800.00))
clients[1].add_account(Account('SE656565640401', 'SEK', 200.18))

clients[2].add_account(Account('FR444779898980', 'EUR'))

# printing out each client and their list of accounts
for client in clients:
  print(f'{client.name} has the following accounts: ')
  for account in client.accounts:
    print(f'  {account.number} ({account.currency}), balance: {account.balance}')

# make transactions
clients[0].accounts[0].make_deposit(1200, 'salary')
clients[0].accounts[0].make_withdrawal(50, 'groceries')
clients[0].accounts[0].make_withdrawal(140, 'clothes')
clients[0].accounts[0].make_withdrawal(20, 'dinner')

for client in clients:
  print(f'{client.name}')
  for account in client.accounts:
    print(f'    {account.number}')
    for transaction in account.transactions:
      print(f'      {transaction.time_stamp} {transaction.amount} {transaction.currency}')


# Collect all client data into a dictionary
clients_data = [client.to_dict() for client in clients]

# Save the data to a JSON file
with open("clients_data.json", "w") as outfile:  #"sample.json" as filename, "w" as mode of file - write mode 
    json.dump(clients_data, outfile, indent=4)

# reading JSON into a dictionary
import json

# Opening JSON file
with open('clients_data.json') as json_file:
  data = json.load(json_file)

# printing client name
for client in data:
  print(f'{client["name"]} ({client["id"]})')
