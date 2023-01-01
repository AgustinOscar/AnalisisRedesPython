from scapy.all import *

traceroute(['www.google.com.mx'], maxttl=20)

#Constuyendo un traceroute de manera más manual.
ip = IP(dst='www.google.com.mx')
udp = UDP(dport=40000)
pkt = ip/udp
rsp = send(pkt)
