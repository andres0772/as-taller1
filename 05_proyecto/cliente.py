import socket
import threading

HOST = "localhost"
PORT = 8080

# construye el socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# pide el nombre
nombre = input("Tu nombre: ")
cliente.send(nombre.encode())


# Función para recibir mensajes
def recibir():
    while True:
        try:
            mensaje = cliente.recv(1024).decode()
            if mensaje:
                # \r borra la línea actual para mostrar el mensaje limpio
                print(f"\r{mensaje}", end="")
                print("Tu letra: ", end="", flush=True)
        except:
            break


# Iniciar hilo para recibir
hilo = threading.Thread(target=recibir, daemon=True)
hilo.start()

# Enviar letras
print("\n✨ ¡Empieza el juego!\n")
print("Tu letra: ", end="", flush=True)

while True:
    letra = input()
    if letra.lower() == "salir":
        break
    if len(letra) == 1 and letra.isalpha():
        cliente.send(letra.upper().encode())
    else:
        print("Envía UNA letra: ", end="", flush=True)

cliente.close()
print("\nJuego terminado")
