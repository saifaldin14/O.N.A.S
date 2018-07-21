#MAIN NAVIGATOR OPTIONS

#make imports
from math import cos, sin
from Tkinter import *
import tkFont
import time



#globals
global alt 
alt = 1500
xvals = []
yvals = []
tk = Tk()
global s
s = Canvas(tk, width=1000, height=1000, background="#000000")
s.pack()



def PlotVector(aVector, res, alt, scale):

	"""
	Plot vector on canvas

	Args:
		Canvas aCanv: TK canvas object
		Vector aVector: Vector object for coordinates
	"""

	(vx, vy) = aVector.genDistCoor(res, alt)

	return s.create_line(500, 500, 500+vx/scale, -1*vy/scale+500, fill="#ff0000", width=3)

def delPlot():
    s.delete("all")
    drawGrid()
    drawPlane()

def showStatus(text, x, y):

    f = tkFont.Font(family="Consolas", size=12)

    s.create_text(x, y, text=text, anchor=NW, font=f, fill="#eeeeee")

def blastRadius(v, r, s, res, alt):

    (vx, vy) = v.genDistCoor(res, alt)

    return createCircle(vx/s+500, vy/s*-1+500, float(r/s), "#ff0000")



def createCircle(x, y, r, f):

	"""
	Draw circle using centerpoint

	Args:
		Canvas aCanv: TK canvas object
		float x: x center coodrinate
		float y: y center coordinate
		float r: radius of circle
		string f: fill color
	"""
	
	s.create_oval(x-r, y-r, x+r, y+r, fill=f, outline="")



# Variables
ml = alt / 1000
glines = []



# Draws the grid
def drawGrid():
    global ml, glines, xvals, yvals
    cx = 500
    cy = 500
    xc = 0
    yc = 0

    c = "#d9d9d9"

    s.create_line(500, 0, 500, 1000, fill="#b3b3b3", width=2)
    s.create_line(0, 500, 1000, 500, fill="#b3b3b3", width=2)


    for g1 in range(2):
        if g1 == 1:
            yc = 0
        for g2 in range(1000):
        
            #Line value changing and drawing
            if g2 % 2 == 0:
                if g1 == 0:
                    l = s.create_line(cx + (xc*20), 0, cx + (xc*20), 1000, fill=c)
                    l2 = s.create_line(cx - (xc*20), 0, cx - (xc*20), 1000, fill=c)
                    xc += ml
                    yc = 500
                    xvals.append(xc)
                else:
                    l = s.create_line(0, cy + (yc*20), 1000, cy + (yc*20), fill=c)
                    l2 = s.create_line(0, cy - (yc*20), 1000, cy - (yc*20), fill=c)
                    yc += ml
                    xc = 500
                    yvals.append(yc)
                glines.append(l)
                glines.append(l2)



#Deletes the grid
def delGrid():
    global glines
    for g in range(len(glines)):
        s.delete(glines[0])
        glines.remove(glines[0])



#plane
def drawPlane():
    
    c = "#3399ff"

    s.create_line(500, 400, 500, 575, fill = c, width = 5)#frame
    s.create_line(500, 450, 550, 500, fill = c, width = 5)#right wing
    s.create_line(500, 450, 450, 500, fill = c, width = 5)#left wing
    s.create_line(500, 575, 550, 625, fill = c, width = 5)

    createCircle(500, 500, 6, "#99e6ff")



def reDrawAll():

    delGrid()
    drawPlane()
    drawGrid()


#execute
drawGrid()
drawPlane()