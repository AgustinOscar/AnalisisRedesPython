'''
    * pcapy.findalldevs()
        El siguiente código sirve para reconocer los dispositivos que están a nuestro alcance.

    * pcapy.lookupdev()
        Seleccionara un dispositivo válido que podemos utilizar después del método open_live().

    * pcapy.open_live()
        Método para capturar paquetes.
'''

#Librerías necesarias.
import pcapy

#Se obtienen todos los dispositivos al alcance.
devs = pcapy.findalldevs()
print(devs)

