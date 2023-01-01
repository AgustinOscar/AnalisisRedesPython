'''
    * sniff()

        Argumentos:
            iface: Interfaz desde la que se van a obtener paquetes.
            count: Número de paquetes a capturar (0 para paquetes infinitos).
            prn: Función a ejecutar por cada uno de los paquetes.
            store: Si se desean guardar o eliminar los paquetes capturados (0 para sólo monitorizar).
            timeout: Termina la captura después de este tiempo.
            filter: Utiliza la sintaxis BPF (Berkeley Packet Filters).
'''

from scapy.all import *

#lsc() #Nos muestra todos los comandos que tiene scapy.
#help(sniff) #Muestra información del método.

#Escuchando el tráfico de red.
sniff()

#Escuchando el tráfico en una interfaz específica.
#sniff(iface='fe80')

#prn Permite ejecutar una función en cada paquete.
# pkts = sniff(filter='', prn=function, count=3)

pkts = sniff(filter='icmp', prn= lambda pkt: '{} {}'.format(pkt.sniffed_on, pkt.summary()), count=3, timeout=10)
pkts.show()

