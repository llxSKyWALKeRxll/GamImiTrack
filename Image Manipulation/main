import pygame
import numpy

class mainImageManipulation: #This class will perform the main manipulation operations on the loaded image
    def __init__(self, imiManip, charSize = 4):
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
        self.image = self.load_image('Images/mj1.jpg')


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
                            quit()
                        if keys[pygame.K_w]:
                            print('white colour pressed') #debugging
                            shade = (color, color, color)
                        if keys[pygame.K_c]:
                            print('cyan colour pressed') #nice debugging bro
                            shade = (0, color, color)
                        if keys[pygame.K_p]:
                            print('purple pressed') #nice debugging bro
                            shade = (color, 0, color)
                        if keys[pygame.K_y]:
                            print('yellow colour pressed') #nice debugging bro
                            shade = (color, color, 0)
                        if keys[pygame.K_u]:
                            print('yellow2 colour pressed')
                            shade = (color/2, color, 0)
                        if keys[pygame.K_r]:
                            print('red colour pressed') #nice debugging bro
                            shade = (color, 0, 0)
                        if keys[pygame.K_g]:
                            print('green colour pressed') #nice debugging bro
                            shade = (0, color, 0)
                        if keys[pygame.K_b]:
                            print('blue colour pressed') #nice debugging bro
                            shade = (0, 0, color)
                        if keys[pygame.K_h]:
                            print('light green colour pressed') #nice debugging bro
                            shade = (0, color, color/2)
                        if keys[pygame.K_s]:
                            print('skin colour pressed') #nice debugging bro
                            shade = (color, color/2, 0)
                        if keys[pygame.K_o]:
                            print('purple2 colour')
                            shade = (color/2, 0, color)
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
        self.width = 1300 #og 750, 1300
        self.height = 800 #og 800
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


run = initializeImage()
run.execute()
