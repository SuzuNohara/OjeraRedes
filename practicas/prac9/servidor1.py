import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5004
IFACE_IP = '192.168.0.72'  # IP de wlo1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))

# Join multicast group on the specific interface
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("Servidor1 escuchando en el grupo multicast...")
while True:
    print("Usando interfaz:", sock.getsockname())
    data, addr = sock.recvfrom(10240)
    print(f"[{addr}] {data.decode()}")
