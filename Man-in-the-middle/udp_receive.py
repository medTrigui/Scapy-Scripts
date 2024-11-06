# Mohamed Trigui 9/24/24

import socket

# Server (Host 2) configuration
server_ip = "0.0.0.0"   # Listen on all available interfaces
server_port = 9090    # Same port as the client

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP and port
udp_socket.bind((server_ip, server_port))

print("UDP server is listening...")

# Process incoming messages from the client
try:
    while True:
        data, client_addr = udp_socket.recvfrom(1024)  # Receive client data
        print(f"Message from {client_addr}: {data.decode()}")
        
        # Send a response back to the client
        response = f"Received your message: {data.decode()}"
        udp_socket.sendto(response.encode(), client_addr)
        
except KeyboardInterrupt:
    print("\nServer shutting down.")

finally:
    udp_socket.close()

