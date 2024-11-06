# Mohamed Trigui 9/22/2024
#!/usr/bin/python3

from scapy.all import *

def spoof_pkt(pkt):
    #check if pkt is an ICMP pkt and if it is an echo request (type 8)
    if ICMP in pkt and pkt[ICMP].type == 8:
        print("Original Packet .....")
        print("Source IP:", pkt[IP].src)
        print("Destination IP :", pkt[IP].dst)

        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl)
        ip.ttl = 99
        icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)

        if pkt.haslayer(Raw):
            data = pkt[Raw].load
            newpkt = ip/icmp/data
        else:
            newpkt = ip/icmp

        print("Spoofed Packet .....")
        print("Source IP: ", newpkt[IP].src)
        print("Destination IP: ", newpkt[IP].dst)

        send(newpkt, verbose=0)

# Sniff and spoof from h3
sniff(iface='h3-eth0', filter='icmp', prn=spoof_pkt)
