'''
    MANEJO DE EXCEPCIONES PARA SOCKETS.
'''

#Librerías necesarias.
import socket
import sys

host = '127.0.0.1'
port = 80

try: #Falla en la creación del socket.
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(mysocket)
    mysocket.settimeout(5)
except socket.error as e:
    print('Socket create error: %s' %str(e.__class__))
    sys.exit(1)

try: 
    mysocket.connect((host, port))
    print(mysocket)
except socket.timeout as e: #Nos pasamos del tiempo establecido
    print('Timeout %s' %e)
    sys.exit(1)
except socket.gaierror as e: #Devuelve un error por el servidor.
    print('Connection error to the server: %s' %e)
    sys.exit(1)
except socket.error as e: #Ninguna de las otras excepciones. Se imprime el error obtenido.
    print('Connection error: %s' %e)
    sys.exit(1)