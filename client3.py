import socket
# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('Server ip address', 8000)  # Change the address and port as needed

# Connect to the server
client_socket.connect(server_address)
print(f"Connected to the server.{server_address}")

# Receive the file data from the server
file_data = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    file_data += data

# Save the received file in the client's folder
with open('client/recieved-file.txt', 'wb') as file:
    file.write(file_data)

print("File received successfully.")

client_socket.close()
