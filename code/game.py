# Devuelve la variable cells, tras aplicarle las reglas
# de un ciclo del juego de la vida.
def next_step(cells):
    old_cells = {cell for cell in cells}

    for cell in old_cells:
        cells.add((cell[0], cell[1] + 1))
