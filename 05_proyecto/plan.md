# Plan: Juego del Ahorcado Multiplayer

## Descripción
Juego del ahorcado donde múltiples clientes compiten para adivinar la palabra primero.

---

## Decisiones de Diseño

### 1. Modo de juego
**Varios clientes compitiendo entre ellos**
- Todos los clientes ven la misma pantalla de juego
- Gana el primero que adivine la palabra completa

### 2. Selección de palabra
**El servidor elige al azar de una lista**
- Lista predefinida de palabras en el servidor
- Una palabra por partida

### 3. Información visible para cada cliente
- Las letras adivinadas (ej: `_ A _ A _ A`)
- Intentos restantes
- Letras ya utilizadas
- Resultado final (ganó/perdió)
- Mensajes de estado (letra correcta, letra repetida, etc.)

### 4. Flujo de comunicación

```
Cliente envía letra
       ↓
Servidor verifica si está en la palabra
       ↓
SI está:
  - Actualiza la palabra revelada
  - Envía la nueva palabra a TODOS los clientes (broadcast)
  - Si la palabra quedó completa → ese cliente GANA

SI NO está:
  - Reduce intentos restantes
  - Envía actualización a TODOS los clientes

SI letra ya fue usada:
  - Informa al cliente que la letra ya fue usada
```

---

## Estructura del Proyecto

```
05_proyecto/
├── plan.md              (este archivo)
├── servidor.py          (lógica del servidor)
└── cliente.py           (lógica del cliente)
```

---

## Funcionalidades del Servidor

- [ ] Mantener lista de palabras
- [ ] Elegir palabra al iniciar
- [ ] Registrar clientes conectados
- [ ] Recibir letras de los clientes
- [ ] Verificar letras (correcta/incorrecta/repetida)
- [ ] Broadcast del estado a todos los clientes
- [ ] Determinar ganador
- [ ] Manejar desconexiones

---

## Funcionalidades del Cliente

- [ ] Conectarse al servidor
- [ ] Mostrar estado del juego (palabra, intentos, letras usadas)
- [ ] Enviar letras al servidor
- [ ] Recibir actualizaciones del servidor
- [ ] Mostrar mensajes de estado
- [ ] Mostrar resultado final

---

## Estado del juego (lo que se comparte)

```python
estado = {
    "palabra": "PROGRAMACION",    # Palabra completa (solo servidor)
    "revelada": "_ _ O _ _ A _ A _ I _ N",  # Lo que ven los clientes
    "intentos": 6,
    "letras_usadas": ["A", "O", "I"],
    "ganador": None,              # Nombre del cliente o None
    "terminado": False
}
```

---

## Protocolo de comunicación

### Cliente → Servidor
- `letra`: "A" (una letra minúscula)

### Servidor → Cliente (broadcast)
- Estado completo del juego actualizado

---

## Próximos pasos

1. [ ] Implementar servidor básico (socket, listen, accept)
2. [ ] Implementar cliente básico (conectar, enviar, recibir)
3. [ ] Agregar lógica de palabras
4. [ ] Agregar verificación de letras
5. [ ] Agregar broadcast del estado
6. [ ] Manejar ganador y fin de partida
7. [ ] Probar con múltiples clientes
8. [ ] Mejorar interfaz (opcional)
