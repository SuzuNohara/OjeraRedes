from .BaseServer import BaseServer
import socket

class UDPServer(BaseServer):
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))
            print(f"UDP Server listening on {self.host}:{self.port}...")
            while True:
                data, addr = s.recvfrom(self.buffer_size)
                print(f"Received data from {addr}")
                s.sendto(data, addr)