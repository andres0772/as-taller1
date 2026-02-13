import random
import socket

HOST = "localhost"
PORT = 8080

palabras = ["perro", "gato", "elefante", "tigre"]
palabras_secreta = random.choice(palabras)
palabra_revelada = "_" * len(palabras_secreta)
intentos = 6
letras_usadas = []

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"minijuego fase beta activo, la palabra tiene {len(palabras_secreta)} letras")

cliente, direccion = servidor.accept()
print(f"se establecio conexion con {direccion}")

cliente.send(f"palabra: {palabra_revelada} | Intentos: {intentos}".encode())

while intentos > 0 and "_" in palabra_revelada:
    letras = cliente.recv(1024).decode().strip().lower()
    print(f"Letra recibida de cliente: '{letras}'")
    # si la letra ya fue usada
    if letras in letras_usadas:
        cliente.send(
            f"ya usaste {letras} | {palabra_revelada} | Intentos: {intentos}".encode()
        )
        continue
    letras_usadas.append(letras)

    # si la letra es correcta
    if letras in palabras_secreta:
        nueva = ""
        for i in range(len(palabras_secreta)):
            if palabras_secreta[i] == letras:
                nueva += letras
            else:
                nueva += palabra_revelada[i]
        palabra_revelada = nueva

        # gano
        if "_" not in palabra_revelada:
            cliente.send(f"has ganado la palabra era {palabras_secreta}".encode())
            break
        else:
            cliente.send(f"correcto {palabra_revelada} | Intentos: {intentos}".encode())
    # si la letra es incorrecta
    else:
        intentos -= 1
        if intentos == 0:
            cliente.send(f"has perdido la palabra era {palabras_secreta}".encode())
        else:
            cliente.send(
                f"incorrecto {palabra_revelada} | Intentos: {intentos}".encode()
            )

cliente.close()
servidor.close()
