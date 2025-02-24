import socket
import tkinter as tk
from tkinter import filedialog

def receive_file(file_name, host='127.0.0.1', puerto=5001, tam_buffer=1024):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, puerto))
        print(f"Connecting to the server {host}:{puerto}...")

        with open(file_name, "wb") as archivo:
            while True:
                data = s.recv(tam_buffer)
                if not data:
                    break
                archivo.write(data)
        print(f"FIle {file_name} Received successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Select file location", defaultextension=".txt")
    if file_path:
        print("Getting file from: ", file_path)
        receive_file(file_path)