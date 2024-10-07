import os
import json

MY_DATABASE = None

def NewFile(*param):
    with open(MY_DATABASE, "W") as wf:
        json.dump(param[0], wf, indent=4)

def ReadFile():
    with open(MY_DATABASE, "r") as rf:
        return json.load(rf)
    
def checkFile(*param):
    data = list(param)
    if os.path.isfile(MY_DATABASE):
        if len(param):
            data[0].update(ReadFile())
    else:
        if len(param):
            NewFile(data[0])
def guardar_partida(juego):
    NewFile(juego)
def cargar_partida():
    juego = {
        'Maquina':{
            'partidasGanadas': 0,
            'partidasPerdidas': 0,
            'partidasJugadas': 0
        },
        'usuarios': {}
    }
    checkFile(juego)
    return juego