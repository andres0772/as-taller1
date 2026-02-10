# Servidor
import socket

HOST = "localhost"
PORT = 8080

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print("el servidor esta en la espera de conexiones..")

cliente, direccion = servidor.accept()
print(f"un cliente {cliente} se conecto desde la direccion {direccion}")

datos = cliente.recv(1024)
cliente.sendall(
    b"hola!" + datos
)  # esta respuesta debe ser siempre en binaria no en cadena de texto
cliente.close()
