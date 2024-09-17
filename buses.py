import os
import time
import random

# Función para limpiar la terminal en cada actualización
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para imprimir el bus en una posición específica
def draw_bus(position, track_length):
    bus = [
    "  ____________________",
    " |                    )___",
    "| [] [] [] [] [] [] []    |",
    "|_________________________|",
    "  O                  O",
    ]
    # Añadir el espacio antes del bus para simular el movimiento
    for line in bus:
        print(" " * position + line)
    # Dibujar la línea del suelo y la línea de meta
    ground = " " * position + "-" * (track_length - position) + "| META"
    print(ground)

# Función para imprimir la carrera con los buses en sus posiciones
def print_race(bus1_pos, bus2_pos, track_length):
    # Limpiar pantalla
    clear_screen()
    
    # Imprimir Bus 1
    print("Carril 1:")
    draw_bus(bus1_pos, track_length)
    
    # Separador entre carriles
    print("\n" * 2)
    
    # Imprimir Bus 2
    print("Carril 2:")
    draw_bus(bus2_pos, track_length)

# Función para mostrar el mensaje "TE AMO"
def show_love_message():
    clear_screen()
    love_message = [
    " _       _          _________   ___             ___   _________ ",
    "| |     | |        |  _____  |  \\\\\\\\           ////  |  _______) ",
    "| |     | |        | |     | |   \\\\\\\\         ////   | |  ",
    "| |     | |        | |     | |    \\\\\\\\       ////    | |_______   ",
    "| |     | |        | |     | |     \\\\\\\\     ////     |  _______)   ",
    "| |     | |        | |     | |      \\\\\\\\   ////      | |    ",
    "| |     | |_____   | |_____| |       \\\\\\\\_////       | |_______   ",
    "|_|     |_______|  |_________|        (_____)        |_________)    ",
    "",
    "                         ♥ PRINCESA ♥          ",
]
    for line in love_message:
        print(line)
    time.sleep(5)  # Dejar el mensaje unos segundos

# Longitud de la pista
track_length = 110

# Posiciones iniciales de los buses
bus1_pos = 0
bus2_pos = 0

# Meta: la posición final de la pista
goal = track_length - 1

# Simulación de la carrera
while bus1_pos < goal and bus2_pos < goal:
    # Mover los buses de manera aleatoria
    bus1_pos += random.randint(1, 3)  # Bus 1 
    bus2_pos += random.randint(1, 3)  # Bus 2

    # Asegurarse de que no sobrepasen la meta
    bus1_pos = min(bus1_pos, goal)
    bus2_pos = min(bus2_pos, goal)

    # Imprimir el estado actual de la carrera
    print_race(bus1_pos, bus2_pos, track_length)

    # Pausar un poco para controlar la velocidad
    time.sleep(0.1)

# Imprimir el resultado final
clear_screen()
print_race(bus1_pos, bus2_pos, track_length)

# Determinar el ganador
if bus1_pos >= goal and bus2_pos >= goal:
    print("¡Empate!")
elif bus1_pos >= goal:
    print("¡Bus 1 ha ganado!")
else:
    print("¡Bus 2 ha ganado!")

# Mostrar mensaje "TE AMO"
time.sleep(2)
show_love_message()
