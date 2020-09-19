import sys, pygame
from time import sleep

pygame.init()    # Start PyGame

width, height = 412, 412    # Initial size of the window.
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

game_width = 20
game_height = 20
cell_size = 20
cell_offset = [0, 0]


def draw_grid(screen, start_x, start_y, width, height, cell_size):
    for x in range(width + 1):
        pygame.draw.line(screen, (200, 200, 200),
                (start_x + (cell_size * x), start_y), (start_x + (cell_size * x), start_y + (height * cell_size)), 2)
    for y in range(height + 1):
        pygame.draw.line(screen, (200, 200, 200),
                (start_x, start_y + (cell_size * y)), (start_x + (width * cell_size), start_y + (cell_size * y)), 2)

def get_cell_number(absolute_position, start_xy):
    absolute_position = [absolute_position[i] - start_xy[i] for i in [0, 1]]
    game_size = [game_width, game_height]
    return [int(absolute_position[i] / game_size[i]) for i in [0, 1]]

def get_rel_cell_position(cell_position, moved, start_xy, cell_size):
    rel_position = [cell_position[i] - moved[i] for i in [0, 1]]
    x, y = ((rel_position[i] * cell_size) + start_xy[i] for i in [0, 1])
    return [x, y]

def draw_cells(screen, cells, start_xy):
    for cell in cells:
        rect = pygame.Rect(get_rel_cell_position(cell, cell_offset, start_xy, cell_size), (20, 20))
        pygame.draw.rect(screen, (245, 224, 66), rect)

def main(get_cells):
    cells = set()
    global width, height
    global screen
    global game_width, game_height, cell_size, cell_offset

    while True:
        play = False
        start_x = int((width - (game_width * cell_size)) / 2)
        start_y = int((height - (game_height * cell_size)) / 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.__dict__['size']
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN and not play:
                pos = list(event.__dict__['pos'])
                cells.add(tuple(get_cell_number(pos, [start_x, start_y])))
            elif event.type == pygame.KEYDOWN:
                add = {'w': (0, 1), 'a': (-1, 0), 's': (0, -1), 'd': (1, 0)}
                if event.__dict__['unicode'] in add:
                    cell_offset = [cell_offset[i] + add[event.__dict__['unicode']][i] for i in [0, 1]]
                elif event.__dict__['unicode'] == 'n' and not play:
                    get_cells(cells)
                elif event.__dict__['unicode'] == 'p':
                    play = not play 
        if play:
            get_cells(cells)
            wait(0.6)
        screen.fill((50, 50, 50))
        draw_grid(screen, start_x, start_y, game_width, game_height, cell_size)
        draw_cells(screen, cells, (start_x, start_y))
        pygame.display.flip()
        sleep(0.015)
