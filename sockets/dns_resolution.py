'''
    RESOLUCIÓN DE DOMINIOS Y DIRECCIONES.

    * gethostname():
        Devuelve el hostname.

    * gethostname_ex():
        Duevuelve una tupla con el dominio y las IPs que lo resuleven.
    
    * gethostbyname():
        Mapea un hostname a una dirección IP.

    * gethostbyaddr():
        Mapea una dirección IP a un hostname y su información DNS.

    * getserverbyname():
        Mapea un nombre de servicio y un nombre de protocolo a un puerto.

    * getprotocolbyname():
        Mapea el nombre de un protocolo a un puerto.
'''

#Librerías necesarias.
import socket
import sys

try:
    #Obtenemos el nombre de la máquina donde estamos ejecutando el script.
    print('gethostname: ', socket.gethostname())

    #Obtenemos el hostname concreto de la dirección (parámetro).
    print('gethostbyname: ', socket.gethostbyname('www.google.com'))

    #
    print('gethostname_ex: ', socket.gethostbyname_ex('www.google.com'))

    #Convierte una dirección IP en su dominio.
    print('gethostbyaddr: ', socket.gethostbyaddr('8.8.8.8'))

    #Obtenemos el nombre completo del dominio.
    print('getfqdn: ', socket.getfqdn('www.google.com'))

    #
    print('getaddrinfo: ', socket.getaddrinfo('www.google.com', None, 0))

except socket.error as error:
    print(str(error))
    print('Connection Error')