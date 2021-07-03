import pygame
from collections import deque
import dissolving_octagons_text_and_shapes as graphics
"""
DISSOLVING OCTAGONS WITH PYGAME

EXPLANATION:
A grid of octagons (pygame's draw.polygon function) which detects the
X/Y axis of the user's mouse and fills in the octagon with solid color.
Movement creates a historical list of coordinates ('fader') which are stored 
in a deque with a user determined max-value. The iterated index of each coordinate 
is used as the color value (left to right) starting from 0 (black) to number of 
elements in the deque 'fader':

A for loop is used to iterate through the indices of fader:
for idx in range(len(fader)):

Each subsequent index's color value is determined with:
col_value = idx * int(background_value // maxlength)
pseudo: The color value = current index * (background value // the length of fader)

Because the current location will always be 0 index, it will be black and every
following index will fade to the background color. 

Because of the nature of deque with a max limit set, 
the filled octagons will be over written by the initial octagon graph.

In the case of no mouse movement, the current location will default to it's red cursor.

The user can set the amount of octagons horizontally, the length of the tail, 
turning on/off tracer, and turning on/off the graph.

Using Python's module Collections Deque:
https://docs.python.org/3/library/collections.html

Download "earthorbitertitle.ttf" font from: https://ufonts.com/fonts/earth-orbiter-title.html
Copyright: 2016 Iconian Fonts - www.iconian.com

**NOTE** You will need pygame library installed for this:
pygame installation: https://www.pygame.org/wiki/GettingStarted

Thanks for your interest!

Twitter: https://twitter.com/Bennyboy_JP
Github: https://github.com/thejourneyville

bennyBoy_JP 2021
"""
# --------------------
# USER PARAMETERS:
# number of octagons on x-axis (y-axis is determined by x-axis // 2)
poly_count_x = 25

# length of fading trail
maxlength = 25

# tracer follows the path
tracer_on = False

# graph on/off
graph = True
# --------------------

# initializing pygame
pygame.init()
display_info_object = pygame.display.Info()
margin = 100  # space from the edge of surface ('screen')
screen_width, screen_height = display_info_object.current_w - margin, display_info_object.current_h - (margin * 2)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dissolving octagons")
clock = pygame.time.Clock()
fps = 60

# graph height is hardcoded 1/2 of width
poly_count_y = poly_count_x // 2

# we create our deque called 'fader' which will hold maxlength number of coordinates
fader = deque([], maxlen=maxlength)

# polygon square size is determined by height of 'screen' * .75 to accommodate margin
poly_size_y = int((screen_height // poly_count_y) * .75)
poly_size_x = poly_size_y

# margin is created as starting x/y points for graph
margin_x = (screen_width - (poly_size_x * poly_count_x)) // 2
margin_y = (screen_height - (poly_size_y * poly_count_y)) // 2

# used to remove cursor rendering when cursor goes outside of the margins
margin_border = (margin_x, margin_y, (poly_size_x * poly_count_x) + margin_x, (poly_size_y * poly_count_y) + margin_y)

# octagon maths
corner_to_center = ((poly_size_x ** 2 + poly_size_x ** 2) ** (1 / 2)) / 2
side_length = poly_size_x - ((poly_size_x - corner_to_center) * 2)
diag_dist = ((side_length * 2 ** (1 / 2)) / 2)

background_value = 200
background_color = [background_value for _ in range(3)]

# maxlength cannot exceed background value otherwise the fade effect will lose its magic
if maxlength > background_value:
    maxlength = background_value
    print(f"maxlength must be <= to background value color\n"
          f"maxlength set equal to background color")


def start():

    while True:

        screen.fill(background_color)
        clock.tick(fps)

        # able to quit by closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # grab current mouse coordinates
        mx, my = pygame.mouse.get_pos()
        current_cell_x, current_cell_y = f"x:{mx}", f"y:{my}"

        # render text coordinates
        graphics.render_text(
            screen, current_cell_x, current_cell_y, margin_x, screen_height)

        # begin for loop iteration to draw graph
        for r in range(0, poly_size_y * poly_count_y, poly_size_y):
            for c in range(0, poly_size_x * poly_count_x, poly_size_x):

                # margins are added to coordinates
                row = r + margin_y
                col = c + margin_x

                # square and octagons are plotted as a list of points
                square = graphics.square(col, row, poly_size_x, poly_size_y)
                octagon = graphics.octagon(col, diag_dist, row, side_length)

                # if the cursor coordinates is on a specific square...
                if col <= mx < (col + poly_size_x):
                    if row <= my < (row + poly_size_y):

                        # add coordinates to the fader queue from index 0
                        fader.appendleft((col, row))

                        # outline current octagon
                        pygame.draw.polygon(screen, (255, 69, 0), octagon, 3)

                if graph:  # option to enable graph architecture
                    pygame.draw.polygon(screen, (220, 220, 220), square, 1)
                    pygame.draw.polygon(screen, (100, 100, 100), octagon, 1)

        # the following actions only take place if the cursor is within the margins
        if margin_border[2] >= mx >= margin_border[0]:
            if margin_border[3] >= my >= margin_border[1]:

                # if more than 1 coordinate currently is in 'fader' deque
                if len(set(fader)) > 1:
                    # iterates from in reverse so newest octagons render OVER older ones
                    for idx in range(len(fader) - 1, 0, -1):

                        # grab coordinate history
                        col_p = fader[idx][0]
                        row_p = fader[idx][-1]

                        # create octagon coordinates based on idx history of 'fader'
                        octagon_p = graphics.octagon(col_p, diag_dist, row_p, side_length)

                        # idx also determines the value of the color of the octagon
                        col_value = [idx * background_value // maxlength for _ in range(3)]

                        pygame.draw.polygon(screen, col_value, octagon_p)

                        # tracer feature, follows the path of the coordinates delayed by the
                        #  iterations through maxlength
                        if tracer_on:
                            if idx == len(fader) - 1:
                                pygame.draw.polygon(screen, (255, 69, 0), octagon_p)
            else:  # if not in margins, clear 'fader' deque
                fader.clear()
        else:  # if not in margins, clear 'fader' deque
            fader.clear()

        pygame.display.update()


if __name__ == "__main__":
    start()
