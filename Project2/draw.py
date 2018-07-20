from display import *

def draw_line(x0, y0, x1, y1, screen, color):
	dx=x1-x0
	dy=y1-y0
	if dx>0:
		if dy>0:
			if dy<dx:
	#Octant 1
				A=y1-y0
				B=-1*(x1-x0)
				A=2*A
				d=A+B
				B=2*B
				x=x0
				y=y0
				while x<=x1:
					plot(screen, color, x, y)
					if d>0:
						y+=1
						d+=B
					x+=1
					d+=A
			else:
	#Octant 2
				A=y1-y0
				B=-1*(x1-x0)
				B=2*B
				d=A+B
				A=2*A
				x=x0
				y=y0
				while y<=y1:
					plot(screen, color, x, y)
					if d<0:
						x+=1
						d+=A
					y+=1
					d+=B
		else:
			if dy*-1<dx:
	#Octant 8
				A=y1-y0
				B=-1*(x1-x0)
				A=2*A
				d=A-B
				B=2*B
				x=x0
				y=y0
				while x<=x1:
					plot(screen, color, x, y)
					if d<0:
						y-=1
						d-=B
					x+=1
					d+=A
			else:
	#Octant 7
				A=y1-y0
				B=-1*(x1-x0)
				B=2*B
				d=A-B
				A=2*A
				x=x0
				y=y0
				while y>=y1:
					plot(screen, color, x, y)
					if d>0:
						x+=1
						d+=A
					y-=1
					d-=B
	else:
		if dy>0:
			if dy>dx*-1:
	#Octant 3
				A=y1-y0
				B=-1*(x1-x0)
				B=2*B
				d=B-A
				A=2*A
				x=x0
				y=y0
				while y<=y1:
					plot(screen, color, x, y)
					if d>0:
						x-=1
						d-=A
					y+=1
					d+=B
			else:
	#Octant 4
				A=y1-y0
				B=-1*(x1-x0)
				A=2*A
				d=B-A
				B=2*B
				x=x0
				y=y0
				while x>=x1:
					plot(screen, color, x, y)
					if d<0:
						y+=1
						d+=B
					x-=1
					d-=A
		else:
			if dy<dx:
	#Octant 6
				A=y1-y0
				B=-1*(x1-x0)
				B=2*B
				d=0-A-B
				A=2*A
				x=x0
				y=y0
				while y>=y1:
					plot(screen, color, x, y)
					if d<0:
						x-=1
						d-=A
					y-=1
					d-=B
			else:
	#Octant 5
				A=y1-y0
				B=-1*(x1-x0)
				A=2*A
				d=0-A-B
				B=2*B
				x=x0
				y=y0
				while x >= x1:
					plot(screen, color, x, y)
					if d > 0:
						y-=1
						d-=B
					x-=1
					d-=A
