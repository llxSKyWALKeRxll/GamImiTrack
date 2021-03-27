import pygame
from gameSettings import *
from map import *
from RayCastingTechnique import *
from collections import *

class Objects:
    def __init__(self, screen, mini_map):
        self.screen = screen
        self.mini_map1 = mini_map
        self.font = pygame.font.SysFont('Times New Roman', 30, bold=True)
        self.textures = {
            1: pygame.image.load('images/textures/t3.jpg').convert(),
            2: pygame.image.load('images/textures/cat1.jpg').convert(),
            3: pygame.image.load('images/textures/t2.jpg').convert(),
            4: pygame.image.load('images/textures/t1.jpg').convert(),
            5: pygame.image.load('images/textures/vm1.jpg').convert(),
            6: pygame.image.load('images/textures/vm2.jpg').convert(),
            'S': pygame.image.load('images/textures/s3.jpg').convert()
                         }
        self.textures[1] = pygame.transform.scale(self.textures[1], (width, height))
        self.textures[3] = pygame.transform.scale(self.textures[3], (width, height))
        self.textures[4] = pygame.transform.scale(self.textures[4], (width, height))
        self.textures[2] = pygame.transform.scale(self.textures[2], (width, height)) #use this only for manual images with undefined res. else comment this out lol
        self.textures['S'] = pygame.transform.scale(self.textures['S'], (width, height))
        self.textures[5] = pygame.transform.scale(self.textures[5], (width, height))
        self.textures[6] = pygame.transform.scale(self.textures[6], (width, height))
        #for i in range(9):
        #self.textures['X'] = pygame.transform.scale(self.textures['X'], (width, height))

    def background(self, angle):
        #pygame.draw.rect(self.screen, sky_blue, (0, 0, width, h_height))  # Sky
        s_offset = -5 * math.degrees(angle) % width #displacement
        self.screen.blit(self.textures['S'], (s_offset, 0)) #Black gaps
        self.screen.blit(self.textures['S'], (s_offset - width, 0)) #So that sky is visible at all times
        self.screen.blit(self.textures['S'], (s_offset + width, 0)) #Sky will be visible at all times
        #self.screen.blit(self.textures['X'], (s_offset, 0))  # Black gaps
        #self.screen.blit(self.textures['X'], (s_offset - width, 0))  # So that sky is visible at all times
        #self.screen.blit(self.textures['X'], (s_offset + width, 0))
        '''for i in range (10, 14):
            self.screen.blit(self.textures[i], (s_offset, 0))  # Black gaps
            self.screen.blit(self.textures[i], (s_offset - width, 0))  # So that sky is visible at all times
            self.screen.blit(self.textures[i], (s_offset + width, 0))'''
        pygame.draw.rect(self.screen, gray, (0, h_height, width, h_height))  # Ground

    def gameWorld(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle, self.textures)

    def display_fps(self, tick):
        fps = str(int(tick.get_fps()))
        pos = self.font.render(fps, 0, yellow)
        self.screen.blit(pos, fps_pos)

    def mini_map(self, Player):
        self.mini_map1.fill(black)
        mini_map_x = Player.x // mini_map_size
        mini_map_y = Player.y // mini_map_size
        #pygame.draw.circle(self.mini_map, brown, (int(mini_map_x), int(mini_map_y)), 5)
        pygame.draw.line(self.mini_map1, yellow, (mini_map_x, mini_map_y), (mini_map_x + (12 * math.cos(Player.angle)), mini_map_y + (12 * math.sin(Player.angle))), 2)  # Applying Ray-Tracing formula to get our camera angle and to generate rays from the camera's POV
        pygame.draw.circle(self.mini_map1, brown, (int(mini_map_x), int(mini_map_y)), 5)
        for i, j in mini_map:  # Draw squares in correspondance with the string_map that we created
            pygame.draw.rect(self.mini_map1, yellow, (i, j, mini_tile_size, mini_tile_size))
        self.screen.blit(self.mini_map1, mini_map_position)
