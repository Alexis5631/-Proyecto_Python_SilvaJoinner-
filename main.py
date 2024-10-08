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
        try:
            ut.borrar_pantalla()
            print(msj.tituloPrincipal)
            print(mn.menuPrincipal)
            opMenu = int(input(":)_"))
            match opMenu:
                case 1:
                    us.crearUsuarios(chachipun)
                case 2:
                    pass
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
        
        