from pygame import Rect
# from curve import Curve

class Dot:
	def __init__(self, left, top, base, owners):
		self.owners = []
		self.base = base
		self.x = left
		self.y = top

		if self.base:
			self.rect = Rect(self.x, self.y, 10, 10)
		else:
			self.rect = Rect(self.x, self.y, 1, 1)

		self.owners = owners

	def update(self):
		if self.base:
			self.rect = Rect(self.x, self.y, 10, 10)
		else:
			self.rect = Rect(self.x, self.y, 1, 1)

	def __str__(self):
		res = str(self.rect.x) + " "
		res += str(self.rect.y) + " "
		res += str(self.base)
		return res