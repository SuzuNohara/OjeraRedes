import socket
import pickle
import threading

HOST = '127.0.0.1'
PORT = 666

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(4096)
        if not data:
            break
        obj = pickle.loads(data)
        print(f"Received from {addr}: {obj}")
        response = pickle.dumps(obj)
        conn.sendall(response)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
