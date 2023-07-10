import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('Server ip address', 8000)  # Change the address and port as needed
server_socket.bind(server_address)
server_socket.listen(1)

print("Server is listening for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Take user input for the file name to be transferred
    file_name = input("Enter the name of the file to transfer: ")

    try:
        # Open the file in binary mode
        with open(f'server/{file_name}', 'rb') as file:
            file_data = file.read()

        # Send the file data to the client
        client_socket.sendall(file_data)
        print("File sent successfully.")
    except FileNotFoundError:
        print("File not found.")

    client_socket.close()
