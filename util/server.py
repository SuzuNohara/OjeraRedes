import socket


def enviar_archivo(nombre_archivo, host='127.0.0.1', puerto=5001, tam_buffer=1024):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, puerto))
        s.listen(1)
        print(f"Servidor escuchando en {host}:{puerto}...")

        # Esperar conexión del cliente
        conn, addr = s.accept()
        with conn:
            print(f"Conexión establecida desde {addr}")
            try:
                with open(nombre_archivo, "rb") as archivo:
                    while (data := archivo.read(tam_buffer)):
                        conn.sendall(data)
                print("Archivo enviado exitosamente.")
            except FileNotFoundError:
                print(f"Error: El archivo {nombre_archivo} no se encontró.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    # Especifica el nombre del archivo que deseas enviar
    enviar_archivo("archivo_a_transferir.txt")
