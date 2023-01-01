'''
    En este archivo se muestran ejemplos para el envío y recepción de paquetes.
'''

'''
    ENVÍO DE PAQUETES

        * send():
            Envía paquetes en la capa 3 (Capa de red).

            Argumentos:
                iface: Interfaz desde la que se va a enviar el paquete.
                inter: Tiempo (segundos) para el envío entre paquetes.
                loop: Envío infinito de paquetes (hasta Ctrl + C).
                packet: Paquete o lista de paquetes.
                verbose: Permite cambiar el nivel de log o cambiarlo (0).  
        
        * sendp():
            Envía paquetes en la capa 2 (Enlace de datos).
'''


from scapy.all import *

#Creando paquete.
package = (IP( #Tipo de paquete que queremos crear.
    dst='127.0.0.1') #Dirección IP destino del paquete.
    /ICMP()/ #Paquete ICMP con la configuración default de Scapy.
    'Hello world' #Payload a incluir en el paquete. (Opcional)
    )

#Envíando un paquete.
send(package)

#Creando paquete.
package = (IP( #Tipo de paquete que queremos crear.
    src='10.211.55.100', #Spoofing de la dirección de origen (IP falsa).
    dst='127.0.0.1') #Dirección IP destino del paquete.
    /ICMP()/ #Paquete ICMP con la configuración default de Scapy.
    'Hello world' #Payload a incluir en el paquete. (Opcional)
    )

send(package)

#Creando paquete.
package = (IP( #Tipo de paquete que queremos crear.
    src='10.211.55.100', #Spoofing de la dirección de origen (IP falsa).
    dst='127.0.0.1', #Dirección IP destino del paquete.
    ttl=128) #Time to live de 128 segundos.
    /ICMP()/ #Paquete ICMP con la configuración default de Scapy.
    'Hello world' #Payload a incluir en el paquete. (Opcional)
    )

send(package)


#Envío de paquetes de la capa 2 (Enlace de datos).
package = (Ether()
/IP(dst='twitter.com')
/ICMP()/
'Paquete en la capa dos')

#Envío a través de un loop.
#send(package, loop=1, inter=1)


#Spoofear direcciones MAC.
ether_package = (Ether(src='ab:cd:ef:ab:cd:ef', dst='ff:ff:ff:ff:ff:ff')
/IP(src='1.2.3.4', dst='3.4.5.6')
/UDP(dport=9)/
b'hello')

ether_package.show()

#Envío a través de un loop.
send(ether_package)


#Creando un paquete para esperar su respuesta.
pkt = IP(dst='twitter.com')/ICMP()/'Paquete de la capa 3'

pkt.summary()

sr(pkt) #Se queda con todos los paquetes que reciben respuesta.
srp(pkt) #Lo mismo pero en la capa 2.
sr1(pkt) #Se queda con el primer paquete que recibe una respuesta.
srp1(pkt) #Lo mismo pero en la capa 2.
srbt(pkt) #Conexiones bluetooth.
srloop(pkt) #Envío y recepción de paquetes n veces.
srploop(pkt) #Envío y recepción de paquetes n veces en la capa 2.



#Recibiendo respuestas.