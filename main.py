import pygame
import numpy

class mainImageManipulation: #This class will perform the main manipulation operations on the loaded image
    def __init__(self, imiManip, charSize = 2):
        self.imiManip = imiManip
        self.char_Size = charSize
        self.rows = imiManip.height // charSize #Adjusting the no. of characters that will be displayed row-wise according to the set resolution
        self.columns = imiManip.width // charSize #Adjusting the no. of characters that will be displayed column-wise according to the set resolution
        self.size = self.rows, self.columns #Aggregated size
        self.special_char = numpy.array([chr(int('0x0180', 16) + i) for i in range (96)] + [' ' for i in range(15)]) #Load the symbols/characters from the specified unicode block and the given range
        self.font = pygame.font.SysFont('times new roman', charSize, bold=True) #Setting the font-style for characters. It loads the font from the Local Machine/System
        self.manipulation = numpy.random.choice(self.special_char, self.size) #To randomize the selection of characters from the specified unicode
        self.symbol_animation = numpy.random.choice(self.special_char, self.char_Size) #Generates random symbols from the specified unicode so that they look animated on the display screen
        self.move_symbol = numpy.random.randint(25, 50, size=self.char_Size) #Helps in moving the symbols along a vertical line so that they appear animated
        self.symbol_speed = numpy.random.randint(250, 400, size=self.char_Size) #This defines the speed in which the letters randomize themselves
        self.image = self.load_image('Images/kobe3.jpg')


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
        for x, row in enumerate(self.manipulation):
            for y, char in enumerate(row):
                if char:
                    position = y * self.char_Size, x * self.char_Size  # Calculate position of each character w.r.t. set resolution (in terms of rows and columns)
                    _, red, green, blue = pygame.Color(self.image[position]) #Colour the pixels at the positions according to the x-axis and y-axis indices
                    if red and green and blue: #if red/green/blue have a value, else no need to saturate or adjust the brightness of the pixelated array, else it will be left blank (because value goes into underscope)
                        color = (red + blue + green) // 3 #Adjust brightness of image, can change to 4, 5, etc.
                        color = 220 if 160 < color < 220 else color #Set brightness and saturation for particular indices of the pixelated array to give a good effect
                        char = self.font.render(char, False, (color, color, color))  # Render the characters on screen with the provided colour code
                        char.set_alpha(color + 60)
                        self.imiManip.display.blit(char, position)  # Place the characters randomly on the display screen

    def load_image(self, location):
        image = pygame.image.load(location)
        image = pygame.transform.scale(image, self.imiManip.resolution)
        pixel_image = pygame.pixelarray.PixelArray(image) #Convert/Transform the image into an array of pixels which will be used for manipulation
        return pixel_image


class initializeImage: #This class will initialize, load and call the manipulation operations from the mainImageManipulation Class
    def __init__(self): #This method will mainly act as a setter method
        self.width = 750
        self.height = 800
        self.resolution = self.width, self.height
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.display = pygame.Surface(self.resolution)
        self.clock = pygame.time.Clock()
        self.imageManipulation = mainImageManipulation(self)

    def load(self): #Setter
        self.display.fill(pygame.Color('black'))
        self.imageManipulation.execute()
        self.screen.blit(self.display, (0, 0))

    def execute(self): #Getter method
        while True:
            self.load()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT] #Exit when the 'X' button is pressed///Returns false so that the loop stops
            pygame.display.set_caption("Image Manipulation") #Sets the title of the pygame display screen
            #pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip() #Update pygame display screen
            self.clock.tick() #Set the frames per second here (FPS Cap)


run = initializeImage()
run.execute()
