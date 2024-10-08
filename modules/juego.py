import modules.core as cr
import random
import modules.usuarios as us 
import modules.utils as ut

opciones = ['piedra', 'papel', 'tijera']

# Función para determinar el ganador de una ronda
def determinarGanador(elecionJugador1, eleccionJugador2):
    if elecionJugador1 == eleccionJugador2:
        print("Empate")
    if (elecionJugador1 == 'piedra' and eleccionJugador2 == 'tijera' ) or (elecionJugador1 == 'papel' and eleccionJugador2 == 'piedra') or (elecionJugador1 == 'tijera' and eleccionJugador2 == 'papel'):
        print("Punto para ")
    else:
        print("jugador2")
        
jugador1GanaConsecutivas = 0
jugador2GanaConsecutivas = 0
jugador1Escudo = False
jugador2Escudo = False

rondasJugador1 = 0
rondasJugador2 = 0       
   
def unoVsUno(chachipun, nicknameJugador1, nicnameJugador2):
    ut.borrar_pantalla()
    us.mostrarJugadores()
    jugador1 = nicknameJugador1
    jugador2 = nicnameJugador2
    
    while rondasJugador1 < 3 and rondasJugador2 < 3:
        eleccionJugador1 = input(f"{jugador1}, elige entre piedra, papel o tijera: ").lower()
        if eleccionJugador1 not in opciones:
            print("Opcion invalida, intenta de nuevo.")
            continue
        
        eleccionJugador2 = input(f"{jugador2}, Elige entre piedra, papel o tijera: ").lower()
        if eleccionJugador2 not in opciones:
            print("Opcion invalida, intenta de nuevo.")
            continue
        
        resultado = determinarGanador(eleccionJugador1, eleccionJugador2)
        if resultado == "empate":
            print(f"Es un empate")
            jugador1GanaConsecutivas = 0
            jugador2GanaConsecutivas = 0
        elif resultado == "jugador1":
            if jugador2Escudo:
                print(f"{jugador1} estaba protegido por su escudo!")
                jugador2Escudo = False