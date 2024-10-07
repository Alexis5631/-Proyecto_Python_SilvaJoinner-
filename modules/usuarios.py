import os 

def crearUsuario():
    usuario1 = input("Ingrese el nombre del usuario 1: ")
    nickname1 = input("Ingrese el nickname: ")
    usuario2 = input("Ingrese el nombre del usuario 2: ")
    nickname2 = input("Ingrese el nickname: ")
    añadirUsuario = {
        'nombre': usuario1,
        'nickname1': nickname1,
        'nombre2': usuario2,
        'nickname2': nickname2       
    }

    print("Usuarios registrados con exito.")

