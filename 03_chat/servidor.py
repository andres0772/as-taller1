# Servidor
import socket
import threading

HOST = "localhost"
PORT = 8080

clientes = []


def atender_cliente(cliente, nombre):
    while True:
        try:
            mensaje = cliente.recv(1024)
            if not mensaje:
                break
            print(f"{nombre}: {mensaje.decode()}")
            broadcast(mensaje.decode(), cliente)
        except ConnectionResetError:
            clientes.remove(cliente)
            cliente.close()
            break


def broadcast(mensaje, emisor):
    for cliente in clientes:
        if cliente != emisor:
            cliente.send(mensaje.encode())


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print("el servidor 'CHAT' esta esperando conexiones..")

while True:
    cliente, direccion = servidor.accept()
    print(f"un cliente se conecto desde la IP {direccion}")
    nombre = cliente.recv(1024).decode()
    clientes.append(cliente)
    broadcast(f"{nombre} se ha unido al chat", cliente)
    hilo_cliente = threading.Thread(target=atender_cliente, args=(cliente, nombre))
    hilo_cliente.start()
