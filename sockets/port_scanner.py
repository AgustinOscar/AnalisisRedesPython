#Librerías necesarias.
import socket
import sys

#Ejemplo del escaneo de diferentes puertos.

#IP del localhost.
ip = '127.0.0.1'
portList = [21, 22, 23, 80]

#Función para determinar qué puertos están abiertos.
def check_ports(ip, portList):
    try:
        for port in portList:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #Si en 5 seg no se establece la comunicación, detiene el socket.
            sock.settimeout(5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print('Port {} open.'.format(port))
            else:
                print('Port {} closed.'.format(port))

            #Cerramos el socket.
            sock.close()
    except sock.error as error:
        print(str(error))
        print('La conexión tuvo un error.')
        sys.exit() #Salimos del programa.

#Ejecutando la función.
check_ports(ip, portList)
