import socket

HOST = "localhost"
PORT = 8080

cliente = socket.socket()
cliente.connect((HOST, PORT))

print(cliente.recv(1024).decode())

while True:
    letras = input("digite la letra: ")
    cliente.send(letras.encode())

    respuesta = cliente.recv(1024).decode()
    print(respuesta)

    if "ganaste" in respuesta or "perdiste" in respuesta:
        break
cliente.close()
