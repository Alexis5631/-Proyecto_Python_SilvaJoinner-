import random
import modules.core as cr
import modules.usuarios as us 
import modules.utils as ut

opciones = ['piedra', 'papel', 'tijera']

# Función para determinar el ganador de una ronda
def determinarGanadorUnoVsUno(eleccionJugador1, eleccionJugador2):
    if eleccionJugador1 == eleccionJugador2:
        return "empate"
    if (eleccionJugador1 == 'piedra' and eleccionJugador2 == 'tijera') or (eleccionJugador1 == 'papel' and eleccionJugador2 == 'piedra') or (eleccionJugador1 == 'tijera' and eleccionJugador2 == 'papel'):
        return "jugador1"
    else:
        return "jugador2"

def unoVsUno(nicknameJugador1, nicknameJugador2):
    jugador1GanaConsecutivas = 0
    jugador2GanaConsecutivas = 0
    jugador1Escudo = False
    jugador2Escudo = False

    rondasJugador1 = 0
    rondasJugador2 = 0
    us.mostrarJugadores()
    jugador1 = nicknameJugador1
    jugador2 = nicknameJugador2

    while rondasJugador1 < 3 and rondasJugador2 < 3:
        ut.borrar_pantalla()
        eleccionJugador1 = input(f"{jugador1}, elige entre piedra, papel o tijera: ").lower()
        if eleccionJugador1 not in opciones:
            print("Opción inválida, intenta de nuevo.")
            continue

        eleccionJugador2 = input(f"{jugador2}, elige entre piedra, papel o tijera: ").lower()
        if eleccionJugador2 not in opciones:
            print("Opción inválida, intenta de nuevo.")
            continue

        resultado = determinarGanadorUnoVsUno(eleccionJugador1, eleccionJugador2)

        if resultado == "empate":
            print(f"Es un empate - {jugador1}: {rondasJugador1} y {jugador2}: {rondasJugador2}")
            ut.pausar_pantalla()
            jugador1GanaConsecutivas = 0
            jugador2GanaConsecutivas = 0

        elif resultado == "jugador1":
            jugador1GanaConsecutivas += 1
            jugador2GanaConsecutivas = 0
            if jugador1GanaConsecutivas == 2:
                jugador1Escudo = True
                print(f"{jugador1} ha obtenido un escudo.")
            if jugador2Escudo:
                jugador2Escudo = False
                print(f"{jugador2} tenía un escudo, así que se anula el punto.")
            else:
                rondasJugador1 += 1
                print(f"Punto para {jugador1} = {jugador1}: {rondasJugador1} y {jugador2}: {rondasJugador2}")
            ut.pausar_pantalla()

        elif resultado == "jugador2":
            jugador2GanaConsecutivas += 1
            jugador1GanaConsecutivas = 0
            if jugador2GanaConsecutivas == 2:
                jugador2Escudo = True
                print(f"{jugador2} ha obtenido un escudo.")
            if jugador1Escudo:
                jugador1Escudo = False
                print(f"{jugador1} tenía un escudo, así que se anula el punto.")
            else:
                rondasJugador2 += 1
                print(f"Punto para {jugador2} = {jugador2}: {rondasJugador2} y {jugador1}: {rondasJugador1}")
    if rondasJugador1 == 3:
        print(f"¡{jugador1} ha ganado el juego!")
    else:
        print(f"¡{jugador2} ha ganado el juego!")

def determinarGanadorVsMaquina(elecionJugador1, eleccionMaquina):
    if elecionJugador1 == eleccionMaquina:
        return "empate"
    if (elecionJugador1 == 'piedra' and eleccionMaquina == 'tijera' ) or (elecionJugador1 == 'papel' and eleccionMaquina == 'piedra') or (elecionJugador1 == 'tijera' and eleccionMaquina == 'papel'):
        return "jugador1"
    else:
        return "IA"

def jugadorVsIA(nicknameJugador1):
    jugador1GanaConsecutivas = 0
    maquinaGanaConsecutivas = 0
    jugadorEscudo = False
    maquinaEscudo = False

    rondasJugador1 = 0
    rondasMaquina = 0
    us.mostrarJugadores()
    jugador1 = nicknameJugador1

    while rondasJugador1 < 3 and rondasMaquina < 3:
        ut.borrar_pantalla()
        eleccionJugador1 = input(f"{jugador1}, elige entre piedra, papel o tijera: ").lower()
        if eleccionJugador1 not in opciones:
            print("Opción inválida, intenta de nuevo.")
            continue

        eleccionMaquina = random.choice(opciones)
        print(f"La máquina eligió {eleccionMaquina}")
        ut.pausar_pantalla()

        resultado = determinarGanadorVsMaquina(eleccionJugador1, eleccionMaquina)

        if resultado == "empate":
            print(f"Es un empate - {jugador1}: {rondasJugador1} y IA: {rondasMaquina}")
            ut.pausar_pantalla() 
            jugador1GanaConsecutivas = 0
            maquinaGanaConsecutivas = 0

        elif resultado == "jugador1":
            jugador1GanaConsecutivas += 1
            maquinaGanaConsecutivas = 0
            if jugador1GanaConsecutivas == 2:
                jugadorEscudo = True
                print(f"{jugador1} Ha obtenido un escudo.")
                ut.pausar_pantalla()
            if maquinaEscudo:
                maquinaEscudo = False
                print("La IA tenía un escudo, así que se anula el punto.")
                ut.pausar_pantalla()
            else:
                rondasJugador1 += 1
                print(f"Punto para {jugador1} = {jugador1}: {rondasJugador1} y IA: {rondasMaquina}")
                ut.pausar_pantalla()

        elif resultado == "IA":
            maquinaGanaConsecutivas += 1
            jugador1GanaConsecutivas = 0
            if maquinaGanaConsecutivas == 2:
                maquinaEscudo = True
                print("La maquina ha obtenido un escudo.")
                ut.pausar_pantalla()
                
            if jugadorEscudo:
                jugadorEscudo = False
                print(f"{jugador1} tenía un escudo, así que se anula el punto.")
                ut.pausar_pantalla()
            else:
                rondasMaquina += 1
                print(f"Punto para la IA = IA: {rondasMaquina} y {jugador1}: {rondasJugador1}")
                ut.pausar_pantalla()
