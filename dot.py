from pygame import Rect
# from curve import Curve

class Dot:
	# x = 0
	# y = 0
	# rect = Rect(0, 0, 0, 0)
	# base = True
	# owners = []

	def __init__(self, left, top, base, owners):
		# self.x = 0
		# self.y = 0
		# self.rect = Rect(0, 0, 0, 0)
		# self.base = True
		self.owners = []
		self.base = base
		self.x = left
		self.y = top

		if base:
			self.rect = Rect(self.x, self.y, 10, 10)
		else:
			self.rect = Rect(left, top, 1, 1)

		self.owners = owners

	def __str__(self):
		res = str(self.rect.x) + " "
		res += str(self.rect.y) + " "
		res += str(self.base)
		return res