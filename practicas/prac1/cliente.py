import socket

def cliente(mensaje, host='127.0.0.1', puerto=8080):
    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establecer el socket como bloqueante
    cliente_socket.setblocking(True)
    # Conectar el socket al servidor
    cliente_socket.connect((host, puerto))
    print(f'Conectado a {host}:{puerto}')
    # Enviar el mensaje al servidor
    cliente_socket.sendall(mensaje.encode())
    # Cerrar el socket del cliente
    cliente_socket.close()
    print(f'Mensaje enviado al servidor: {mensaje}')

cliente("Hola, servidor")