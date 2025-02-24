import socket
import pickle

HOST = '127.0.0.1'
PORT = 666

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(4096)
        if not data:
            continue
        obj = pickle.loads(data)
        print(f"Object received from {addr}: {obj}")
        response = pickle.dumps(obj)
        s.sendto(response, addr)
