from gameSettings import *
import pygame
import math

class player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    @property #Getter method as returnPosition()
    def returnPosition(self): #Getter method
        return (self.x, self.y)

    def playerMovement(self):
        sin_pov = math.sin(self.angle)
        cos_pov = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x = self.x + (player_speed * cos_pov) #+
            self.y = self.y + (player_speed * sin_pov)#Move backwards along the y-axis if 'y' is pressed to give a forward movement illusion
            print('W')
        if keys[pygame.K_s]:
            self.x = self.x + (-player_speed * cos_pov) #+
            self.y = self.y + (-player_speed * sin_pov) ##Move forward along the y-axis if 's' is pressed to give a backward movement illusion
            print('S')
        if keys[pygame.K_d]:
            self.x = self.x + (-player_speed * sin_pov) #+
            self.y = self.y + (player_speed * cos_pov) #Move forward along the x-axis if 'd' is pressed to give a sideways movement illusion
            print('D')
        if keys[pygame.K_a]:
            self.x = self.x + (player_speed * sin_pov) #+
            self.y = self.y + (-player_speed * cos_pov) #Move backwards along the x-axis if 'a' is pressed to give a sideways movement illusion
            print('A')
        if keys[pygame.K_LEFT]:
            self.angle = self.angle - 0.01 #Move camera angle backward on the x-axis
        if keys[pygame.K_RIGHT]:
            self.angle = self.angle + 0.01 #Move camera angle forward on the x-axis
