![Python Sig Intro Logo](./slides/img/banner.svg)


# Introducción
Este es mi repositorio para un pequeño taller enfocado a alumnos de primero sobre el lenguaje de programación Python.

Esta pensado para que quien quiera venir lo pueda clonar, y tener tanto las transparencias como los recursos para la pequeña practica que hemos pensado.
Para clonar el repositorio, necesitarás Git. Si usas alguna distribución de Linux, ¡es muy probable que ya lo tengas!

En caso de que uses Windows, puedes descargar el instalador desde aquí:

https://git-scm.com/


# Editor de Texto
*Como la gente de ACM es en su totalidad una manada de lobos feroces y tengo miedo de que en una de estas me coman un brazo o me arranquen la cabeza, esta sección esta editada para ser más corta, no mostrar ninguna preferencia entre Vim y Emacs, e incluir algún IDE de Python. A todo el mundo que ha hecho algún comentario: Os odio con todo mi ser.*
Para seguir la practica sin dificultades, es necesario tener un editor de texto plano instalado o un IDE para Python.

**Atom:** Facil, extensible, bonito, lento.

https://atom.io/

**VS Code**: Facil, extensible, no lo he usado nunca, lento, has de sacrificar a tu primer hijo a Bill Gates para usarlo.

https://code.visualstudio.com/

**PyCharm**(IDE): Yo empezé con PyCharm, me apaño muy bien con su debugger, solo te vale para Python.

https://www.jetbrains.com/pycharm/

**Emacs**: Mimimimi, Emacs es lo mejor, mimimimi.

https://www.gnu.org/software/emacs/

**Vim / NeoVim**: Mimimimi, no quiero que mi editor de texto sea tb un sistema operativo entero.

https://neovim.io/    |    https://www.vim.org/


# Instalar Python
Explicaremos qué hay que hacer para instalar Python en el propio taller, pero si quieres llevarlo hecho, te lo agradeceremos mucho. Sigue las instrucciones según tu sistema operativo:

### Windows
Puedes encontrar la página de descargas aquí:

https://www.python.org/downloads/

Una vez descargado el instalador, es cuestión de seguir los pasos. Si no me equivoco, el propio instalador te da la opción de añadir Python al PATH, hacedlo, que si no, no se puede acceder desde la terminal.

### MacOS
A mi no me molesta Homebrew, es un package manager para MacOS:

Lo podeis encontrar aquí: https://brew.sh/

Y una vez instalado desde la terminar hacer:
```
brew install python
```
Pero estoy seguro de que se puede instalar de forma similar a como se hace en Windows.

### Linux
Utilizad el package manager de vuestra distribución:

Para Ubuntu / Debian / Mint / PopOS!:
```
sudo apt install python3
```
Para Arch / Manjaro:
```
sudo pacman -S python
```


# Presentación
La presentación esta hecha con Marp, podéis seguirla desde cualquier navegador, abriendo el archivo 'slides/index.html'. También hay una versión en pdf en la misma carpeta.


# Game of Life
La actividad que hemos pensado para este taller, es pediros que programéis la lógica del Juego de la Vida de Conway:

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules

Para ello, tenéis tres archivos en la carpeta 'code':

Archivo | Descripción
------- | -----------
\_\_main\_\_.py | Es el archivo que debéis ejecutar cuando queréis probar vuestro programa, en teoría no deberíais necesitar modificarlo.
gui.py | Es la implementación de la pequeña interfaz gráfica que os damos para que podáis ver lo que está haciendo vuestro código. Podéis verlo si queréis, pero no es mi código más limpio. :S
config.json | Aqui estan las opciones del programa. La mayoria son colores y tamaños, pero la primera es importante. Escribir "mode": "matrix" si vais a trabajar con una matriz y "mode": "set" si vais a trabajar con un set.
game.py | Este es vuestro archivo. El que tenéis que editar.

La actividad consiste en escribir una función en 'game.py' llamada 'next_step' que reciba como parámetro uno de los siguientes:
- Una matriz de 1s y 0s con 20 filas y 20 columnas representando las células vivas y muertas.
- Un set de tuplas con las coordenadas de las células activas.

Y aplique sobre ese parámetro las reglas del juego.
