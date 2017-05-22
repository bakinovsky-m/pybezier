

class Figure:
	def __init__(self):
		self.base_dots = []
		self.curves = []

	def addCurve(self, curve):
		self.curves.append(curve)