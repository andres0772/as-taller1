# Juego del Ahorcado Multiplayer - Socket

**Materia:** Arquitectura de Software  
**Estudiante:** Andrés Esteban Vásquez Peña

---

## Descripción

Juego del ahorcado multijugador implementado con sockets TCP en Python. Varios jugadores pueden conectarse simultáneamente para adivinar una palabra secreta en tiempo real. Todos comparten los mismos intentos y trabajan en equipo para descubrir la palabra.

### Características

- **Multijugador en tiempo real:** Varios clientes pueden conectarse al mismo servidor
- **Sincronización instantánea:** Todos ven los mismos intentos y progreso
- **Gestión de desconexiones:** Si un jugador se va, los demás siguen jugando
- **Comunicación bidireccional:** Servidor distribuye mensajes a todos los clientes

---

## Requisitos

- Python 3.x (cualquier versión moderna)
- No requiere librerías externas 

---

## Estructura del Proyecto

```
├── servidor.py    # Servidor del juego (debe ejecutarse primero)
└── cliente.py     # Cliente para cada jugador
```

---

## Cómo Ejecutar

### Paso 1: Iniciar el Servidor

En una terminal, ejecutá el servidor:

```bash
python3 servidor.py
```

El servidor mostrará la palabra secreta y quedará esperando conexiones.

### Paso 2: Conectar Clientes

En otra terminal (por cada jugador), ejecutá el cliente:

```bash
python3 cliente.py
```

**Repetí este paso en tantas terminales como jugadores quieras.**

---

## Flujo del Juego

1. **El cliente te pedirá tu nombre:**
   ```
   Tu nombre: Juan
   ```

2. **El servidor informa quién se unió:**
   ```
   Juan se unió | Jugando: Juan, María, Pedro
   ```

3. **Se muestra el estado del juego:**
   ```
   Palabra: _ _ _ _ _ | Intentos: 6 | Jugando: Juan, María, Pedro
   ```

4. **Ingresá una letra y presioná Enter:**
   ```
   Tu letra: A
   ```

5. **El servidor actualiza a todos:**
   - Si acertás: `Juan acertó 'A' | _ A _ _ _ | Intentos: 6`
   - Si fallás: `Juan falló con 'Z' | _ A _ _ _ | Intentos: 5`
   - Si repetís: `Juan ya usó 'A'`

6. **El juego termina cuando:**
   - **Ganan:** Descubren toda la palabra
   - **Pierden:** Se quedan sin intentos (0)

7. **Para salir:** Escribí `salir` y presioná Enter

---

## Ejemplo de Partida

### Terminal 1 - Servidor
```bash
$ python3 servidor.py
Servidor listo. Palabra secreta: PERRO
Un jugador se conecto desde ('127.0.0.1', 54321)
Un jugador se conecto desde ('127.0.0.1', 54322)
```

### Terminal 2 - Jugador 1 (Andrés)
```
$ python3 cliente.py
Tu nombre: Andrés

¡Empieza el juego!

Andrés se unió | Jugando: Andrés
Palabra: _____ | Intentos: 6
Tu letra: P
Andrés acertó 'P' | P____ | Intentos: 6 | Jugando: Andrés, María
Tu letra: 
```

### Terminal 3 - Jugador 2 (María)
```
$ python3 cliente.py
Tu nombre: María

¡Empieza el juego!

María se unió | Jugando: Andrés, María
Palabra: P____ | Intentos: 6
Tu letra: E
María acertó 'E' | PE___ | Intentos: 6 | Jugando: Andrés, María
Tu letra: 
```

---

## Arquitectura

### Servidor (`servidor.py`)
- **Socket TCP** en `localhost:8080`
- **Threading:** Cada cliente se atiende en un hilo separado (`threading.Thread`)
- **Broadcast:** Mensajes se envían a todos los clientes conectados
- **Estado compartido:** Palabra, intentos y letras usadas son globales

### Cliente (`cliente.py`)
- **Socket TCP** que se conecta al servidor
- **Hilo de recepción:** Escucha mensajes del servidor en segundo plano
- **Input principal:** El usuario ingresa letras

---

## Notas Técnicas

- Las palabras disponibles son: `GATO`, `PERRO`, `CASA`
- Intentos iniciales: **6**
- Puerto: **8080**
- Host: **localhost**

---
