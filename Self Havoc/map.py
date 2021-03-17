from gameSettings import *

#Here, W indicates the Walls and the dots indicates the empty space in the map
string_map = [ #OG = 8 total tuples, 12 columns
    'WWWWWWWWWWWW',
    'W..........W',
    'W..........W',
    'W.W.....W..W',
    'W..W...W...W',
    'W...W.W....W',
    'W....W.....W',
    'WWWWWWWWWWWW'
]

game_map = set()
mini_map = set()
for i, row in enumerate(string_map):
    for j, char in enumerate(row):
        if char == 'W':
            game_map.add((j * tile, i * tile))
            mini_map.add((j * mini_tile_size, i * mini_tile_size))
