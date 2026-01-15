import pygame
import random

#--------------------------
# SECTION 1: PYGAME SETUP
#--------------------------

# Pygame Initialisation Logic
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
clock = pygame.time.Clock()

# the font setup logic
font_size = 20
font = pygame.font.SysFont("MS Gothic", font_size, bold=True)

# the strand characters --> half-width KataKana
matrix_chars = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"

# number of columns based on the font size
columns = width // font_size

#--------------------------
# SECTION 2: STREAM CLASS
#--------------------------

class Stream:
    def __init__(self, x):
        self.x = x
        self.reset()

    def reset(self):
        self.y = random.randint(-height, 0)
        self.speed = random.randint(4, 12)
        self.length = random.randint(5, 20)

    def draw(self):
        for i in range(self.length):
            char = random.choice(matrix_chars)
            color_intensity = max(50, 255 - i * 12)

            # adds a soft green glow to the streams
            glow_color = (0, 80, 0) # dim green
            glow = font.render(char, True, glow_color)
            screen.blit(glow, (self.x - 1, self.y - i * font_size))
            screen.blit(glow, (self.x + 1, self.y - i * font_size))
            screen.blit(glow, (self.x,     self.y - i * font_size + 1))
            screen.blit(glow, (self.x,     self.y - i * font_size - 1))

            if i == 0:
                color = (180, 255, 180) # leading bright glyph
            else:
                color = (0, color_intensity, 0)

            text = font.render(char, True, color)
            screen.blit(text, (self.x, self.y - i * font_size))

        self.y += self.speed

        if self.y - self.length * font_size > height:
            self.reset()

#-------------------------------------
# SECTION 3: CREATE STREAMS FOR EFFECT
#-------------------------------------

streams = [Stream(x * font_size) for x in range(columns)]

#-----------------------------------
# SECTION 4: THE MAIN ANIMATION LOOP
#-----------------------------------

running = True
while running:
    fade_surface = pygame.Surface((width, height))
    fade_surface.set_alpha(70) # lower = longer trails = more cinematic and movie-like
    fade_surface.fill((0, 0, 0))
    screen.blit(fade_surface, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

    for stream in streams:
        stream.draw()

    pygame.display.flip()
    clock.tick(60) # smooth 60 FPS (frames per second)

pygame.quit()


