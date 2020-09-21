from gui import main
from game import next_step

# Cambia esto a:
#   'set' si vas a trabajar con un set de coordenadas.
#   'matrix si vas a trabajar con una matriz de 1s y 0s.
mode = 'matrix'

if __name__ == '__main__':
    main(next_step, mode)


