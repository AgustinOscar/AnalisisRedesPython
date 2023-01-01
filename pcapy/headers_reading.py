#Librerías necesarias.
import pcapy
from struct import *

#Lectura de cabeceras en paquetes.
cap = pcapy.open_live('en0', 65536, 1, 0)

while 1:
    (header, payload) = cap.next()
    l2hdr = payload[:14]
    l2data = unpack('!6s6sH', l2hdr)
    srcmac = '%.2x:%.2x:%.2x:%.2x:%.2x:%.2x' % (l2hdr[0], l2hdr[1], l2hdr[2], l2hdr[3], l2hdr[4], l2hdr[5])
    dstmac = '%.2x:%.2x:%.2x:%.2x:%.2x:%.2x' % (l2hdr[6], l2hdr[7], l2hdr[8], l2hdr[9], l2hdr[10], l2hdr[11])
    print('Source MAC: {srcmac}\t Destination MAC: {}'.format(srcmac, dstmac))

    #Obtenemos el IP header de 14 bytes desde 14 al 34 en el payload.
    ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
    timetolive = ipheader[5]
    protocol = ipheader[6]
    print('Protocol: {} Time To Live: {}'.format(protocol, timetolive))
