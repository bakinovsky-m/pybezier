from pygame import Rect
# from curve import Curve

class Dot:
	def __init__(self, left, top, type_, owners):
		self.owners = []
		## base, lever or whatever else
		self.type = type_
		self.x = left
		self.y = top

		if self.type == "base" or self.type == "lever":
			self.rect = Rect((self.x-5), (self.y-5), 10, 10)
		else:
			self.rect = Rect((self.x-0.5), (self.y), 1, 1)
			self.inv_rect = Rect((self.x-5), (self.y), 5, 5)

		self.update()

		self.owners = owners

	def update(self):
		if self.type == "base" or self.type == "lever":
			self.rect = Rect((self.x-5), (self.y-5), 10, 10)
		else:
			self.rect = Rect((self.x-0.5), (self.y), 1, 1)
			self.inv_rect = Rect((self.x-2.5), (self.y), 5, 5)

	def __str__(self):
		res = str(self.rect.x) + " "
		res += str(self.rect.y) + " "
		res += str(self.type)
		return res