# Inteligencia Artificail — IA con Minimax y Alfa-Beta

Juego de Conecta Cuatro en consola donde el jugador se enfrenta a una IA que utiliza los algoritmos **Minimax** y **Alfa-Beta Pruning** para elegir su jugada óptima.

---

## Estructura del proyecto

```
connect4/
├── Connect4.py   # Lógica del tablero y reglas del juego
├── agents.py     # Algoritmos de búsqueda: Minimax y Alfa-Beta
└── main.py       # Punto de entrada, loop principal del juego
```

---

## Requisitos

- Python 3.8+
- [NumPy](https://numpy.org/)

Instala la dependencia con:

```bash
pip install numpy
```

---

## Cómo jugar

```bash
python main.py
```

El tablero se muestra en consola. Cuando sea tu turno, ingresa el número de columna (0–6) donde quieres colocar tu ficha. La IA responderá automáticamente.

```
¡Bienvenido a Connect Four!
La IA usa Alfa-Beta con profundidad 5.

Tu movimiento [0, 1, 2, 3, 4, 5, 6]: 3
Turno de la IA → columna 3
```

---

## Algoritmos implementados

### Minimax (`minimax`)
Explora el árbol de juego de forma exhaustiva hasta una profundidad dada. El agente maximizador representa a la IA y el minimizador al jugador humano. Sin poda, el número de nodos visitados puede ser muy alto.

### Alfa-Beta Pruning (`alphabeta`)
Optimización del Minimax que descarta ramas del árbol que no pueden mejorar el resultado ya conocido, reduciendo drásticamente los nodos evaluados sin alterar la decisión final.

Ambos algoritmos terminan antes de la profundidad máxima si detectan un estado **terminal** (victoria, derrota o empate).

### Función de evaluación heurística (`evaluate`)
Usada por Alfa-Beta cuando se alcanza el límite de profundidad sin llegar a un estado terminal. Puntúa el tablero según:

| Criterio | Puntos |
|---|---|
| Fichas propias en el centro | +6 por ficha |
| 3 propias + 1 vacío en ventana de 4 | +50 |
| 2 propias + 2 vacíos en ventana de 4 | +10 |
| 3 del rival + 1 vacío en ventana de 4 | -80 |

Las ventanas se evalúan en las cuatro direcciones: horizontal, vertical y ambas diagonales.

---

## Parámetros configurables

En `main.py` puedes ajustar la profundidad de búsqueda:

```python
depth = 5  # Aumentar para mayor dificultad (más lento)
```

| Profundidad | Dificultad | Velocidad aproximada |
|---|---|---|
| 3 | Fácil | Muy rápida |
| 5 | Media | Rápida |
| 7 | Difícil | Lenta |

---

## Ejemplo de salida

```
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 1 2 0 0 0]]

Nodos visitados (Alfa-Beta): 18423
Turno de la IA → columna 4
```

---

## Constantes del juego

Definidas en `Connect4.py`:

```python
ROWS         = 6
COLS         = 7
EMPTY_SPACE  = 0
PLAYER_TAKEN = 1
IA_TAKEN     = 2
```
