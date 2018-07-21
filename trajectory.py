#TRAJECTORY CALCULATION



#make imports
from math import sqrt
from math import cos, sin, atan2 as atan



#vector class
class Vector:

	"""
	Vector property calculations class

	Args:
		float cx (optional): component in x direction
		float cy (optional): component in y direction
	"""

	#constructor
	def __init__(self, cx, cy):

		#set vector components
		self.compx = cx
		self.compy = cy

		#calculate magnitude and angle
		self.mag = sqrt(abs(self.compx**2 + self.compy**2))
		self.angle = atan(self.compy, self.compx)

	def calcMag(self):

		"""
		Calculate magnitude of vector
		"""

		#recalculate magnitude
		self.mag = sqrt(abs(self.compx**2 + self.compy**2))
	
	def calcAngle(self):

		"""
		Calculate angle of vector from positive x axis
		"""

		#recalculate angle
		self.angle = atan(self.compy, self.compx)

	def calcDist(self, res, alt):

		"""
		Calculate distance travelled by vector

		Args:
			float res: resistance in newtons
			float alt: custom altitude
		Returns:
			float dist: distance travelled in metres
		"""

		#get time in flight
		at = sqrt(abs(alt/4.9)) #altitude time
		ot = sqrt(abs(float(res)**2 - self.mag**2)) #calculated time

		#check time to use
		if at < ot:
			return (self.mag / 2) * at
		
		else:
			return (self.mag / 2) * ot

	def XinRange(self, ax):

		"""
		Calculate if X coordinate within range of vector

		Args:
			float ax: X coordinate
		Retruns:
			bool inRange: is coordinate in vector's range
		"""

		#return bool
		return ax <= self.mag*cos(self.angle)

	def YinRange(self, ay):
		
		"""
		Calculate if Y coordinate within range of vector

		Args:
			float ay: Y coordinate
		Retruns:
			bool inRange: is coordinate in vector's range
		"""

		#return bool
		return ay <= self.mag*sin(self.angle)

	def inRange(self, px, py):

		"""
		Calculate if coordinates within range of vector

		Args:
			float px: X coordinate
			float py: Y coordinate
		Retruns:
			bool inRange: are coordinates in vector's range
		"""

		#return bool
		return self.XinRange(px) and self.YinRange(py)
	
	def genDistCoor(self, res, alt):

		"""
		Generate points for distance end
		
		Args:
			float res: resistance in newtons
			float alt: custom altitude
		Returns
			list pts: array with two elements as coors
		"""

		#calculate distance
		vd = self.calcDist(res, alt)

		#return array
		return [vd*cos(self.angle), vd*sin(self.angle)]