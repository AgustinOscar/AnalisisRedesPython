'''
    * pcapy.open_live()
        Método para capturar paquetes.

    Argumentos:
        * Dispositivo.
        * Bytes a capturar por paquete.
        * Modo promiscuo.
        * Timeout (ms).
'''

#Librerías necesarias.
import pcapy

#Se capturan los paquetes.
package = pcapy.open_live()

#package.setfilter('tcp port 80')

count = 1

while count:
    (header, payload) = package.next() #Pasamos de un paquete a otro.
    print('{0}: {1}-{2}'.format(count, header, payload))
    count += 1