import pygame
from gameSettings import *
from playerPOV import player
import math
from map import game_map
from RayCastingTechnique import ray_casting
from sprites import *
from RayCastingTechnique import *
from objects import *

pygame.init() #Initializes all imported pygame modules
pygame.mixer.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((width, height)) #Set up our display screen with the provided resolution
mini_map = pygame.Surface(mini_resolution)
pygame.display.set_caption('SELF HAVOC')
sprites = Sprites()
clock = pygame.time.Clock() #Can be used to manage/aupdate and regulate our FPS
#pygame.display.set_caption(str((clock.get_fps())))
Player = player()
Object = Objects(screen, mini_map)
theme_song = pygame.mixer.music.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\music\theme\SHtheme1.wav')
pygame.mixer.music.play(-1)
fps_base = pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\pov\0.png').convert_alpha()
#fps_base = pygame.transform.scale(fps_base, (h_width, h_height))
base_offset = -10 * math.degrees(Player.angle) % width
base_rect = fps_base.get_rect()
base_position = (h_width - base_rect.width // 2, height - base_rect.height)
#screen.blit(fps_base, base_position)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(fps_base, base_position)
    Player.moveMent() #Movement method
    screen.fill(black) #Fill the display screen with specified colour
    #pygame.draw.rect(screen, sky_blue, (0, 0, width, h_height)) #Sky
    #pygame.draw.rect(screen, gray, (0, h_height, width, h_height)) #Ground
    Object.background(Player.angle) #Game world background method
    #Object.gameWorld(Player.returnPosition, Player.angle)  #Ray casting technique
    walls = ray_casting(Player, Object.textures)
    Object.gameWorld(walls + [sprt.sprite_position(Player, walls) for sprt in sprites.sprite_collection])
    Object.display_fps(clock) #display fps on display
    Object.mini_map(Player)
    '''pygame.draw.circle(screen, red, (int(Player.x), int(Player.y)), 12)
    pygame.draw.line(screen, red, Player.returnPosition, (Player.x + (width * math.cos(Player.angle)), Player.y + (width * math.sin(Player.angle)))) #Applying Ray-Tracing formula to get our camera angle and to generate rays from the camera's POV
    for i, j in game_map: #Draw squares in correspondance with the string_map that we created
        pygame.draw.rect(screen, dark_blue, (i, j, tile, tile), 2)'''
    pygame.display.flip() #Update the contents of the entire display screen
    clock.tick() #Render a frame or set a FPS cap here