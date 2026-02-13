# Plan: Juego del Ahorcado Cooperativo

## Descripción
Juego del ahorcado donde múltiples clientes **cooperan** para adivinar la palabra juntos. Si uno adivina, GANAN TODOS. Si se agotan los intentos, PIERDEN TODOS.

---

## Cambios del modo Original al Cooperativo

### Antes (Competitivo)
- Gana el primero que adivine
- Cada cliente tiene sus propios intentos
- No hay lista de jugadores visible

### Después (Cooperativo)
- Intentos **compartidos** entre todos
- ¡Gana o pierde EL GRUPO entero!
- Lista de jugadores conectados
- Mensajes de entrada/salida
- Preguntar si quieren volver a jugar

---

## Decisiones de Diseño

### 1. Modo de juego
**Cooperativo (MÚLTIPLES JUGADORES)**
- Todos ven la misma pantalla
- Intentos compartidos: "_ _ _ _ _ | Intentos: 5"
- Gana el GRUPO si alguien adivina
- Pierde el GRUPO si se agotan intentos

### 2. Selección de palabra
**El servidor elige al azar de una lista**
- Lista predefinida de palabras
- Una palabra por partida

### 3. Información visible para cada cliente
- Las letras adivinadas (ej: `_ A _ A _`)
- **Intentos restantes del GRUPO**
- Letras ya utilizadas por cualquiera
- Lista de jugadores conectados
- Resultado final (¡GANARON! o ¡PERDIERON!)
- Mensajes de estado (letra correcta, letra repetida, etc.)

### 4. Flujo de comunicación

```
Cliente envía letra
       ↓
Servidor verifica si está en la palabra
       ↓
SI está:
  - Actualiza palabra_revelada
  - Broadcast a TODOS: "{jugador} acertó! _ A _ A _ | Intentos: 5"
  - Si palabra completa → ¡GANARON TODOS!

SI NO está:
  - Reduce intentos compartidos
  - Broadcast: "{jugador} erró. _ A _ A _ | Intentos: 4"
  - Si intentos == 0 → ¡PERDIERON TODOS!

SI letra ya fue usada:
  - Broadcast: "{jugador} ya usó 'A'. Intentos: 5"
```

---

## Funcionalidades Nuevas (Cooperativo)

- [x] Servidor básico (socket, listen, accept)
- [x] Recepción de nombre del cliente
- [x] Lista de clientes conectados
- [x] Recepción de letras
- [x] Verificación de letras (correcta/incorrecta/repetida)
- [x] Broadcast del estado
- [x] Determinación de victoria/derrota
- [ ] **Lista visible de jugadores conectados**
- [ ] **Mensaje cuando alguien se une**
- [ ] **Mensaje cuando alguien se va**
- [ ] **Preguntar si quieren reiniciar partida**

---

## Funcionalidades del Cliente

- [x] Conectarse al servidor
- [x] Mostrar estado del juego
- [x] Enviar letras
- [x] Recibir actualizaciones
- [x] Mostrar mensajes
- [x] Mostrar resultado final
- [ ] **Mostrar lista de jugadores**
- [ ] **Opción de reiniciar**

---

## Estado del juego

```python
# Variables del servidor
clientes = []                    # Lista de sockets conectados
palabras = ["CASA", "PERRO", ...]

palabra_secreta = "PROGRAMACION"
palabra_revelada = "_ _ _ _ _ _ _ _ _ _ _"
intentos = 6                     # COMPARTIDOS por todos
letras_usadas = ["A", "O"]      # Compartidas por todos
jugadores = {}                   # {socket: "nombre"}
juego_terminado = False
```

---

## Protocolo de comunicación

### Cliente → Servidor
- Primera conexión: nombre (string)
- Después: una letra (ej: "A")

### Servidor → Cliente (broadcast)
- Estado: `"_ A _ _ A | Intentos: 5 | Jugadores: Juan, Martin"`
- Mensaje: `"Juan acertó!"`
- Error: `"Juan ya usó 'A'"`
- Victoria: `"¡GANARON! La palabra era PERRO"`
- Derrota: `"¡PERDIERON! La palabra era PERRO"`

---

## Próximos pasos

1. [x] Implementar servidor básico
2. [x] Implementar cliente de prueba
3. [x] Agregar lógica de palabras
4. [x] Agregar verificación de letras
5. [x] Agregar broadcast
6. [x] Manejar victoria/derrota
7. [x] Probar con múltiples clientes
8. [ ] **Agregar lista de jugadores**
9. [ ] **Agregar mensajes de entrada/salida**
10. [ ] **Mejorar cliente final**
11. [ ] **Opción de reiniciar partida**

---

## Notas

- El servidor guarda el nombre asociado a cada socket
- Cuando alguien gana/perder, el juego termina
- Para reiniciar, se puede crear una función `reiniciar_juego()`
- La lista de jugadores se puede enviar con cada broadcast
