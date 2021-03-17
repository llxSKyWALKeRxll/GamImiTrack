import pygame
from gameSettings import *
from map import *
from RayCastingTechnique import *

class Objects:
    def __init__(self, screen, mini_map):
        self.screen = screen
        self.mini_map1 = mini_map
        self.font = pygame.font.SysFont('Times New Roman', 30, bold=True)

    def background(self):
        pygame.draw.rect(self.screen, sky_blue, (0, 0, width, h_height))  # Sky
        pygame.draw.rect(self.screen, gray, (0, h_height, width, h_height))  # Ground

    def gameWorld(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle)

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
            pygame.draw.rect(self.mini_map1, blue_green, (i, j, mini_tile_size, mini_tile_size))
        self.screen.blit(self.mini_map1, mini_map_position)
