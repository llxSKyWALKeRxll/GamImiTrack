import pygame
from gameSettings import *

class Sprites:
    def __init__(self):
        self.sprites_category = {
            'dbz1': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\sonGoku.png').convert_alpha(),
            'dbz2': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\goku3.png').convert_alpha(),
            'dbz3': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\gohan1.png').convert_alpha(),
            'dbz4': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\goku8.png').convert_alpha(),
            'dbz5': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\goku9.png').convert_alpha(),
            'dbz6': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\vegeta1.png').convert_alpha(),
            'dbz7': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\vegeta2.png').convert_alpha(),
            'dbz8': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\trunks1.png').convert_alpha(),
            'dbz9': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\trunks2.png').convert_alpha(),
            'dbz10': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\picollo1.png').convert_alpha(),
            'soldier': [pygame.image.load(rf'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\moving\{i}.png').convert_alpha for i in range(8)],
            'cod1': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\cod1.png').convert_alpha(),
            'catW': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\catWelcome.png').convert_alpha(),
            'catS': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\catSelfie.png').convert_alpha(),
            'cb1': pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Self Havoc\images\sprites\bheem1.png').convert_alpha(),
        }
        self.sprite_collection = [
            SpritesCalc(self.sprites_category['dbz1'], True, (6.5, 10.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz2'], True, (23.5, 7.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz3'], True, (23.5, 9.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz4'], True, (23.5, 11.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz5'], True, (22.5, 7.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz6'], True, (22.5, 9.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz7'], True, (22.5, 11.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz8'], True, (21.5, 7.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz9'], True, (21.5, 9.5), 0, 1),
            SpritesCalc(self.sprites_category['dbz10'], True, (21.5, 11.5), 0, 1),
            SpritesCalc(self.sprites_category['cod1'], True, (20.5, 7.5), 0, 1),
            #SpritesCalc(self.sprites_category['soldier'], False, (22, 4), 0, 0.8),
            SpritesCalc(self.sprites_category['catW'], True, (22.5, 4), 0, 1),
            SpritesCalc(self.sprites_category['catS'], True, (22.5, 3), 0, 1),
            SpritesCalc(self.sprites_category['cb1'], True, (22.5, 5), 0, 1)
        ]


class SpritesCalc:
    def __init__(self, sprite, type, position, change, size): #type = is it static or moving?
        self.sprite = sprite
        self.type = type
        self.position = self.x, self.y = position[0] * tile, position[1] * tile
        self.change = change
        self.size = size
        if not type:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)] # As 360/45 = 8
            self.sprite_positions = {angle: position for angle, position in zip(self.sprite_angles, self.sprite)}

    def sprite_position(self, player, walls): #Using same formulas from the notes
        Dx = self.x - player.x
        Dy = self.y - player.y
        sprite_distance = math.sqrt(Dx ** 2 + Dy ** 2)
        theta_angle = math.atan2(Dy, Dx)
        gamma_angle = theta_angle - player.angle
        if Dx > 0 and 180 <= math.degrees(player.angle) <= 360 or Dx < 0 and Dy < 0:
            gamma_angle = gamma_angle + (math.pi * 2)
        Drays = int(gamma_angle / ray_angle)
        Cray = central_ray + Drays
        sprite_distance = sprite_distance * math.cos(h_fov - Cray * ray_angle) #for fish-eye effect
        if 0 <= Cray <=no_of_rays - 1 and sprite_distance < walls[Cray][0]: # check if sprite is within our scope and if sprite is closer to player model than the wall
            est_height = int(Est_Coeff / sprite_distance * self.size) #sprite height
            h_est_height = est_height // 2 #adjust height of sprite
            change = h_est_height * self.change
            if not self.type:
                if theta_angle < 0:
                    theta_angle = theta_angle + (math.pi * 2)
                theta_angle = 360 - int(math.degrees(theta_angle))
                for angle in self.sprite_angles:
                    if theta_angle in angle:
                        self.sprite = self.sprite_positions[angle]
                        break
            sprite_position = (Cray * scale - h_est_height, h_height - h_est_height + change) #sprite position
            sprite = pygame.transform.scale(self.sprite, (est_height, est_height)) #scale/adjust the sprite
            return (sprite_distance, sprite, sprite_position)
        else:
            return (False,)