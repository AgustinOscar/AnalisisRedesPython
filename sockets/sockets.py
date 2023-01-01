'''
    En este archivo se describe cómo crear sockets.
'''

#Librerías necesarias.
import socket
import sys

'''
    Sintaxis:

        skt = socket(socket_family, socket_type, protocol=0)

    socket_family:
        * Sockets UNIX: socket.AF_UNIX  (Basados en la capa de datos, antes
                                        de la definición de la capa de red).
        * Sockets IPV4: socket.AF_INET  (Trabaja con el protocolo IPv4).
        * Sockets IPV6: socket.AF_INET6 (Trabaja con el protocolo IPv6).

    socket_type:
        * TCP: socket.SOCK_STREAM
        * UDP: socket.SOCK_DGRAM
'''

print(dir(socket))

'''
    PRINCIPALES MÉTODOS Y FUNCIONES GENERALES

    * socket():
        Crea un objeto de la clase socket.
    
    * connect():
        Conecta un socket a una dirección.
    
    * send(bytes):
        Envía datos al target específicado (TCP).

    * sendfrom(data, address):
        Envía datos al target específicado (UDP).

    * sendall(data):
        Envía todos los datos del buffer al socket.
    
    * recv(buflen):
        Permite recibir una cantidad de datos (TCP).

    * recvfrom(buflen):
        Recibe la cantidad de datos (UDP).
    
    * recv_into(buflen):
        Recibe los datos y los guarda en el buffer.

    * close():
        Cierra el descriptor del socket.
'''

'''
    PRINCIPALES FUNCIONES DEL LADO DEL SERVIDOR

    * bind(address):
        Enlaza un socket a una dirección.

    * listen(count):
        Permite a un socket aceptar conexiones.

    * accept():
        Acepta una conexión, devuelve el objeto conexión y la dirección.
        Necesita bind() y listen() previamente.
'''

'''
    PRINCIPALES FUNCIONES DEL LADO DEL CLIENTE

    * connect():
        Conecta un cliente a una dirección.

    * connect_ex():
        Misma funcionalidad del connect pero ofrece la posibilidad de devolver
        un error si no se puede establecer la conexión. Es muy útil en los escaneos
        de puertos.
'''


#Creando un socket TCP.
skt_tcp = socket.socket()
print(skt_tcp)

#Creando un socket UDP.
skt_udp = socket.socket(type=socket.SOCK_DGRAM)
print(skt_udp)

#Ejemplo del escaneo de diferentes puertos.

#IP del localhost.
ip = '127.0.0.1'
portList = [21, 22, 23, 80]

#Se escanean todos los puertos en la lista.
for port in portList:
    
    #Se crea socket TCP-IPv4.
    skt_tcp_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Intentamos conectar el socket a una dirección.
    result = skt_tcp_ipv4.connect_ex((ip, port))

    #Mostramos resultados en pantalla.
    print(port, ':', result)

    #Cerramos el socket.
    skt_tcp_ipv4.close()