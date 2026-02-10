# Cliente
import socket
import threading

HOST = "localhost"
PORT = 8080


def recibir_mensaje():
    while True:
        mensaje = cliente.recv(1024).decode()
        print(mensaje)


nombre = input("Cual es tu nombre?  : ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
cliente.send(nombre.encode())

hilo_recibir = threading.Thread(target=recibir_mensaje)
hilo_recibir.start()

while True:
    mensaje = input("mensaje: ")
    cliente.send(mensaje.encode())
