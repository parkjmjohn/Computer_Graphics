import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return
    
    ident(tmp)
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    tmp = []
    step = 0.1
    for command in commands:
        if command[0] == 'sphere':
            add_sphere(tmp, float(command[1]), float(command[2]), float(command[3]), float(command[4]), step)
            matrix_mult(stack[-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp=[]

        elif command[0] == 'torus':
            add_torus(tmp, float(command[1]), float(command[2]), float(command[3]), float(command[4]), float(command[5]), step)
            matrix_mult(stack[-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp = []

        elif command[0] == 'box':
            add_box(tmp, float(command[1]), float(command[2]), float(command[3]), float(command[4]), float(command[5]), float(command[6]))
            matrix_mult(stack[-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp=[]

        elif command[0] == 'circle':
            add_circle(tmp, float(command[1]), float(command[2]), float(command[3]), float(command[4]), step)

        elif command[0] == 'hermite' or command[0] == 'bezier':
            add_curve(tmp, float(command[1]), float(command[2]), float(command[3]), float(command[4]), float(command[5]), float(command[6]), float(command[7]), float(command[8]), step, command[0])

        elif command[0] == 'line':
            add_edge( tmp, float(command[1]), float(command[2]), float(command[3]), float(command[4]), float(command[5]), float(command[6]) )

        elif command[0] == 'scale':
            i = make_scale(float(command[1]), float(command[2]), float(command[3]))
            matrix_mult(stack[-1], i)
            stack[-1] = [ x[:] for x in i ]

        elif command[0] == 'move':
            i = make_translate(float(command[1]), float(command[2]), float(command[3]))
            matrix_mult(stack[-1], i)
            stack[-1] = [ x[:] for x in i ]


        elif command[0] == 'rotate':
            theta = float(command[2]) * (math.pi / 180)
            if command[1] == 'x':
                i = make_rotX(theta)
            elif command[1] == 'y':
                i = make_rotY(theta)
            else:
                i = make_rotZ(theta)
            matrix_mult(stack[-1], i)
            stack[-1] = [ x[:] for x in i ]

        elif command[0] == 'clear':
            tmp=[]

        elif command[0] == 'ident':
            ident(transform)

        elif command[0] == 'apply':
            matrix_mult(transform, tmp)

        elif command[0] == 'push':
            stack.append([x[:] for x in stack[-1]])

        elif command[0] == 'pop':
            stack.pop()

        elif command[0] == 'display' or command[0] == 'save':
            if command[0] == 'display':
                display(screen)
            else:
                save_extension(screen, command[1])
