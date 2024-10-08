import os
import modules.usuarios as us
import modules.utils as ut
import modules.mensajes as msj
import modules.menu as mn
import modules.juego as jg

if __name__ == "__main__":
    chachipun = []
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            os.system('cls')
            print(msj.tituloPrincipal)
            print(mn.menuPrincipal)
            opMenu = int(input(":)_"))
            match opMenu:
                case 1:
                    jugarUnoVsUno = True
                    while(jugarUnoVsUno):
                        os.system('cls')
                        print(msj.tituloPvP)
                        jg.usuarioVsUsuario()
                case 2:
                    jugarUnoVsIa = True
                    while(jugarUnoVsIa):
                        os.system('cls')
                        print(msj.titulo1vsIA)
                        os.system('pause')
                case 3:
                    estadisticas = True
                    while(estadisticas):
                        os.system('cls')
                        print(msj.tituloEstadisticas) 
                        os.system('pause')                  
                case 4:
                    pass
                case _:
                    print("La opcion es incorrecta.")
                    os.system('pause')
        except ValueError:
            print("Error en la opcion ingresada")
            os.system('cls')
            continue
        
        