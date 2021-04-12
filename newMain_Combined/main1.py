import pygame
import numpy
import sys
from gameSettings import *
from playerPOV import *
import math
from map import game_map
from RayCastingTechnique import ray_casting
from sprites import *
from RayCastingTechnique import *
from objects import *
from datetime import *


#nice debugging nOObz
class mainImageManipulation: #This class will perform the main manipulation operations on the loaded image
    def __init__(self, imiManip, charSize = 6):
        self.imiManip = imiManip
        self.char_Size = charSize
        self.rows = imiManip.height // charSize #Adjusting the no. of characters that will be displayed row-wise according to the set resolution
        self.columns = imiManip.width // charSize #Adjusting the no. of characters that will be displayed column-wise according to the set resolution
        self.size = self.rows, self.columns #Aggregated size of rows and columns combined
        self.special_char = numpy.array([chr(int('0x0180', 16) + i) for i in range (96)] + [' ' for i in range(15)]) #Load the symbols/characters from the specified unicode block and the given range
        self.font = pygame.font.SysFont('times new roman', charSize, bold=True) #Setting the font-style for characters. It loads the font from the Local Machine/System
        self.manipulation = numpy.random.choice(self.special_char, self.size) #To randomize the selection of characters from the specified unicode
        self.symbol_animation = numpy.random.choice(self.special_char, self.char_Size) #Generates random symbols from the specified unicode so that they look animated on the display screen
        self.move_symbol = numpy.random.randint(25, 50, size=self.char_Size) #Helps in moving the symbols along a vertical line so that they appear animated #OG = 25, 50
        self.symbol_speed = numpy.random.randint(250, 500, size=self.char_Size) #This defines the speed in which the letters randomize themselves #Og = 250, 400
        self.image = self.load_image(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\Images\hagler3.jpg')
        #self.flag = 0


    def execute(self):
        frames = pygame.time.get_ticks()
        self.switch_symbols(frames)
        self.switch_columns(frames)
        self.positioning()

    def switch_columns(self, tick):
        check = tick % self.symbol_speed #Calculate no. of frames required
        final_check = numpy.argwhere(check == 0) #Returns the position of the intervals where check == 0
        final_check = final_check[:, :] #Replaces itself with two copies of itself
        final_check = numpy.unique(final_check) #Returns the unique symbols of the array in a sorted manner (non-repetitive)
        self.manipulation[:, final_check] = numpy.roll(self.manipulation[:, final_check], shift=5, axis=0) #Places random symbols in the vertical line/y-axis

    def switch_symbols(self, tick):
        check = tick % self.move_symbol #Calculate the no. of frames required
        final_check = numpy.argwhere(check == 0) #Returns the indices/position of the intervals where check == 0
        swap_symbol = numpy.random.choice(self.special_char, final_check.shape[0])
        self.manipulation[final_check[:, 0], final_check[:, :]] = swap_symbol #Places the random symbols in the horizontal line/x-axis


    def positioning(self):
        keys = pygame.key.get_pressed()
        #shade = tuple()
        #if flag == 0:
        shade = (0, 0, 0)
        for x, row in enumerate(self.manipulation):
            for y, char in enumerate(row):
                if char:
                    position = y * self.char_Size, x * self.char_Size  # Calculate position of each character w.r.t. set resolution (in terms of rows and columns)
                    _, red, green, blue = pygame.Color(self.image[position]) #Colour the pixels at the positions according to the x-axis and y-axis indices
                    if red and green and blue: #if red/green/blue have a value, else no need to saturate or adjust the brightness of the pixelated array, else it will be left blank (because value goes into underscope)
                        color = (red + blue + green) // 3 #Adjust brightness of image, can change to 4, 5, etc.
                        color = 220 if 160 < color < 220 else color #Set brightness and saturation for particular indices of the pixelated array to give a good visual effect
                        #char = self.font.render(char, False, (color, color, color))  # Render the characters on screen with the provided colour code
                        if keys[pygame.K_ESCAPE]:
                            print('quitting now')
                            mainMenu = GamImiTrack()
                        if keys[pygame.K_w]:
                            print('white colour pressed') #debugging
                            #global shade
                            shade = (color, color, color)
                            #flag = 1
                        if keys[pygame.K_c]:
                            print('cyan colour pressed') #nice debugging bro
                            #global shade
                            shade = (0, color, color)
                            #flag = 1
                        if keys[pygame.K_p]:
                            print('purple pressed') #nice debugging bro
                            #global shade
                            shade = (color, 0, color)
                            #flag = 1
                        if keys[pygame.K_y]:
                            print('yellow colour pressed') #nice debugging bro
                            #global shade
                            shade = (color, color, 0)
                            #flag = 1
                        if keys[pygame.K_u]:
                            print('yellow2 colour pressed')
                            #global shade
                            shade = (color/2, color, 0)
                            #flag = 1
                        if keys[pygame.K_r]:
                            print('red colour pressed') #nice debugging bro
                            #global shade
                            shade = (color, 0, 0)
                            #flag = 1
                        if keys[pygame.K_g]:
                            print('green colour pressed') #nice debugging bro
                            #global shade
                            shade = (0, color, 0)
                            #flag = 1
                        if keys[pygame.K_b]:
                            print('blue colour pressed') #nice debugging bro
                            #global shade
                            shade = (0, 0, color)
                            #flag = 1
                        if keys[pygame.K_h]:
                            print('light green colour pressed') #nice debugging bro
                            #global shade
                            shade = (0, color, color/2)
                            #flag = 1
                        if keys[pygame.K_s]:
                            print('skin colour pressed') #nice debugging bro
                            #global shade
                            shade = (color, color/2, 0)
                            #flag = 1
                        if keys[pygame.K_o]:
                            print('purple2 colour')
                            #global shade
                            shade = (color/2, 0, color)
                            #flag = 1
                        char = self.font.render(char, False, (shade))
                        char.set_alpha(color + 80) #60
                        self.imiManip.display.blit(char, position)  # Place the characters in the particular position in the display screen

    def load_image(self, location):
        image = pygame.image.load(location)
        image = pygame.transform.scale(image, self.imiManip.resolution)
        pixel_image = pygame.pixelarray.PixelArray(image) #Convert/Transform the image into an array of pixels which will be used for manipulation
        return pixel_image


class initializeImage: #This class will initialize, load and call the manipulation operations from the mainImageManipulation Class
    def __init__(self): #This method will mainly act as a setter method
        self.width = 650 #og 750, 1300
        self.height = 550 #og 800
        self.resolution = self.width, self.height
        pygame.init() #initialize modules of pygame
        self.screen = pygame.display.set_mode(self.resolution) #set res on display screen
        self.display = pygame.Surface(self.resolution)
        self.clock = pygame.time.Clock()
        self.imageManipulation = mainImageManipulation(self)

    def load(self): #Setter
        self.display.fill(pygame.Color('black'))
        self.imageManipulation.execute()
        self.screen.blit(self.display, (0, 0))

    def execute(self): #Getter method
        pygame.display.set_caption("Image Manipulation") #Sets the title of the pygame display screen
        #pygame.display.set_caption(str(self.clock.get_fps()))
        self.buttonFont = pygame.font.SysFont('times new roman', 14, bold=True)
        t1 = self.buttonFont.render('White = W', True, (255, 255, 255))
        t2 = self.buttonFont.render('Red = R', True, (255, 0, 0))
        t3 = self.buttonFont.render('Yellow = Y', True, (255, 255, 0))
        t4 = self.buttonFont.render('Blue = B', True, (0, 0, 255))
        t5 = self.buttonFont.render('Purple = P', True, (255, 0, 255))
        t6 = self.buttonFont.render('Green = G', True, (0, 128, 0))
        t7 = self.buttonFont.render('Cyan = C', True, (0, 255, 255))
        t8 = self.buttonFont.render('Skin = S', True, (255, 128, 0))
        #self.screen.blit(t1, (100, 100, 50, 60))
        #self.screen.blit(t2, (10, 30, 30, 30))
        #pygame.display.flip()
        while True:
            self.load()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT] #Exit when the 'X' button is pressed///Returns false so that the loop stops
            #pygame.display.set_caption("Image Manipulation") #Sets the title of the pygame display screen
            #pygame.display.set_caption(str(self.clock.get_fps()))
            self.screen.blit(t1, (10, 10))
            self.screen.blit(t2, (10, 25))
            self.screen.blit(t3, (10, 40))
            self.screen.blit(t4, (10, 55))
            self.screen.blit(t5, (10, 70))
            self.screen.blit(t6, (10, 85))
            self.screen.blit(t7, (10, 100))
            self.screen.blit(t8, (10, 115))
            pygame.display.flip() #Update pygame display screen
            self.clock.tick() #Set the frames per second here (FPS Cap)


def GamImiTrack():
    pygame.init()
    pygame.display.set_caption('GamImiTrack')
    clock = pygame.time.Clock() #Will be used to help regulate the fps in the game/software
    fps = 60 #This will be our FPS cap (LOL)
    resolution = [800, 600] #The Resolution (bruh)
    mmColour = (255, 255, 255) #Main Menu Colour (Shadow Colour)
    fontStyle = pygame.font.Font(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\fonts\f2.ttf', 44)
    mainText = pygame.font.Font(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\fonts\f1.otf', 140)
    screen = pygame.display.set_mode(resolution) #Setup the Main Screen
    bgImg = pygame.image.load(r"C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\bgImg2.jpg") #This is used to load any image (can be used for the background, etc.)

    outline1 = pygame.Rect(30, 190, 320, 70) #Outline for Button-1
    outline2 = pygame.Rect(30, 290, 420, 70) #Outline for Button-2
    outline3 = pygame.Rect(30, 390, 320, 70) #Outline for Button-3
    #outline4 = pygame.Rect(165, 390, 220, 70) #Outline for Button-4
    outline5 = pygame.Rect(30, 490, 220, 70) #Outline for Button-5

    button1 = pygame.Rect(40, 200, 300, 50) #Button-1 for Self Havoc
    button2 = pygame.Rect(40, 300, 400, 50) #Button-2 for Image Manipulation
    button3 = pygame.Rect(40, 400, 300, 50) #Button-3 for Video Manipulation
    #button4 = pygame.Rect(175, 400, 200, 50) #Button-4 for Credit
    button5 = pygame.Rect(40, 500, 200, 50) #Button-5 for Exit

    text1 = fontStyle.render('Self Havoc', True, yellow)
    text2 = fontStyle.render('Image Manipulation', True, yellow)
    text3 = fontStyle.render('DigiClock', True, yellow)
    #text4 = fontStyle.render('CREDITS', True, (0, 255, 0))
    text5 = fontStyle.render('EXIT', True, (yellow))
    text6 = mainText.render('GamImiTrack', True, yellow, red)

    #green = (0, 128, 0)
    #blue = (0, 0, 255)


    screen.fill(mmColour)
    screen.blit(bgImg, (0, 0))
    pygame.draw.rect(screen, yellow, outline1)  # Outline for Button-1
    pygame.draw.rect(screen, yellow, outline2)  # Outline for Button-2
    pygame.draw.rect(screen, yellow, outline3)  # Outline for Button-3
    #pygame.draw.rect(screen, green, outline4)  # Outline for Button-4
    pygame.draw.rect(screen, yellow, outline5)  # Outline for Button-5
    pygame.draw.rect(screen, red, button1)  # Display the Button-1
    pygame.draw.rect(screen, red, button2)  # Display the Button-2
    pygame.draw.rect(screen, red, button3)  # Display the Button-3
    #pygame.draw.rect(screen, blue, button4)  # Display the Button-4
    pygame.draw.rect(screen, red, button5)  # Display the Button-5
    screen.blit(text1, button1)  # Add text1 to Button-1
    screen.blit(text2, button2)  # Add text2 to Button-2
    screen.blit(text3, button3)  # Add text3 to Button-3
    #screen.blit(text4, button4)  # Add text4 to Button-4
    screen.blit(text5, button5)  # Add text5 to Button-5
    screen.blit(text6, (190, 20))


    pygame.display.update()  # To update our Display screen
    clock.tick(fps)  # Limit our FPS to 60 (bruh)

    ctr1 = 0

    while True: #Loop will continue to run till a condition or a check block returns False bool
        #screen.blit(bgImg, (0, 0), ((ctr1 % width), h_height, width, height))
        #ctr1 += 1
        menu_trigger = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                    sys.exit()
                    return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos  #This will get the position of the mouse pointer


                #The following if conditions will check whether the mouse is pointing/hovering our button or not
                #We can perform actions based on them

                '''while menu_trigger:
                    screen.blit(bgImg, (0, 0), (ctr1 % width, h_height, width, height))
                    ctr1 = ctr1 + 1'''

                if button1.collidepoint(mousePos):
                    menu_trigger = False
                    print("Self Havoc is still in its development phase!")
                    pygame.init() #Initializes all imported pygame modules
                    pygame.mixer.init()
                    pygame.mouse.set_visible(False)
                    screen = pygame.display.set_mode((width, height)) #Set up our display screen with the provided resolution
                    mini_map = pygame.Surface(mini_resolution)
                    pygame.display.set_caption('SELF HAVOC')
                    sprites = Sprites()
                    clock = pygame.time.Clock() #Can be used to manage/aupdate and regulate our FPS
                    #pygame.display.set_caption(str((clock.get_fps())))
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        mainMenu1 = GamImiTrack()
                    Player = player()
                    Object = Objects(screen, mini_map)
                    theme_song = pygame.mixer.music.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\music\theme\SHtheme1.wav')
                    pygame.mixer.music.play(-1)
                    fps_base = pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined\images\sprites\pov\0.png').convert_alpha()
                    #fps_base = pygame.transform.scale(fps_base, (h_width, h_height))
                    base_offset = -10 * math.degrees(Player.angle) % width
                    base_rect = fps_base.get_rect()
                    base_position = (h_width - base_rect.width // 2, height - base_rect.height)
                    #screen.blit(fps_base, base_position)

                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    pygame.mouse.set_visible(True)
                                    pygame.mixer.music.stop()
                                    print('Escape pressed')
                                    mainMenu3 = GamImiTrack()
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
                    #pygame.display.flip()
                    #clock.tick()
                    #pass
                    #Add the Self Havoc main script here

                if button2.collidepoint(mousePos):
                    menu_trigger = False
                    print("Image Manipulation is still in its development phase!")
                    run = initializeImage()
                    run.execute()
                    #pass
                    #Add the Image Manipulation script here

                if button3.collidepoint(mousePos):
                    menu_trigger = False
                    #print("Video Manipulation is still in its development phase!")
                    width1 = 1200
                    height1 = 600
                    resolution = width1, height1
                    pygame.init()
                    pygame.display.set_caption('DigiClock')
                    screen = pygame.display.set_mode(resolution)
                    clock = pygame.time.Clock()
                    font = pygame.font.SysFont('Times New Roman', 200)
                    '''for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                print('Escape pressed')
                                mainMenu2 = GamImiTrack()'''

                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    print('Escape pressed')
                                    mainMenu2 = GamImiTrack()
                        [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
                        screen.fill(pygame.Color('black'))
                        time = datetime.now()
                        rendered_time = font.render(f'{time:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('yellow'))
                        screen.blit(rendered_time, (230, 150))
                        pygame.display.flip()
                        clock.tick(60)
                    pass
                    #Add the Video Manipulation script here

                '''if button4.collidepoint(mousePos):
                    #Add credits here
                    pass'''

                if button5.collidepoint(mousePos):
                    menu_trigger = False
                    quit()
                    sys.exit()
                    return False

    pygame.display.flip()  # To update our Display screen
    clock.tick(fps)  # Limit our FPS to 60 (bruh)


mainMenu = GamImiTrack()