import modules.utils as ut
import modules.core as cr
import modules.mensajes as msg

def crearUsuarios(chachipun):
    while True:
        ut.borrar_pantalla()
        print(msg.tituloRegistrar)
        nombre = input("Ingrese el nombre del usuario: ")
        nickname = input("Ingrese el nickname: ")
        nuevoUsuario = {
            'nombre': nombre,
           'nickname': nickname,  
           'partidasGanadas': 0,
           'partidasPerdidas': 0,
           'totalPuntos': 0,
           'partidasGanadasIA': 0,
           'partidasPerdidasIA': 0,
           'totalPuntosIA': 0
        }
        chachipun[nickname] = nuevoUsuario
        cr.AddData(chachipun)
        confirmacion = input("Desea agregar otro usuario S(Si) N(No): ")
        if confirmacion == ('S' or 's'):
            continue
        else:
              break