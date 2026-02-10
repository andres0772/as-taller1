# Cliente
import http.client
import socket

HOST = "localhost"
PORT = 8080

cliente = http.client.HTTPConnection(HOST, PORT)
cliente.request("GET", "/")

respuesta = cliente.getresponse()
datos = respuesta.read().decode()

print(datos)

cliente.close()
