# Mohamed Trigui
# 9/25/2024
# TCP Server (on Host 1)

import socket

# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('10.0.0.1', 9090)  # Server listens on this address and port
print(f'Starting server on {server_address}')
socket.bind(server_address)

# Listen for connections
socket.listen()

while True:
    print("Awaiting new connection ...")
    connection, client_address = socket.accept()

    try:
        print(f"Connected by {client_address}")
        # Receive data in chunks
        while True:
            msg = connection.recv(1024)
            if msg:
                print(f"Received: {msg.decode()}")
                connection.sendall(b"Message acknowledged!")
            else:
                print(f"End of data from {client_address}")
                break
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        # Clean up the connection
        connection.close()
        print(f"Connection with {client_address} terminated.")


