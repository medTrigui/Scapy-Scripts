# Mohamed Trigui
# 9/25/2024
# tcp_client

import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection to the server
server_address = ('10.0.0.1', 9090)
print(f"Connecting to {server_address}")
client_socket.connect(server_address)

try:
    while True:
        message = input("Enter message. Type 'exit' to exit: ")
        # If user types exit then break
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
finally:
    print("Closing connection")
    client_socket.close()

