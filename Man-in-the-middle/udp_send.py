# Mohamed Trigui
# 9/24/2024
import socket

# Step 2: Define the target IP address and port number
target_ip = "10.0.0.2"
target_port = 9090

# Create a udp socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input("Enter message to send to Server: ")
        udp_socket.sendto(message.encode(), (target_ip, target_port))
        
        # Receive the server response
        data, server = udp_socket.recvfrom(1024)
        print("Server says: ", data.decode())

except KeyboardInterrupt:
    print("\nClient exiting.")

udp_socket.close
