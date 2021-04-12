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
            1: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\t2.jpg').convert_alpha(),
            2: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\cat1.jpg').convert_alpha(),
            3: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\t2.jpg').convert_alpha(),
            4: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\t3.jpg').convert_alpha(),
            5: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm1.jpg').convert_alpha(),
            6: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm2.jpg').convert_alpha(),
            7: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\ill1.png').convert_alpha(),
            8: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm3.jpg').convert_alpha(),
            9: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm4.jpg').convert_alpha(),
            10: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm5.jpg').convert_alpha(),
            11: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm6.jpg').convert_alpha(),
            12: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm7.jpg').convert_alpha(),
            13: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm8.jpg').convert_alpha(),
            14: pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\vm9.jpg').convert_alpha(),
            'S': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\textures\s2.png').convert_alpha(),
                         }
        self.textures[1] = pygame.transform.scale(self.textures[1], (width, height))
        self.textures[3] = pygame.transform.scale(self.textures[3], (width, height))
        self.textures[4] = pygame.transform.scale(self.textures[4], (width, height))
        self.textures[2] = pygame.transform.scale(self.textures[2], (width, height)) #use this only for manual images with undefined res. else comment this out lol
        self.textures['S'] = pygame.transform.scale(self.textures['S'], (width, height))
        self.textures[5] = pygame.transform.scale(self.textures[5], (width, height))
        self.textures[6] = pygame.transform.scale(self.textures[6], (width, height))
        self.textures[7] = pygame.transform.scale(self.textures[7], (width, height))
        self.textures[8] = pygame.transform.scale(self.textures[8], (width, height))
        self.textures[9] = pygame.transform.scale(self.textures[9], (width, height))
        self.textures[10] = pygame.transform.scale(self.textures[10], (width, height))
        self.textures[11] = pygame.transform.scale(self.textures[11], (width, height))
        self.textures[12] = pygame.transform.scale(self.textures[12], (width, height))
        self.textures[13] = pygame.transform.scale(self.textures[13], (width, height))
        self.textures[14] = pygame.transform.scale(self.textures[14], (width, height))
        #for i in range(9):
        #self.textures['X'] = pygame.transform.scale(self.textures['X'], (width, height))

    def background(self, angle):
        #pygame.draw.rect(self.screen, sky_blue, (0, 0, width, h_height))  # Sky
        s_offset = -15 * math.degrees(angle) % width #displacement
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

    def gameWorld(self, game_sprites): #player_position, player_angle):
        #ray_casting(self.screen, player_position, player_angle, self.textures)
        for sprt in sorted(game_sprites, key=lambda n: n[0], reverse=True):
            if sprt[0]:
                _, sprite, sprite_position = sprt
                self.screen.blit(sprite, sprite_position)

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