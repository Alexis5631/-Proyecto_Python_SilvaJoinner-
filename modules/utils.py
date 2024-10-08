import sys
import os

def validateData(message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que usted ingreso no esta permitida.......')
            validateData()
        elif (accion== 'N'): 
            flagFunction = True
        elif  (accion == 'S'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateData(message)

def validateResponse(message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que usted ingreso no esta permitida.......')
            validateData()
        elif (accion== 'S', 's'): 
            flagFunction = True
        elif  (accion == 'N', 'n'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateResponse(message)


def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")