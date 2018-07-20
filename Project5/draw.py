from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    x0 = r+cx
    y0 = cy
    t = step
    while t <= 1.0001: 
        x1 = r*math.cos(2*math.pi*t)+cx
        y1 = r*math.sin(2*math.pi*t)+cy
        add_edge(points,x0,y0,cz,x1,y1,cz)
        x0 = x1
        y0 = y1
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    x = generate_curve_coefs(x0,x1,x2,x3,curve_type)[0]
    y = generate_curve_coefs(y0,y1,y2,y3,curve_type)[0]
    t = step
    x_0 = x0
    y_0 = y0
    while t<1.001:
        x_1 = x[0]*pow(t,3)+x[1]*pow(t,2)+x[2]*t+x[3]
        y_1 = y[0]*pow(t,3)+y[1]*pow(t,2)+y[2]*t+y[3]
        add_edge(points,x_0,y_0,0,x_1,y_1,0)
        x_0 = x_1
        y_0 = y_1
        t += step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #1 octant 1 while
            plot(screen, color, x1, y1)
        #1 octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #1 octant 8 while
            plot(screen, color, x1, y1)
        #1 octant 8
    #1 octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #1 octant 2 while
            plot(screen, color, x1, y1)
        #1 octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #1 octant 7 while
            plot(screen, color, x1, y1)
        #1 octant 7
    #1 octants 2 and 7
#1 draw_line
