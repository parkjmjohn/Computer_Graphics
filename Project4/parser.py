from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires nextuments must have those nextuments in the second line.
     The commands are as follows:
        line: add a line to the edge matrix - 
	    takes 6 nextuemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 nextuments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 nextuments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 nextuments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 nextument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
	with open(fname) as f:
		lines=f.readlines()
		lines=[x.strip() for x in lines]
	i=0;
	while(i<len(lines)):
		command=lines[i]
		next=lines[i+1]
		if(command=="line"):
			points=next.split(" ")
			add_edge(points,int(points[0]),int(points[1]),int(points[2]),int(points[3]),int(points[4]),int(points[5]))
			i+=2
		if(command=="ident"):
			ident(transform)
			i+=1
		if(command=="scale"):
			points=next.split(" ")
			ret=make_scale(int(points[0]),int(points[1]),int(points[2]))
			matrix_mult(ret,transform)
			i+=2
		if(command=="move"):
			points=next.split(" ")
			ret=make_translate(int(points[0]),int(points[1]),int(points[2]))
			matrix_mult(ret,transform)
			i+=2
		if(command=="rotate"):
			points=next.split(" ")
			if(points[0]=="z"):
				ret=make_rotZ(int(points[1]))
			if(points[0]=="y"):
				ret=make_rotY(int(points[1]))
			if(points[0]=="x"):
				ret=make_rotX(int(points[1]))
			matrix_mult(ret,transform)
			i+=2
		if(command=="apply"):
			matrix_mult(transform,points)
			i+=1
		if(command=="display"):
			draw_lines(points,screen,color)
			display(screen)
			sleep(.5)
			clear_screen(screen)
			i+=1
		if(command=="save"):
			save_extension(screen,next)
			clear_screen(screen)
			i+=2
		print_matrix(points)
	f.close()
