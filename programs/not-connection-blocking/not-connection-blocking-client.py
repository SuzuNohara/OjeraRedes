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

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(serialized_data, (HOST, PORT))
    data, server = s.recvfrom(4096)
    response_obj = pickle.loads(data)
    print(f"Object received from server: {response_obj}")
