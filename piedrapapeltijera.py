import random

# Obtener la cantidad de turnos a jugar
num_turnos = int(input("Ingrese la cantidad de turnos a jugar: "))

# Inicializar puntajes
puntaje_maquina = 0
puntaje_jugador = 0

# Jugar los turnos
for turno in range(1, num_turnos + 1):
    print(f"Turno {turno}:")
    
    # Obtener la elección del jugador
    eleccion_jugador = input("Ingrese su elección (piedra, papel o tijera): ")
    
    # Generar la elección de la máquina
    eleccion_maquina = random.choice(["piedra", "papel", "tijera"])
    
    # Determinar el ganador del turno
    if (eleccion_jugador == "piedra" and eleccion_maquina == "tijera") or \
       (eleccion_jugador == "papel" and eleccion_maquina == "piedra") or \
       (eleccion_jugador == "tijera" and eleccion_maquina == "papel"):
        ganador = "jugador"
        puntaje_jugador += 1
    elif eleccion_jugador == eleccion_maquina:
        ganador = "empate"
    else:
        ganador = "maquina"
        puntaje_maquina += 1
    
    # Mostrar el resultado del turno
    print(f"Elección del jugador: {eleccion_jugador}")
    print(f"Elección de la máquina: {eleccion_maquina}")
    print(f"Ganador del turno: {ganador}")
    print(f"Puntaje actual: Jugador {puntaje_jugador} - Máquina {puntaje_maquina}")
    print()
    
# Mostrar el puntaje final y el ganador de la partida
print("Puntaje final:")
print(f"Jugador: {puntaje_jugador}")
print(f"Máquina: {puntaje_maquina}")
if puntaje_jugador > puntaje_maquina:
    print("¡El jugador ha ganado la partida!")
elif puntaje_jugador < puntaje_maquina:
    print("¡La máquina ha ganado la partida!")
else:
    print("La partida ha terminado en empate.")
