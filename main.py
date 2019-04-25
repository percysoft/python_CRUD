
import sys


clients = ['pablo', 'ricardo']

# clients = 'pablo,ricardo,'


def crear_cliente(client_name):
  global clients
  
  if(client_name not in clients):
    clients.append(client_name)
    # clients += client_name
    # _add_coma()
  else:
    print('El cliente ya esta en la lista de clientes')
  
def update_client(client_name, update_client_name):
  global clients
  if client_name in clients:
    index = clients.index(client_name)
    clients[index] = update_client_name
    # clients = clients.replace(client_name+ ',', update_client_name)
    list_clients()
  else:
    print('El cliente no se encuentra')

def delete_client(client_name):
  global clients

  if client_name in clients:
    clients.remove(client_name)
    # clients = clients.replace(client_name + ',', '')
    list_clients()
  else:
    print('No se encuentra en la lista')

def search_client(client_name):
  global clients
  # client_list = clients.split(',')

  for client in clients:
    if client != client_name:
      continue
    else:
      return True


def list_clients():
  global clients
  for idx,client in enumerate(clients):
    print('{}:{}'.format(idx,client))
  # print(clients)


# def _add_coma():
#   global clients

#   clients += ','

def pint_welcome():
  print('Welcome a platziventas')
  print('*' * 50)
  print('What would you like today')
  print('[C]reate client')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')

def _get_client_name():
  client_name = None
  while not client_name:
    client_name= input('What is client name: ')

    if client_name == 'exit':
      client_name = None
      break
  if not client_name:
    sys.exit()
  return client_name

if __name__ == '__main__':
  # clients += 'percy'
  pint_welcome()

  command = input()

  if command == 'c':
    client_name = _get_client_name()
    crear_cliente(client_name)
    list_clients()

  elif command == 'd':
    client_name = _get_client_name()
    delete_client(client_name)

  elif command == 'u':
    client_name = _get_client_name()
    update_client_name = input('What is update client name: ')
    update_client(client_name, update_client_name)
  elif command == 's':
    client_name = _get_client_name()
    found = search_client(client_name) 
    if found:
      print('el cliente esta en la lista de clientes')
    else:
      print('No esta en la lista de clientes')
  else:
    print('El comando es invalido.')
