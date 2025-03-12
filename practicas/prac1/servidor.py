import socket

def servidor(host='127.0.0.1', puerto=8080):
    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establecer el socket como bloqueante
    servidor_socket.setblocking(True)
    # Vincular el socket al puerto
    servidor_socket.bind((host, puerto))
    # Escuchar conexiones entrantes
    servidor_socket.listen(1)
    print(f'Servidor escuchando en {host}:{puerto}')
    # Esperar a que llegue una conexión
    conexion, direccion = servidor_socket.accept()
    print(f'Conexión aceptada de {direccion}')
    # Establecer el socket de conexión como bloqueante
    conexion.setblocking(True)
    # Recibir el mensaje
    mensaje = conexion.recv(1024).decode()
    # Mostrar el mensaje recibido
    print(f'Mensaje recibido: {mensaje}')
    # Cerrar la conexión y el socket del servidor
    conexion.close()
    servidor_socket.close()

servidor()