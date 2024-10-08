import modules.core as cr
import random
import modules.usuarios as us 

# Función para determinar el ganador de una ronda
def determinarGanador(eleccion_jugador1, eleccion_jugador2):
    if eleccion_jugador1 == eleccion_jugador2:
        print("Empate")
        return
    if (eleccion_jugador1 == 'piedra' and eleccion_jugador2 == 'tijera') or (eleccion_jugador1 == 'tijera' and eleccion_jugador2 == 'papel') or (eleccion_jugador1 == 'papel' and eleccion_jugador2 == 'piedra'):
        print("jugador1")
        return
    else:
        print("jugador2")
        return

# Función principal para el juego
def piedraPapelTijera(chachipun, nicknameJugador1, nicknameJugador2):
    # Obtener los jugadores del diccionario `chachipun`
    jugador1 = chachipun.get(nicknameJugador1)
    jugador2 = chachipun.get(nicknameJugador2)
    
    # Verificar si ambos jugadores existen
    if not jugador1:
        print(f"El jugador {nicknameJugador1} no existe. Debe registrarse primero.")
        return
    if not jugador2:
        print(f"El jugador {nicknameJugador2} no existe. Debe registrarse primero.")
        return

    # Variables para las rondas
    rondasJugador1 = 0
    rondasJugador2 = 0
    jugador1Escudo = False
    jugador2Escudo = False
    jugador1GanaConsecutivas = 0
    jugador2GanaConsecutivas = 0

    opciones = ['piedra', 'papel', 'tijera']

    # Mientras ninguno gane 3 rondas
    while rondasJugador1 < 3 and rondasJugador2 < 3:
        eleccionJugador1 = input(f"{jugador1['nombre']}, elige piedra, papel o tijera: ").lower()
        if eleccionJugador1 not in opciones:
            print("Opción inválida, intenta de nuevo.")
            continue
        
        eleccionJugador2 = input(f"{jugador2['nombre']}, elige piedra, papel o tijera: ").lower()
        if eleccionJugador2 not in opciones:
            print("Opción inválida, intenta de nuevo.")
            continue
        
        resultado = determinarGanador(eleccionJugador1, eleccionJugador2)
        
        if resultado == "empate":
            print("Es un empate. Las rachas se reinician.")
            jugador1GanaConsecutivas = 0
            jugador2GanaConsecutivas = 0
        elif resultado == "jugador1":
            if jugador2Escudo:
                print(f"{jugador2['nombre']} estaba protegido por su escudo!")
                jugador2Escudo = False
            else:
                print(f"{jugador1['nombre']} gana esta ronda!")
                rondasJugador1 += 1
                jugador1GanaConsecutivas += 1
                jugador2GanaConsecutivas = 0

                if jugador1GanaConsecutivas == 2:
                    print(f"{jugador1['nombre']} ha ganado dos rondas consecutivas! Ahora tiene un escudo.")
                    jugador1Escudo = True
        else:
            if jugador1Escudo:
                print(f"{jugador1['nombre']} estaba protegido por su escudo!")
                jugador1Escudo = False
            else:
                print(f"{jugador2['nombre']} gana esta ronda!")
                rondasJugador2 += 1
                jugador2GanaConsecutivas += 1
                jugador1GanaConsecutivas = 0

                if jugador2GanaConsecutivas == 2:
                    print(f"{jugador2['nombre']} ha ganado dos rondas consecutivas! Ahora tiene un escudo.")
                    jugador2Escudo = True
    
    # Alguien ganó 3 rondas, actualizar la información de la partida
    if rondasJugador1 == 3:
        print(f"¡Felicidades {jugador1['nombre']}! Ganaste la partida.")
        jugador1['partidasGanadas'] += 1
        jugador2['partidasPerdidas'] += 1
        jugador1['totalPuntos'] += 2
    else:
        print(f"¡Felicidades {jugador2['nombre']}! Ganaste la partida.")
        jugador2['partidasGanadas'] += 1
        jugador1['partidasPerdidas'] += 1
        jugador2['totalPuntos'] += 2

    # Guardar los cambios en el archivo usando `cr.AddData()`
    cr.AddData(chachipun)
