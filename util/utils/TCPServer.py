from .BaseServer import BaseServer
import socket

class TCPServer(BaseServer):
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(1)
            print(f"TCP Server listening on {self.host}:{self.port}...")
            conn, addr = s.accept()
            with conn:
                print(f"Connection established from {addr}")
                while True:
                    data = conn.recv(self.buffer_size)
                    print("Received data:", data)
                    if not data:
                        break
                    conn.sendall(data)
                print("Connection closed.")