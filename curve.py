import pygame
from dot import Dot

class Curve:
	def __init__(self, base):
		self.dots_count = 1000
		self.base_dots = []
		self.dots = []
		for dot in base:
			self.base_dots.append(dot)
			dot.owners.append(self)

		count = 0

		while count != self.dots_count:
			temp = self.bezierPoint(count/self.dots_count)
			self.dots.append(temp)
			count += 1
	
	def update(self):
		for base_dot in self.base_dots:
			base_dot.update()
		count = 0
		self.dots[:] = []
		while count != self.dots_count:
			temp = self.bezierPoint(count/self.dots_count)
			self.dots.append(temp)
			count += 1	

	def draw(self, bg):
		for bdot in self.base_dots:
			pygame.draw.rect(bg, pygame.Color("#000000"), bdot.rect, 1)

		for dot in self.dots:
			pygame.draw.rect(bg, pygame.Color("#000000"), dot.rect, 1)

	def __str__(self):
		res = ""
		for dot in self.base_dots:
			res += str(dot)
			res += str('\n')
		return res


	def bezierPoint(self, t):
		u = 1-t
		tt = t*t
		uu = u*u
		uuu = uu * u
		ttt = tt * t

		p = []
		p.append(self.base_dots[0].x * uuu)
		p.append(self.base_dots[0].y * uuu)

		p[0] += self.base_dots[1].x * (3 * uuu * t)
		p[1] += self.base_dots[1].y * (3 * uuu * t)

		p[0] += self.base_dots[2].x * (3 * u * tt)
		p[1] += self.base_dots[2].y * (3 * u * tt)
		
		p[0] += self.base_dots[3].x * ttt
		p[1] += self.base_dots[3].y * ttt

		return Dot(p[0], p[1], False, self)