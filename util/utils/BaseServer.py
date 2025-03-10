import socket

class BaseServer:
    def __init__(self, host='127.0.0.1', port=5001, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

    def start(self):
        raise NotImplementedError("Not implemented")

    def stop(self):
        raise NotImplementedError("Not implemented")