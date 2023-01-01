from scapy.all import *

#Creando un paquete TCP/IP.
pkt_tcp = Ether()/IP(dst='twiter.com')/TCP(dport=80)

#Imprimiendo en pantalla el contenido del paquete.
pkt_tcp.show()

#Enviar el paquete.
send(pkt_tcp)