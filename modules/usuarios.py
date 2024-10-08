import os 
import json
import modules.utils as ut


MY_DATABASE = 'modules/data/jugadores.json'

def cargarUsuarios():
    try:
        with open(MY_DATABASE, "r") as rf:
            usuarios = json.load(rf)
    except FileNotFoundError:
        usuarios = {}
    return usuarios
        
def guardarUsuario(usuarios):
    with open(MY_DATABASE, "w") as wf:
        json.dump(usuarios, wf, indent=4)


def validarUsuarios(nickname, usuarios):
        if nickname not in usuarios:
              return True
        else:
              print(f"El nickname '{nickname}' ya esta registrado.")
              return False
              
              

def crearUsuarios(usuarios):
        nombre = input("Ingrese el nombre del usuario: ")
        nickname = input("Ingrese el nickname: ")
        
        nuevoUsuario = {
            'nombre': nombre,
           'nickname': nickname,     
        }
        if validarUsuarios(nickname, usuarios):
               print(f"Bienvenido {nickname}")
               usuarios [nickname] = 'nuevoUsuario'
               guardarUsuario(usuarios)
               
