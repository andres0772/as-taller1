# Cliente
import socket

HOST = "localhost"
PORT = 8080
mensaje = input("Dijite tu mensaje  : ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

cliente.sendall(mensaje.encode())
print(f"Mensaje enviado: '{mensaje}'")

respuesta = cliente.recv(1024)
print(f"Respuesta del 'echo' : '{respuesta.decode()}'")

cliente.close()
