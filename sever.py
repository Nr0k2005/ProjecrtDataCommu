import socket
import threading

# Auto-response dictionary
auto_responses = {
    "hello": "Hi there! How can I help you?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm just a server, but I'm here to assist you!",
    "help": "Available commands: hello, bye, how are you, help",
    "time": "Sorry, I don't have a clock, but I'm always here for you!"
}

# Banner message (3-5 lines)
BANNER = """
╔══════════════════════════════════════╗
║   Welcome to the Chat Server!        ║
║   Type 'help' to see commands.       ║
║   Type 'bye' to disconnect.          ║
╚══════════════════════════════════════╝
"""

def get_auto_response(message):
    message = message.lower().strip()
    # Check if message matches any key in dictionary
    for key in auto_responses:
        if key in message:
            return auto_responses[key]
    return None  # No auto-response found

def handle_client(connection, client_address):
    print(f'[+] Connection from {client_address}')
    try:
        # Send banner when client connects
        connection.sendall(BANNER.encode())

        while True:
            data = connection.recv(1024)
            if not data:
                break

            message = data.decode().strip()
            print(f'Client {client_address}: {message}')

            # Check for auto-response first
            auto_reply = get_auto_response(message)
            if auto_reply:
                print(f'[Auto] Sending: {auto_reply}')
                connection.sendall(auto_reply.encode())
            else:
                # No auto-response — server types manually
                response = input('You: ')
                connection.sendall(response.encode())

    finally:
        print(f'[-] Disconnected: {client_address}')
        connection.close()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address and port
server_address = ('172.19.173.217', 10000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print('Server is running and listening on port 10000')

while True:
    connection, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.daemon = True
    client_thread.start()