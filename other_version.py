from random import randint, choice
import shutil
import time
import sys

# disabling line rendering to reach maximum smoothness and fast-terminal-rendering
sys.stdout.reconfigure(line_buffering=False)

#----------------------------------------
# SECTION 1: TERMINAL AND CHARACTER SETUP
#----------------------------------------

# # getting the terminal size
columns, rows = shutil.get_terminal_size()

# using the character pool to generate random characters
CHAR_POOL = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"

#------------------------------------------
# SECTION 2: STREAM CLASS (CLEAN STRUCTURE)
#------------------------------------------

class Stream:
    def __init__(self, col, layer):
        self.col = col
        self.layer = layer

        if layer == 0: # foreground layer
            self.speed = randint(1, 2)
            self.max_len = randint(7, 15)
            self.brightness = 1.0
        elif layer == 1: # middleground layer
            self.speed = randint(2, 4)
            self.max_len = randint(7, 12)
            self.brightness = 0.6
        else: # background layer
            self.speed = randint(4, 7)
            self.max_len = randint(4, 10)
            self.brightness = 0.3

        self.pos = randint(0, rows-1)
        self.tail = []
        self.counter = 0

    def update(self):
        # add new character
        if randint(0, 2) == 0: # 33% chance
            self.tail.insert(0, choice(CHAR_POOL))

        # crimp off tail
        if len(self.tail) > self.max_len:
            self.tail.pop()

        # move the stream based on the speed
        self.counter += 1
        if self.counter >= self.speed:
            self.pos = (self.pos + 1) % rows
            self.counter = 0

        # create a glitch effect (random reset)
        if randint(0, 200) == 0:
            self.pos = randint(0, rows-1)
            self.tail.clear()

    def draw(self, screen):
        for i,char in enumerate(self.tail):
            y = (self.pos - i) % rows

            # the leading bright glyph (the worm's head)
            if i == 0:
                color = f"\033[38;2;180;255;180m"
            else:
                fade = ((self.max_len - i) / self.max_len) ** 1.7
                fade *= self.brightness
                green = int(255 * fade)
                color = f"\033[38;2;0;{green};0m"

            screen[y][self.col] = f"{color}{char}\033[0m"

#---------------------------------------------
# SECTION 3: CREATE LAYERED STREAMS FOR EFFECT
#---------------------------------------------

streams = []

# the background layer
for col in range(0, columns, 2): # every 2 columns INSTEAD of every columns
    streams.append(Stream(col, layer=2))

# the middle-ground layer
for col in range(0, columns, 3):
        streams.append(Stream(col, layer=1))

# the background layer
for col in range(0, columns, 4):
        streams.append(Stream(col, layer=0))

#---------------------------------------------
# SECTION 4: THE ANIMATION LOOP
#---------------------------------------------

# hide the cursor
print("\033[?25l", end="")

try:
    while True:
        # empty the screen buffer
        screen_buffer = [[" " for _ in range(columns)] for _ in range(rows)]

        # update and draw each of the streams
        for s in streams:
            s.update()
            s.draw(screen_buffer)

        # move the cursor to top-left
        print("\033[H", end="")

        # render the frame
        for line in screen_buffer:
            print("".join(line))

        # smooth frame rate
        time.sleep(0.025)
except KeyboardInterrupt:
    print("\033[0m\033[?25h") # keyboard interrupt
    print("\nMATRIX RAIN ABORTED") # exit message
