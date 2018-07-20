from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = []
add_edge(matrix, 250, 35, 25, 235, 250, 235)
add_edge(matrix, 125, 250, 190, 250, 350, 100)
draw_lines(matrix, screen, color)

matrix = scalar_mult(matrix, 1.2/10)
draw_lines(matrix, screen, color)

matrix_mult(ident(matrix), matrix)
scale = scalar_mult(ident(matrix), 5.5)
matrix = matrix_mult(scale, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

display(screen)
