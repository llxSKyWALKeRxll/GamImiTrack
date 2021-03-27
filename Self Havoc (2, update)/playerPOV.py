from gameSettings import *
import pygame
import math

class player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle
        self.sensitivity = 0.002
        self.walkSound = pygame.mixer.music.load('music/walk/walking.mp3')
        pygame.mixer.music.play(-1)
        self.playSound = False

    @property #Getter method as returnPosition()
    def returnPosition(self): #Getter method
        return (self.x, self.y)

    def moveMent(self):
        self.playerMovement()
        self.mouseMapping()
        self.angle = self.angle % (math.pi * 2)

    def playerMovement(self):
        sin_pov = math.sin(self.angle)
        cos_pov = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("Should I add a dash or a jump button?")
            pass
            #A dash or a jump button perhaps?
        if keys[pygame.K_w]:
            self.playSound = True
            self.x = self.x + (player_speed * cos_pov) #+
            self.y = self.y + (player_speed * sin_pov)#Move backwards along the y-axis if 'y' is pressed to give a forward movement illusion
            print('W')
        if keys[pygame.K_s]:
            self.playSound = True
            self.x = self.x + (-player_speed * cos_pov) #+
            self.y = self.y + (-player_speed * sin_pov) ##Move forward along the y-axis if 's' is pressed to give a backward movement illusion
            print('S')
        if keys[pygame.K_d]:
            self.playSound = True
            self.x = self.x + (-player_speed * sin_pov) #+
            self.y = self.y + (player_speed * cos_pov) #Move forward along the x-axis if 'd' is pressed to give a sideways movement illusion
            print('D')
        if keys[pygame.K_a]:
            self.playSound = True
            self.x = self.x + (player_speed * sin_pov) #+
            self.y = self.y + (-player_speed * cos_pov) #Move backwards along the x-axis if 'a' is pressed to give a sideways movement illusion
            print('A')
        if self.playSound == True:
            pygame.mixer.music.play(-1)
        if keys[pygame.K_LEFT]:
            print('turning left')
            self.angle = self.angle - 0.02 #Move camera angle backward on the x-axis
        if keys[pygame.K_RIGHT]:
            print('turning right')
            self.angle = self.angle + 0.02 #Move camera angle forward on the x-axis
        if keys[pygame.K_ESCAPE]:
            #Should I further add another main menu for Self Havoc?
            #Think brudda
            print('quittin fam')
            quit()

    def mouseMapping(self):
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - h_width
            pygame.mouse.set_pos((h_width, h_height))
            self.angle = self.angle + (diff * self.sensitivity)
