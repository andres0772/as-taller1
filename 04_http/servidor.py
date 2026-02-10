# Servidor
import http.server
import socket

HOST = "localhost"
PORT = 8080


class Servidor(http.server.SimpleHTTPRequestHandler):
    pass


servidor = http.server.HTTPServer((HOST, PORT), Servidor)
servidor.serve_forever()
