from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0, 250, 500, 250, screen, color)
draw_line(250, 0, 250, 500, screen, color)
draw_line(0, 0, 500, 500, screen, color)
draw_line(500, 500, 0, 0, screen, color)

count = 0
while (count < 100):
    color = [ random.randrange(255), random.randrange(255), random.randrange(255) ]
    draw_line(random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500), screen, color)
    count += 1

display(screen)
save_extension(screen, 'img.png')
