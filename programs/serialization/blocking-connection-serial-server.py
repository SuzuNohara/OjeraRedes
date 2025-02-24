import socket
import pickle

HOST = '127.0.0.1'
PORT = 666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connecting from {addr}")
        while True:
            data = conn.recv(4096)
            if not data:
                break
            obj = pickle.loads(data)
            print(f"Object received: {obj}")
            response = pickle.dumps(obj)
            conn.sendall(response)
