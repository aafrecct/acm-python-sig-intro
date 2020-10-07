# Devuelve la variable cells, tras aplicarle las reglas
# de un ciclo del juego de la vida.


def get_surrounding_cells(cell):
    sc = {(cell[0] + x, cell[1] + y) for x in (-1, 0, 1) for y in (-1, 0, 1)}
    sc.remove(cell)
    return sc


def get_cells_to_check(cells):
    ctc = set(cells)
    for c in cells:
        for c2 in get_surrounding_cells(c):
            ctc.add(c2)
    return ctc

def check_cell(cell, cells):
    ac = 0
    for c in get_surrounding_cells(cell):
        if c in cells:
            ac += 1
    if cell in cells:
        return 1 < ac < 4
    else:
        return ac == 3


def next_step(cells):
    oc = set(cells)
    for c in get_cells_to_check(oc):
        if check_cell(c, oc):
            cells.add(c)
        elif c in oc:
            cells.remove(c)
