import os 
import modules.utils as ut
import modules.core as cr

def crearUsuario(crearUsuario):
        usuarios = cr.ReadFile(nombre)
        nombre = input("Ingrese el nombre del usuario: ")
        nickname = input("Ingrese el nickname: ")
        crearUsuario = {
            'nombre': nombre,
           'nickname1': nickname,     
        }
        if nombre in usuarios:
                print(f"El nickname '{nickname}' ya esta registrado.")
        else:
                usuarios.append(nombre)
                cr.NewFile(usuarios)
                print(f"Usuario '{nickname}' registrado exitosamente.")

