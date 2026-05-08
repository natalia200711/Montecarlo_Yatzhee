import random

# -------------------------
# Lanzar dados
# -------------------------
def lanzar_dados():
    return [random.randint(1, 6) for _ in range(5)]

# -------------------------
# Evaluar jugada
# -------------------------
def evaluar(dados):
    conteo = {i: dados.count(i) for i in range(1, 7)}
    valores = list(conteo.values())

    if 5 in valores:
        return 50  # Yahtzee
    elif 4 in valores:
        return 40
    elif 3 in valores and 2 in valores:
        return 30  # Full house
    elif 3 in valores:
        return 25
    elif valores.count(2) == 2:
        return 20
    elif 2 in valores:
        return 10
    else:
        return sum(dados)

# -------------------------
# Turno jugador
# -------------------------
def turno():
    dados = lanzar_dados()

    for _ in range(2):  # hasta 3 lanzamientos
        dados = [d if d >= 4 else random.randint(1, 6) for d in dados]

    return evaluar(dados)

# -------------------------
# Partida
# -------------------------
def partida():
    j1 = turno()
    j2 = turno()

    if j1 > j2:
        return 1
    elif j2 > j1:
        return 2
    else:
        return 0

# -------------------------
# Montecarlo
# -------------------------
def simulacion(n):
    j1 = j2 = emp = 0

    for _ in range(n):
        ganador = partida()

        if ganador == 1:
            j1 += 1
        elif ganador == 2:
            j2 += 1
        else:
            emp += 1

    return j1, j2, emp

# -------------------------
# Ejecutar
# -------------------------
if __name__ == "__main__":
    n = 1000   #Número de simulaciones
    j1, j2, emp = simulacion(n)

    print("RESULTADOS")
    print("Jugador 1:", j1)
    print("Jugador 2:", j2)
    print("Empates:", emp)