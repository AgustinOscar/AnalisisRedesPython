from scapy.all import *


#Creando paquete TCP/IP.
#ans: Paquetes respondidos.
#unans: Paquetes no respondidos.
#Puerto 23: telnet.
ans, unans = sr(IP(dst='127.0.0.1')/TCP(dport=23)) 
ans.summary()

ans, unans = sr(IP(dst='127.0.0.1')/TCP(dport=[23,80,53])) 
ans.summary()

#Escaneo de puertos.
ans, unans = sr(IP(dst='127.0.0.1')/TCP(sport=666, dport=[23,80,53,21], flags='S'))
ans.summary()

#Escaneo de puertos.
ans, unans = sr(IP(dst='127.0.0.1')/TCP(sport=666, dport=[23,80,53,21], flags='A'))
ans.summary()