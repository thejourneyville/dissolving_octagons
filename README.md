<h1>DISSOLVING OCTAGONS WITH PYGAME</h1>

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
