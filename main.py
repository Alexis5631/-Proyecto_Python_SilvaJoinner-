import os
import modules.usuarios as us
import modules.utils as ut
import modules.mensajes as msj
import modules.menu as mn
import modules.juego as jg
import modules.core as cr
import modules.estadisticas as esta

if __name__ == "__main__":
    chachipun = {}
    cr.MY_DATABASE = 'data/chachipun.json'
    cr.checkFile(chachipun)
    isActive = True
    opMenu = 0
    while (isActive):
        src = cr.ReadFile()
        try:
            ut.borrar_pantalla()
            print(msj.tituloPrincipal)
            print(mn.menuPrincipal)
            opMenu = int(input(":)_"))
            match opMenu:
                case 1:
                    us.crearUsuarios(chachipun)
                case 2:
                    ut.borrar_pantalla()
                    us.mostrarJugadores()
                    o1 = input('Ingrese el nickname del jugador 1: ')
                    j1 = src[o1]["nickname"]
                    o2 = input('Ingrese el nickname del jugador 2: ')
                    j2 = src[o2]["nickname"]
                    ut.borrar_pantalla()
                    jg.unoVsUno(j1,j2)
                case 3:
                    ut.borrar_pantalla()
                    us.mostrarJugadores()
                    o1 = input('Ingrese el nickname del jugador 1: ')
                    j1 = src[o1]["nickname"]
                    jg.jugadorVsIA(j1)
                case 4:
                    esta.estadisticas()
                case 5:
                    print("Saliendo del programa....")
                    break
                case _:
                    print("La opcion es incorrecta.")
                    ut.pausar_pantalla()
        except ValueError:
            print("Error en la opcion ingresada")
            ut.borrar_pantalla()
            continue
        
        