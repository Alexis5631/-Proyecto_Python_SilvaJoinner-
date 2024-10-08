import modules.utils as ut
import modules.core as cr
import modules.mensajes as msg

# Función para crear usuarios y añadirlos al diccionario `chachipun`
def crearUsuarios(chachipun):
    while True:
        ut.borrar_pantalla()
        print(msg.tituloRegistrar)
        nombre = input("Ingrese el nombre del usuario: ")
        nickname = input("Ingrese el nickname: ")
        
        # Crear la estructura del usuario
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
        
        # Añadir el nuevo usuario al diccionario `chachipun`
        chachipun[nickname] = nuevoUsuario
        
        # Guardar los datos de los usuarios en algún archivo o base de datos
        cr.AddData(chachipun)
        
        # Preguntar si se desea agregar otro usuario
        confirmacion = input("Desea agregar otro usuario S(Si) N(No): ").lower()
        if confirmacion == 's':
            continue
        else:
            break

def mostrarJugadores():
    gameData = cr.ReadFile()
    print("Jugadores registrados:")
    for nickname, datos in gameData.items():
        print(f"Nickname: {nickname}, Nombre: {datos['nombre']}")
