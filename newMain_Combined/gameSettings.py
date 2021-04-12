#This file will contain the main settings for our game
import math

#RESOLUTION SETTINGS
width = 1500 #1200
height = 750 #800
h_width = width // 2
h_height = height // 2
fps = 120
tile = 120 #OG = 100 #Tile size
fps_pos = (width - width + 10, 10)

#POV SETTINGS // FPS CAMERA
player_position = (h_width * 2, h_height * 2)
player_angle = 0
player_speed = 3

#COLOUR CODES
white = (255, 255, 255)
yellow = (255, 255, 0)
light_gray = (192, 192, 192)
sky_blue = (0, 255, 255)
yellow_green = (0, 255, 0)
gray = (128, 128, 128)
dark_yellow = (128, 128, 0)
dark_pink = (255, 0, 255)
blue_green = (0, 128, 128)
red = (255, 0, 0)
green = (0, 128, 0)
purple = (128, 0, 128)
brown = (128, 0, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 128)
black = (0, 0, 0)

#SETTINGS FOR RAY CASTING ALGORITHM
#refer to the notes
fov = math.pi / 3 # /3
h_fov = fov / 2 # /2
no_of_rays = 300 #300
fov_length = 800 #Same as our res. height
ray_angle = fov / no_of_rays #A single ray from the whole scope
D = no_of_rays / (2 * math.tan(h_fov))
Est_Coeff = 3 * D * tile #Can adjust to make our projection better
scale = width // no_of_rays

#Minimap config
mini_scale = 5 #5
mini_resolution = (width // mini_scale, height // mini_scale)
mini_map_size = 2 * mini_scale # 1 for 12x8, 2 for 24x16, 3 for 36x24
mini_tile_size = tile // mini_map_size
mini_map_position = (width - width + 10, height - height // mini_scale) #0, height - height // mini_scale

#Texture settings
t_width = 1500
t_height = 750
t_size = t_width // tile

#Sprite settings
central_ray = no_of_rays // 2 - 1