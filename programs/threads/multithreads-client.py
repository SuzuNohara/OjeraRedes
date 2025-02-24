import socket
import pickle

HOST = '127.0.0.1'
PORT = 666

data_to_send = {
    "message": "Hello threaded server, I'm the client",
    "id": 14321,
    "status": "OK"
}

serialized_data = pickle.dumps(data_to_send)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(serialized_data)
    data = client_socket.recv(4096)
    response_obj = pickle.loads(data)

print(f"Response from server: {response_obj}")
