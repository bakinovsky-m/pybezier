import pygame
from dot import Dot
from functions import *

class Curve:
	def __init__(self, base):
		self.dots_count = 100
		self.base_dots = []
		self.levers = []
		self.dots = []
		self.lever_visibility = True
		self.dot_moved = None

		## for dragging section:
		self.b = None
		self.t = None
		self.c = None
		self.ratio = None
		self.a = None
		self.e1 = None
		self.e2 = None
		#
		
		for dot in base:
			if dot.type == "base":
				self.base_dots.append(dot)
			elif dot.type == "lever":
				self.levers.append(dot)

			dot.owners.append(self)

		for count in range(self.dots_count):
			temp = self.bezierPoint(count/self.dots_count)
			self.dots.append(temp)
	
	def update(self):
		for base_dot in self.base_dots:
			base_dot.update()
		for lever in self.levers:
			lever.update()

		self.dots[:] = []

		for count in range(self.dots_count):
			temp = self.bezierPoint(count/self.dots_count)
			self.dots.append(temp)

	# def update(self):
	# 	for base_dot in self.base_dots:
	# 		base_dot.update()
	# 	# for dot in self.dots:
	# 	if self.dot_moved != None and self.mozhno_movat:
	# 		b = get_B(self.dot_moved)
	# 		# t = get_t(b)
	# 		t = get_t(self.dot_moved)
	# 		c = get_c(self.base_dots[0], self.base_dots[-1], t)
	# 		ratio = ratio_t(t)
	# 		a = get_a(b,c,ratio)
	# 		new_a = get_new_a(self.dot_moved, c, ratio)
	# 		e1 = get_e1(self.dot_moved, self.base_dots[0], self.levers[0], a, b, t)
	# 		e2 = get_e2(self.dot_moved, self.base_dots[-1], self.levers[-1], a, b, t)
	# 		c_start = get_c_start(self.base_dots[0], new_a, e1, t)
	# 		c_end = get_c_end(self.base_dots[-1], new_a, e2, t)

	# 		self.levers[0].x = c_start.x
	# 		self.levers[0].y = c_start.y
	# 		self.levers[1].x = c_end.x
	# 		self.levers[1].y = c_end.y

	# 		self.dot_moved = None
	# 	for lever in self.levers:
	# 		lever.update()
	# 		# dot.update()

	def draw(self, bg):
		for bdot in self.base_dots:
			pygame.draw.rect(bg, pygame.Color("#000000"), bdot.rect, 2)
		if self.lever_visibility:
			for lever in self.levers:
				pygame.draw.rect(bg, pygame.Color("#000000"), lever.rect, 1)
				pygame.draw.line(bg, pygame.Color("#000000"), (lever.x, lever.y), (self.base_dots[self.levers.index(lever)].x, self.base_dots[self.levers.index(lever)].y), 1)

		for dot in self.dots:
			pygame.draw.rect(bg, pygame.Color("#000000"), dot.rect, 1)
			pygame.draw.rect(bg, pygame.Color("#000000"), dot.inv_rect, 1)

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

		p[0] += self.levers[0].x * (3 * uu * t)
		p[1] += self.levers[0].y * (3 * uu * t)

		p[0] += self.levers[1].x * (3 * u * tt)
		p[1] += self.levers[1].y * (3 * u * tt)
		
		p[0] += self.base_dots[1].x * ttt
		p[1] += self.base_dots[1].y * ttt

		return Dot(p[0], p[1], False, self)