import sys, pygame
from time import sleep
from json import load


# Load the options from 'config.json'
with open('./config.json', 'r') as cf:
    config = load(cf)
    mode = config['mode']
    game_width = config['cell_columns']
    game_height = config['cell_rows']
    grid_width = config['grid_width']
    cell_size = config['cell_size']
    bg_color = tuple(config['background_color'])
    grid_color = tuple(config['grid_color'])
    cell_color = tuple(config['cell_color'])

    
cell_offset = [0, 0]        # Initial offset (camera movement).
width, height = [(cell_size * i + 12) for i in [game_width, game_height]]    # Initial size of the window.


# Auxiliary functions.
def draw_grid(screen, start_x, start_y, width, height, cell_size):
    # Vertical lines:
    for x in range(width + 1):
        begin = (start_x + (cell_size * x), start_y)
        end = (start_x + (cell_size * x), start_y + (height * cell_size))
        pygame.draw.line(screen, grid_color, begin, end, grid_width)
    # Horizontal lines:
    for y in range(height + 1):
        begin = (start_x, start_y + (cell_size * y))
        end = (start_x + (width * cell_size), start_y + (cell_size * y))
        pygame.draw.line(screen, grid_color, begin, end, grid_width)


# Returns the cell number given a cursor postion in pixels.
def get_cell_number(absolute_position, start_xy, cell_size):
    absolute_position = [absolute_position[i] - start_xy[i] for i in [0, 1]]
    return tuple([int(absolute_position[i] / cell_size) for i in [0, 1]])


# Returns the relative position of a cell taking into account the offset.
def get_rel_cell_position(cell_position, moved, start_xy, cell_size):
    rel_position = [cell_position[i] - moved[i] for i in [0, 1]]
    x, y = ((rel_position[i] * cell_size) + start_xy[i] for i in [0, 1])
    return [x, y]


# Draws a set of cells.
def draw_cells(screen, cells, start_xy, cell_size):
    for cell in cells:
        rect = pygame.Rect(get_rel_cell_position(cell, cell_offset, start_xy, cell_size), (cell_size, cell_size))
        pygame.draw.rect(screen, cell_color, rect)

# Transforms a set of cells into a matrix and viceversa.
def transform_cells(cells):
    if type(cells) is list:
        result = set()
        for row in cells:
            for cell in row:
                if cell:
                    result.add(row.index(cell), cell.index(row))
    elif type(cells) is set:
        result = [[0 for i in range(20)] for j in range(20)]
        for cell in cells:
            if cell[0] < 20:
                result[cell[1]][cell[0]] = 1
    return result


# Calls the function get_cells taking into account the mode (matrix or set).
def game_cycle(mode, get_cells, cells):
    if mode == 'set':
        get_cells(cells)
    elif mode == 'matrix':
        get_cells(transform_cells(cells))
        cells = transform_cells(cells)


def main(get_cells):
    # We bring the initial paramenters.
    global mode
    global width, height
    global game_width, game_height, cell_size, cell_offset
    global bg_color

    pygame.init()    # Start PyGame.
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    cells = set()    # The coordinates of the cells are stored here.

    while True:
        play = False # When true, the game will advance every >0.6 secs.
        start_x = int((width - (game_width * cell_size)) / 2)
        start_y = int((height - (game_height * cell_size)) / 2)
        
        # Take care of events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()      # Exit application.
            
            elif event.type == pygame.VIDEORESIZE:
                # Center grid on window.
                width, height = event.__dict__['size']
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            
            elif event.type == pygame.MOUSEBUTTONDOWN and not play:
                # Add active cells if clicked.
                pos = list(event.__dict__['pos'])
                cells.add(get_cell_number(pos, [start_x, start_y], cell_size))
            
            elif event.type == pygame.KEYDOWN:
                add = {'w': (0, 1), 'a': (-1, 0), 's': (0, -1), 'd': (1, 0)}   # Keys that change the offset.
                if event.__dict__['unicode'] in add:
                    # Change the offset.
                    cell_offset = [cell_offset[i] + add[event.__dict__['unicode']][i] for i in [0, 1]]
                elif event.__dict__['unicode'] == 'n' and not play:
                    # One game cycle.
                    game_cycle(mode, get_cells, cells)
                elif event.__dict__['unicode'] == 'p':
                    # Continous game cycles.
                    play = not play 
        
        # If updating continously, update the game.
        if play:
            game_cycle(mode, get_cells, cells)
            sleep(0.585)
        
        # Draw elements on screen.
        screen.fill(bg_color)
        draw_grid(screen, start_x, start_y, game_width, game_height, cell_size)
        draw_cells(screen, cells, (start_x, start_y), cell_size)
        
        #Update the screen and wait before next cycle.
        pygame.display.flip()
        sleep(0.015)
