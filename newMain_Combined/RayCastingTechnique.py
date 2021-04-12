import pygame
from map import *
from gameSettings import *

'''def ray_casting(screen, position, angle):
    half_angle = angle - h_fov #Angle of the first ray of scope
    xc, yc = position #Position of the player/camera //Starting position of all rays
    for ray in range(no_of_rays):
        sinA = math.sin(half_angle)
        cosA = math.cos(half_angle)
        for depth in range(fov_length):
            x0 = xc + depth * cosA
            y0 = yc + depth * sinA
            #pygame.draw.line(screen, gray, position, (x0, y0), 2)
            if (x0 // tile * tile, y0 // tile * tile) in game_map: #If an object/sprite falls inside our Scope or FOV
                depth = depth * math.cos(angle - half_angle) #To remove fish-eye effect, removes distorted edges of rectangles in map
                obj_height = Est_Coeff / depth #Calculating height of the object/sprite that falls in our scope
                brightness = 255 / (1 + depth * depth * 0.00002) #Used to give a contrast/saturation effect, the further our object is, it will become darker
                colour = (brightness, brightness // 2, brightness//2) #Applying the effect here, can be used later give the illusion
                pygame.draw.rect(screen, colour, (ray * scale, h_height - obj_height // 2, scale, obj_height)) #Draw a rectangle for the each object in the scope
                break
        half_angle = half_angle + ray_angle'''

def mapping(x, y):
    return (x // tile) * tile, (y // tile) * tile

def ray_casting(player, textures): #Implementing the Bresenham's line algorithm along with ray tracing here
    walls = []
    Px, Py = player.returnPosition #player model's co-ordinates
    v_texture = 1
    h_texture = 1
    Xm, Ym = mapping(Px, Py) #co-ordinates of the upper left corner of current grid in the map
    half_angle = player.angle - h_fov
    for ray in range(no_of_rays):
        sinA = math.sin(half_angle)
        cosA = math.cos(half_angle)

        #For vertical line on the grid map (mentioned in notes)
        if cosA >= 0: #if it is positive (y-axis // vertical axis)
            x = Xm + tile
            dx = 1 #used to store the next location on the vertical axis
        else: #if it is negative (y-axis // vertical axis)
            x = Xm
            dx = -1 #used to store the next location on the vertical axis
        for i in range (0, map_width, tile):
            depthV = (x - Px) / cosA #depth of ray (length)
            yv = Py + (depthV * sinA) #y-co-ordinate of collision with vertical or y-axis
            v_tile = mapping(x + dx, yv)
            if v_tile in game_map: #checking for walls/object
                v_texture = game_map[v_tile]
                break #break if a wall is encountered
            x = x + (dx * tile)

        #For horizontal line on the grid map (mentioned in notes)
        if sinA >= 0: #if it is positive (x-axis // horizontal axis)
            y = Ym + tile
            dy = 1
        else: #for negative
            y = Ym
            dy = -1
        for i in range (0, map_height, tile):
            depthH = (y - Py) / sinA
            xh = Px + (depthH * cosA)
            h_tile = mapping(xh, y + dy)
            if h_tile in game_map: #checking for wall/object
                h_texture = game_map[h_tile]
                break #break if a wall is encountered
            y = y + (dy * tile)

        #Projection
        if depthV < depthH: #picking the shorter distance
            depth = depthV
        else:
            depth = depthH
        if depthV < depthH: #displacement depending upon the shorter distance (closer axis)
            offset = yv
        else:
            offset = xh
        if depthV < depthH:
            texture = v_texture
        else:
            texture = h_texture
        offset = (int(offset) % tile) #displacement
        depth = depth * math.cos(player.angle - half_angle)  # To remove fish-eye effect, removes distorted edges of rectangles in map
        depth = max(depth, 0.00001)
        obj_height = min(int(Est_Coeff / depth), 5 * height)  # Calculating height of the object/sprite that falls in our scope
        #brightness = 255 / (1 + depth * depth * 0.00001)  # Used to give a contrast/saturation effect, the further our object is, it will become darker
        #colour = (brightness, brightness // 3, brightness // 4)  # Applying the effect here, can be used later give the illusion
        #pygame.draw.rect(screen, colour, (ray * scale, h_height - obj_height // 2, scale, obj_height))  # Draw a rectangle for the each object in the scope
        rect_col = textures[texture].subsurface(offset * t_size, 0, t_size, t_height) #this will create a new surface with same dimensions and it will reference the rectangle on which the texture is mapped
        rect_col = pygame.transform.scale(rect_col, (scale, obj_height)) #scale the size of the wall texture
        #screen.blit(rect_col, (ray * scale, h_height - obj_height // 2)) #add it on the display at appropriate location
        rect_position = (ray * scale, h_height - obj_height // 2)
        walls.append((depth, rect_col, rect_position))
        half_angle = half_angle + ray_angle #move to the next ray
    return walls