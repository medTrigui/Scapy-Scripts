# Mohamed Trigui 9/22/24
#!/usr/bin/python3
from scapy.all import *

def process_packet(pkt):
    # Show the packet in human-readable form
    pkt.show()
    print("------------------")
    
# Set filter to only capture icmp traffic
f = 'icmp'

# Start sniffing
sniff(filter=f, prn=process_packet)


