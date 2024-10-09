# Piedra, Papel o Tijera - Juego Interactivo

Este es un juego de Piedra, Papel o Tijera entre dos jugadores, que se ejecuta en la terminal. Los jugadores pueden ser humanos o una IA que elige opciones de manera aleatoria. El juego implementa un sistema de rondas y escudos, donde los jugadores pueden ganar puntos y obtener escudos tras ganar dos rondas consecutivas.

## Estructura del Proyecto

- `main.py`: El archivo principal que maneja la lógica del menú y las interacciones del jugador.
- `modules/`: Contiene varios módulos importantes:
  - `usuarios.py`: Este código gestiona la creación y el registro de usuarios para un juego de "Piedra, Papel o Tijera". Utiliza funciones para crear nuevos usuarios y mostrar la lista de jugadores registrados.

Función crearUsuarios(chachipun):
Permite crear nuevos usuarios y añadirlos a un diccionario llamado chachipun.
Solicita al usuario que ingrese su nombre y un apodo (nickname) único.
Crea un diccionario para almacenar los datos del usuario, que incluye su nombre, apodo y estadísticas iniciales (partidas ganadas, perdidas y puntos).
Guarda la información de los usuarios en un archivo o base de datos mediante la función cr.AddData(chachipun).
Ofrece la opción de agregar más usuarios o finalizar el registro.
Función mostrarJugadores():

Lee los datos de los usuarios desde un archivo o base de datos usando cr.ReadFile().
Imprime en la consola una lista de jugadores registrados, mostrando su nickname y nombre.

  - `utils.py`: Este código contiene dos funciones que manejan la visualización de la pantalla en un entorno de consola. Estas funciones son útiles para limpiar la pantalla y pausar la ejecución del programa, mejorando así la experiencia del usuario al interactuar con la aplicación.

Función borrar_pantalla():

Se encarga de limpiar la consola, eliminando todo el texto mostrado anteriormente.
Utiliza el módulo os para ejecutar comandos del sistema operativo:
Si el sistema operativo es Linux o macOS (darwin), se ejecuta el comando clear.
Para Windows, se utiliza el comando cls.
Esta función es útil para mantener la interfaz limpia y enfocada, especialmente en juegos o aplicaciones de consola que requieren múltiples interacciones.

Función pausar_pantalla():

Detiene la ejecución del programa y espera a que el usuario presione una tecla antes de continuar.
En Linux o macOS, solicita al usuario que presione una tecla usando input().
En Windows, utiliza os.system("pause"), que muestra el mensaje "Presione una tecla para continuar..." en la consola y espera a la interacción del usuario.
Esta función es especialmente útil para permitir que los usuarios lean mensajes importantes antes de continuar con la ejecución.

  - `mensajes.py`: Este código define varios títulos artísticos en formato ASCII que se utilizan probablemente como encabezados para diferentes secciones de un juego de "Piedra, Papel o Tijera". Los títulos están organizados en varias categorías que representan distintas funcionalidades o estados del juego.

tituloPrincipal: El título principal del juego, que se muestra al inicio y establece el tema general.

tituloRegistrar: Título para la sección donde los jugadores pueden registrarse o ingresar sus apodos.

tituloPvP: Encabezado que se muestra en la modalidad de juego entre dos jugadores humanos (Player vs Player).

tituloEstadisticas: Título para la sección que presenta estadísticas del juego, posiblemente mostrando el rendimiento de los jugadores.

titulo1vsIA: Encabezado que se muestra en la modalidad donde un jugador humano compite contra la inteligencia artificial (IA).

  - `menu.py`: Este código define un menú principal en formato de texto, que se presenta al usuario como opciones para interactuar con el juego de "Piedra, Papel o Tijera". Las opciones del menú están numeradas y cada una corresponde a una funcionalidad específica del juego.

Registrar Usuario: Opción para que nuevos jugadores se registren o ingresen sus apodos para participar en el juego.

Jugar 1 vs 1: Opción que permite a dos jugadores competir entre sí en un juego de "Piedra, Papel o Tijera".

Jugar contra la máquina: Opción que permite a un jugador competir contra una inteligencia artificial, que elegirá de manera aleatoria entre piedra, papel o tijera.

Estadísticas: Opción para mostrar las estadísticas del juego, lo que puede incluir información sobre victorias, empates y derrotas de los jugadores.

Salir: Opción para cerrar el juego y salir del programa.

Funcionalidad
Este menú proporciona una interfaz clara y sencilla para que los usuarios seleccionen cómo desean interactuar con el juego. Facilita la navegación y mejora la experiencia del usuario al ofrecer distintas formas de jugar y acceder a información relevante.

  - `juego.py`: Este código implementa un juego de "Piedra, Papel o Tijera" que permite jugar en dos modalidades: entre dos jugadores humanos y contra la maquina (IA).

determinarGanadorUnoVsUno(eleccionJugador1, eleccionJugador2): Esta función evalúa las elecciones de los dos jugadores y determina el ganador de la ronda, o si hubo un empate.

unoVsUno(nicknameJugador1, nicknameJugador2): Maneja la lógica del juego entre dos jugadores humanos. Lleva un registro de las rondas ganadas y de los "escudos" obtenidos por los jugadores tras ganar consecutivas, y declara al ganador cuando uno de los jugadores gana 3 rondas.

determinarGanadorVsMaquina(elecionJugador1, eleccionMaquina): Similar a la función para dos jugadores, pero esta evalúa la elección del jugador humano frente a la elección aleatoria de la IA.

jugadorVsIA(nicknameJugador1): Permite al jugador humano competir contra la IA. Similar a la función de dos jugadores, gestiona las rondas, los escudos y el resultado final del juego.

Características del Juego:
Cada jugador puede acumular hasta tres victorias para ganar el juego.
Se introducen mecánicas de "escudos" que permiten anular puntos si un jugador gana dos rondas consecutivas.
La IA elige sus movimientos de forma aleatoria, lo que añade un elemento de sorpresa al juego.

  - `core.py`: Este código implementa un módulo para gestionar un archivo JSON que actúa como base de datos para almacenar información relacionada con el juego "Piedra, Papel o Tijera". El código incluye las siguientes funciones:

NewFile(*param): Crea un nuevo archivo JSON y escribe el contenido proporcionado en él. Se espera que el primer argumento sea un diccionario que se guardará en el archivo.

ReadFile(): Lee el contenido del archivo JSON y lo devuelve como un diccionario. Esta función se utiliza para acceder a los datos almacenados.

checkFile(*param): Verifica si el archivo JSON existe. Si existe y se proporcionan parámetros, actualiza el contenido existente con los nuevos datos. Si el archivo no existe, crea uno nuevo con los datos proporcionados.

AddData(chachipun): Sobrescribe el contenido del archivo JSON con el nuevo contenido proporcionado. Se utiliza para actualizar o reemplazar completamente los datos almacenados.

  - `estadisticas.py`: Funciones para registrar y mostrar estadísticas del juego.

## Características

- **Modos de Juego**:
  - Juega contra otro jugador en modo local.
  - Juega contra la IA que selecciona aleatoriamente `piedra`, `papel` o `tijera`.
  
- **Sistema de Puntos y Escudos**:
  - Los jugadores ganan una ronda al vencer al otro jugador.
  - Si un jugador gana dos rondas consecutivas, obtiene un escudo que puede protegerlo en la siguiente ronda.

- **Registro de Jugadores**:
  - Los jugadores se registran por sus "nickname" y se almacenan en el archivo `chachipun.json`.