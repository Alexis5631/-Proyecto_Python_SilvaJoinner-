import os
import random
import modules.usuarios as us

opciones = ["piedra", "papel", "tijera"]


def determinarGanador(jugador1, eleccion1, jugador2, eleccion2):
    if eleccion1 == eleccion2:
        print ("Empate")
        return
    elif (eleccion1 == "piedra" and eleccion2 == "tijera"):
        (eleccion1 == "tijera" and eleccion2 == "papel")
        (eleccion1 == "papel" and eleccion2 == "piedra")
        print (f"'{jugador1}' Gana!")
        return
    else:
        print(f"'{jugador2}' Gana!")

def usuarioVsUsuario():


  
#def usuarioVsMaquina():
    pass