# -*- coding: utf-8 -*-

# pip install scapy

"""
[{'name': 'Intel(R) 82574L Gigabit Network Connection',
  'win_index': '4',
  'description': 'Ethernet0',
  'guid': '{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}',
  'mac': '00:0C:29:5C:EE:6D',
  'netid': 'Ethernet0'}]
"""

from pprint import pprint
from scapy.arch.windows import get_windows_if_list
from scapy.all import *


# disable verbose mode
conf.verb = 0


def parse_packet(packet):
    """sniff callback function.
    """
    if packet and packet.haslayer('UDP'):
        udp = packet.getlayer('UDP')
        udp.show()


def udp_sniffer():
    """start a sniffer.
    """
    interfaces = get_windows_if_list()
    pprint(interfaces)

    print('\n[*] start udp sniffer')
    sniff(
        filter="udp port 53",
        iface=r'Realtek PCIe GBE Family Controller', prn=parse_packet,
        store=0)
    

# # create a layer 3 socket
# s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

if __name__ == '__main__':
    print(s)
    udp_sniffer()
    