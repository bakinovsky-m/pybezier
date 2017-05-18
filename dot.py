from pygame import Rect
# from curve import Curve

class Dot:
	def __init__(self, left, top, type, owners):
		self.owners = []
		## base, lever or whatever else
		self.type = type
		self.x = left
		self.y = top

		if self.type == "base" or self.type == "lever":
			self.rect = Rect(self.x, self.y, 10, 10)
		else:
			self.rect = Rect(self.x, self.y, 1, 1)

		self.owners = owners

	def update(self):
		if self.type == "base" or self.type == "lever":
			self.rect = Rect(self.x, self.y, 10, 10)
		else:
			self.rect = Rect(self.x, self.y, 1, 1)

	def __str__(self):
		res = str(self.rect.x) + " "
		res += str(self.rect.y) + " "
		res += str(self.type)
		return res