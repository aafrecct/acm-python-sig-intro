![Python Sig Intro Logo](./slides/img/banner.svg)


# Introducción
Este es mi repositorio para un pequeño taller enfocado a alumnos de primero sobre el lenguaje de programación Python.

Esta pensado para que quien quiera venir lo pueda clonar, y tener tanto las transparencias como los recursos para la pequeña practica que hemos pensado.
Para clonar el repositorio, necesitarás Git. Si usas alguna distribución de Linux, ¡es muy probable que ya lo tengas!

En caso de que uses Windows, puedes descargar el instalador desde aquí:

https://git-scm.com/


# Editor de Texto
Para seguir la practica sin dificultades, es necesario tener un editor de texto plano instalado. Yo estoy acostumbrandome a usar Vim para la mayoría de cosas, porque me gusta, pero no es la herramienta más intuitiva si apenas estáis empezando. Si queréis herramientas de calidad que probablemente podais usar durante toda la carrera estas son mis recomendaciones:

### Atom
Atom es un editor de texto muy fácil de usar que permite mucha personalización y tiene tropecientas extensiones. Sus puntos fuertes tienen el mismo origen que sus puntos débiles: Esta hecho con Electron, es decir en realidad toda su interfaz es una pagina web. Esto significa que puede ser muy bonito, pero en lineas generales, tarda bastante en iniciarse. Para mí, esto nunca ha sido un problema. Podéis descargarlo aquí:

https://atom.io/

### VS Code
Se ha hecho muy popular recientemente, también esta hecho sobre Electron. Nunca lo he usado, pero la poca gente te que he visto que lo usa está contenta. Yo le veo más o menos las mismas ventajas y desventajas que a Atom.

https://code.visualstudio.com/

### Emacs
Este es un poco más difícil de recomendar, Emacs es más complicado que los dos anteriores, pero se inicia claramente más rápido. La mayoría de mis compañeros en ACM están enamorados de Emacs. Lo cierto es que una vez le coges cariño no hay nada que Emacs no pueda hacer, pero de primeras es el más feo y duro hasta ahora.

https://www.gnu.org/software/emacs/

### Vim / NeoVim ([@FORGIS98](https://github.com/FORGIS98 "Pagina de usuario de FORGIS98"))
Odiado por muchos y amado por otros. Es complicado (al igual que Emacs) pero a diferencia de este requiere de unas horas (o días) de práctica antes de tener cierta soltura al programar. Sin embargo, las horas invertidas previamente, desbloquean un poder inigualable. ¿Vim o NeoVim? En pocas palabras, NeoVim tiene el mismo corazón (código) que Vim, pero con añadidos potentes que lo han hecho crecer rápidamente entre los amantes de Vim.

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
