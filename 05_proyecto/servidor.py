import random
import socket
import threading

# Configurar conexión
HOST = "localhost"
PORT = 8080

# Preparar el juego
palabras = ["GATO", "PERRO", "CASA"]  # de ejemplo
palabra_secreta = random.choice(palabras)
palabra_mostrar = "_" * len(palabra_secreta)
intentos = 6
letras_usadas = []
clientes = []
nombres = {}


# Función para enviar a TODOS
def enviar_a_todos(mensaje):
    # Recorre cada jugador y le envía el mensaje
    for cliente in clientes[:]:  # [:] evita errores si alguien se va
        try:
            cliente.send(mensaje.encode())
        except:
            if cliente in clientes:
                clientes.remove(cliente)
            if cliente in nombres:
                del nombres[cliente]


# Función que maneja a UN jugador
def manejar_jugador(cliente):
    global palabra_mostrar, intentos

    # Pedir nombre al jugador
    nombre = cliente.recv(1024).decode().strip()
    nombres[cliente] = nombre
    clientes.append(cliente)

    # Avisar a todos que llegó
    lista = ", ".join(nombres.values())
    enviar_a_todos(f"{nombre} se unió | Jugando: {lista}\n")

    # Enviar estado inicial SOLO a este jugador
    cliente.send(f"Palabra: {palabra_mostrar} | Intentos: {intentos}\n".encode())

    # Bucle: esperar letras
    while True:
        try:
            letra = cliente.recv(1024).decode().strip().upper()

            # Si el jugador se desconectó
            if not letra:
                break

            # Validar que sea una letra
            if len(letra) != 1 or not letra.isalpha():
                cliente.send("Envía UNA letra\n".encode())
                continue

            # LÓGICA DEL JUEGO

            # Letra repetida
            if letra in letras_usadas:
                lista = ", ".join(nombres.values())
                enviar_a_todos(
                    f"🔄 {nombre} ya usó '{letra}' | {palabra_mostrar} | Intentos: {intentos} | Jugando: {lista}\n"
                )
                continue

            letras_usadas.append(letra)

            # Letra INCORRECTA
            if letra not in palabra_secreta:
                intentos -= 1
                lista = ", ".join(nombres.values())
                enviar_a_todos(
                    f"{nombre} falló con '{letra}' | {palabra_mostrar} | Intentos: {intentos} | Jugando: {lista}\n"
                )

                # ¿Perdieron todos?
                if intentos == 0:
                    enviar_a_todos(f"¡PERDIERON! La palabra era {palabra_secreta}\n")
                    break

            # Letra CORRECTA
            else:
                # Actualizar palabra
                nueva = ""
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        nueva += letra
                    else:
                        nueva += palabra_mostrar[i]
                palabra_mostrar = nueva

                lista = ", ".join(nombres.values())
                enviar_a_todos(
                    f"{nombre} acertó '{letra}' | {palabra_mostrar} | Intentos: {intentos} | Jugando: {lista}\n"
                )

                # ¿Ganaron todos?
                if "_" not in palabra_mostrar:
                    enviar_a_todos(
                        f"¡GANARON TODOS! La palabra era {palabra_secreta}\n"
                    )
                    break

        except:
            break  # Jugador se desconectó

    # Al salir: limpiar y avisar
    if cliente in clientes:
        clientes.remove(cliente)
    if cliente in nombres:
        nombre_saliente = nombres.pop(cliente)
        lista = ", ".join(nombres.values()) if nombres else "nadie"
        enviar_a_todos(f"{nombre_saliente} se fue | Quedan: {lista}\n")
    cliente.close()


# PASO 6: Iniciar servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"Servidor listo. Palabra secreta: {palabra_secreta}")

# Aceptar jugadores para siempre
while True:
    cliente, direccion = servidor.accept()
    print(f"Un jugador se conecto desde {direccion}")

    # Crear hilo para atenderlo
    hilo = threading.Thread(target=manejar_jugador, args=(cliente,), daemon=True)
    hilo.start()
