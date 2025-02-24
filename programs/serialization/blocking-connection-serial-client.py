import socket
import pickle

HOST = '127.0.0.1'
PORT = 666

data_to_send = {
    "message": "Hello server, I'm the client",
    "id": 14321,
    "status": "OK"
}

serialized_data = pickle.dumps(data_to_send)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(serialized_data)
    data = s.recv(4096)
    response_obj = pickle.loads(data)

print(f"Object received from server: {response_obj}")
