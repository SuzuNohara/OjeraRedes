from utils.TCPServer import TCPServer
from utils.UDPServer import UDPServer

class ServerManager:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def start_all(self):
        for server in self.servers:
            server.start()

    def stop_all(self):
        for server in self.servers:
            server.stop()

if __name__ == "__main__":
    manager = ServerManager()
    tcp_server = TCPServer(port=5001)
    manager.add_server(tcp_server)
    manager.start_all()