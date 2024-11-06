# Mohamed Trigui 9/25/24
#!/usr/bin/python3
from scapy.all import *

def process_packet(pkt):
    # Show the packet in human-readable form
    pkt.show()
    print("------------------")
    
# Set filter to only capture tcp traffic
f = 'tcp'

# Start sniffing
sniff(filter=f, prn=process_packet)
