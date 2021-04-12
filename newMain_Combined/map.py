from gameSettings import *

#Here, W indicates the Walls and the dots indicates the empty space in the map
'''string_map = [ #OG = 8 total tuples, 12 columns
    '111111111111111111111111',
    '1.222511.........1.....1',
    '1.....61...1.1..1......1',
    '3.....61...1....1..1.1.1',
    '3.222511...111.11..1...1',
    '4.111111.......1...1...1',
    '1............1.........1',
    '114441111111111111111111'
]'''

_ = False
string_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, 1, _, 1, 1, 1, 1, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, 1, _, _, 1, _, _, 1, _, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, 1, _, _, _, 1, 1, 1, 1, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, _, _, _, 1],
    #[1, _, _, _, _, _, _, _, 1, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],
    #[1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1, _, 1, 1, 1, _, _, 1],
    #[1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, _, 1],
    #[1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1],
    [1, 5, 6, 8, 6, 1, _, _, 7, 7, 7, 7, _, 7, 7, 7, 7, _, 1, _, _, _, _, _, 1],
    [14, _, _, _, 9, 1, _, _, 7, _, _, _, _, _, 7, _, 7, _, 1, _, _, _, _, _, 1],
    [13, _, _, _, 10, 1, _, _, _, _, 7, _, 7, _, 7, _, _, _, 1, _, _, _, _, _, 1],
    [12, _, _, _, 1, 1, _, _, 7, _, 7, _, 7, _, 7, _, 7, _, 1, _, _, _, _, _, 1],
    [11, _, _, _, _, _, _, _, 7, _, 7, _, _, _, _, _, 7, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1]
]

map_width = len(string_map[0]) * tile
map_height = len(string_map) * tile

#24 columns #15 rows

'''string_map = [ #OG = 8 total tuples, 12 columns
    '111111111111',
    '1.222511...1',
    '1.....61...1',
    '3.....61...1',
    '3.222511...1',
    '4.111111...1',
    '1..........1',
    '114441111111'
]'''

game_map = {}
mini_map = set()
for i, row in enumerate(string_map):
    for j, char in enumerate(row):
        if char:
            mini_map.add((j * mini_tile_size, i * mini_tile_size))
            if char == 1:
                game_map[(j * tile, i * tile)] = 1
            elif char == 2:
                game_map[(j * tile, i * tile)] = 2
            elif char == 3:
                game_map[(j * tile, i * tile)] = 3
            elif char == 4:
                game_map[(j * tile, i * tile)] = 4
            elif char == 5:
                game_map[(j * tile, i * tile)] = 5
            elif char == 6:
                game_map[(j * tile, i * tile)] = 6
            elif char == 7:
                game_map[(j * tile, i * tile)] = 7
            elif char == 8:
                game_map[(j * tile, i * tile)] = 8
            elif char == 9:
                game_map[(j * tile, i * tile)] = 9
            elif char == 10:
                game_map[(j * tile, i * tile)] = 10
            elif char == 11:
                game_map[(j * tile, i * tile)] = 11
            elif char == 12:
                game_map[(j * tile, i * tile)] = 12
            elif char == 13:
                game_map[(j * tile, i * tile)] = 13
            elif char == 14:
                game_map[(j * tile, i * tile)] = 14