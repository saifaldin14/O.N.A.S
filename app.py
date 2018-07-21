#MAIN APPLICATION



#make imports
from navigator import *
from navigator.trajectory import *



#global vars
alt = 1000.0         #aircraft altitude
scale = alt/1000.0   #grid scale
ws = 5.0             #windspeed
v = 40               #aircraft velocity
br = 50              #blast radius
ot = 0.25            #ordinance air resistance
tar = [800, 200]     #target coordinates
vd = None            #drawn vector
rd = None            #radius drawn



#create vector object
vect = Vector(ws, v)



#title screen
print("O.N.A.S\n\n")



#main loop
while True:

	showStatus("ALTITUDE: " + str(alt) + "M", 0, 0)
	showStatus("PLANE SPEED: " + str(vect.compy) + "M/S", 0, 15)

	createCircle(tar[0], tar[1], 3, "#00ff00")

	#accept command
	cmd = raw_input("> ")

	#check commands
	if cmd == "planespeed":
		vect.compy = float(raw_input(""))
		vect.calcAngle(); vect.calcMag()
	
	elif cmd == "windspeed":
		vect.compx = float(raw_input(""))
		vect.calcAngle(); vect.calcMag()
	
	elif cmd == "ordinancetype":
		ot = float(raw_input(""))
	
	elif cmd == "run":
		delPlot()
		vd = PlotVector(vect, ot, alt, scale)
		rd = blastRadius(vect, br, scale, ot, alt)
		continue
	
	elif cmd == "clear":
		delPlot()
	
	elif cmd == "altitude":
		alt = float(raw_input(""))
		scale = alt/1000.0

	elif cmd == "target":
		tar[0] = float(raw_input(""))
		tar[1] = float(raw_input(""))

		delPlot()
		createCircle(tar[0], tar[1], 3, "#00ff00")
		continue
	
	elif cmd == "confirm":
		(x, y) = vect.genDistCoor(ot, alt)
		(tx, ty) = tar
		mt = sqrt((abs(tx-(x+500)))**2 + (abs(ty-(y*-1+500)))**2)
		if mt <= br:
			print("hit confirmed")
		else:
			print("no hit")

	elif cmd == "correct":

		print("FOR OPTIMAL TAGET ACQUISITION")
		(x, y) = vect.genDistCoor(ot, alt)

		deltaX = tar[0] - (x+500)
		deltaY = tar[1] - (y*-1+500)

		if deltaX > 3:
			print("INCREASE VELOCITY BY " + str(abs(deltaX)) + "m/s")
		elif deltaX < -3:
			print("DECREASE VELOCITY BY " + str(abs(deltaX)) + "m/s")

		if deltaY > 3 or deltaY < -3:
			print("ADJUST FOR WINDSPEED BY " + str(abs(deltaY)) + "m/s")
