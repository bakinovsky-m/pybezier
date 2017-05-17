from pygame import Rect
# from curve import Curve

class Dot:
	x = 0
	y = 0
	rect = Rect(0, 0, 0, 0)
	base = True
	owner = 0

	def __init__(self, left, top, base, owner):
		self.base = base
		self.x = left
		self.y = top

		if base:
			self.rect = Rect(left, top, 10, 10)
		else:
			self.rect = Rect(left, top, 1, 1)

		self.owner = owner

	def __str__(self):
		res = str(self.rect.x) + " "
		res += str(self.rect.y) + " "
		res += str(self.base)
		return res