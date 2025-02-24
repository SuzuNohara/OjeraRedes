import socket

HOST = '127.0.0.1'
PORT = 666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = s.accept()

    with conn:
        print(f"Connection established from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received data:", data.decode())
            conn.sendall(data)
        print("Connection closed.")
