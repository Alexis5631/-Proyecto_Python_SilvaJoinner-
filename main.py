import os
import modules.usuarios as us
import modules.utils as ut
import modules.mensajes as msj
import modules.menu as mn
import modules.juego as jg
import modules.core as cr

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
                    jg.unoVsUno(src, j1,j2)
                case 3:
                    jugarUnoVsIa = True
                    while(jugarUnoVsIa):
                        ut.borrar_pantalla()
                        print(msj.titulo1vsIA)
                        os.system('pause')
                case 4:
                    estadisticas = True
                    while(estadisticas):
                        ut.borrar_pantalla()
                        print(msj.tituloEstadisticas) 
                        os.system('pause')                  
                case 5:
                    pass
                case _:
                    print("La opcion es incorrecta.")
                    os.system('pause')
        except ValueError:
            print("Error en la opcion ingresada")
            ut.borrar_pantalla()
            continue
        
        