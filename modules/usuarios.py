import os 
import modules.utils as ut

def crearUsuario(crearUsuario):
        usuario = input("Ingrese el nombre del usuario: ")
        nickname = input("Ingrese el nickname: ")
        crearUsuario = {
            'nombre': usuario,
            'nickname1': nickname,     
        }
        print("Usuarios registrados con exito.")

