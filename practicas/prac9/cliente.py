import socket
import struct

group = '224.1.1.1'
port = 5004
ttl = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set TTL
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('b', ttl))

# Set the interface (change to the correct IP of your interface)
local_ip = '10.100.74.247'  # wlo1
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(local_ip))

print("Escribe tus mensajes. Escribe 'salir' para terminar.")
while True:
    message = input("Ingrese el mensaje a enviar: ")
    if message.lower() == 'salir':
        break
    sock.sendto(message.encode('utf-8'), (group, port))

print("Cliente cerrado.")
