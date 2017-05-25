import pygame
from dot import Dot
from functions import *

class Curve:
	def __init__(self, base):
		self.dots_count = 1000
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
		self.old_e1 = None
		self.old_e2 = None
		self.e1 = None
		self.e2 = None

		self.k = None
		self.j = None
		self.l = None
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
			base_dot.owners.append(self)
			base_dot.update()
		for lever in self.levers:
			lever.owners.append(self)
			lever.update()

		self.dots[:] = []

		for count in range(self.dots_count):
			temp = self.bezierPoint(count/self.dots_count)
			self.dots.append(temp)

	def draw(self, bg):
		for bdot in self.base_dots:
			pygame.draw.rect(bg, pygame.Color("#000000"), bdot.rect, 2)
		# if self.lever_visibility:
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

	def draw_algo(self, img, dragged_dot):
		pygame.draw.line(img, pygame.Color("#ff0000"), (self.a.x, self.a.y), (dragged_dot.x, dragged_dot.y))
		pygame.draw.line(img, pygame.Color("#00ff00"), (dragged_dot.x, dragged_dot.y), (self.c.x, self.c.y))

		pygame.draw.line(img, pygame.Color("#0000ff"), (self.e1.x, self.e1.y), (self.e2.x, self.e2.y))

		pygame.draw.line(img, pygame.Color("#ff00ff"), (self.k.x, self.k.y), (self.a.x, self.a.y))
		pygame.draw.line(img, pygame.Color("#ff00ff"), (self.a.x, self.a.y), (self.l.x, self.l.y))

		pygame.draw.line(img, pygame.Color("#00ffff"), (self.base_dots[1].x, self.base_dots[1].y), (self.base_dots[0].x, self.base_dots[0].y))
		pygame.draw.line(img, pygame.Color("#00ffff"), (self.levers[1].x, self.levers[1].y), (self.levers[0].x, self.levers[0].y))

	def get_old_id(self, dot):
		self.b = get_B(dot)
		self.t = get_t(dot)
		self.c = get_c(self.base_dots[0], self.base_dots[-1], self.t)
		self.ratio = ratio_t(self.t)
		self.a = get_a(self.b,self.c,self.ratio)
		self.old_e1 = get_old_e1(self.base_dots[0], self.levers[0], self.levers[-1], self.t)
		self.old_e2 = get_old_e2(self.base_dots[-1], self.levers[-1], self.levers[0], self.t)
		self.e1 = get_old_e1(self.base_dots[0], self.levers[0], self.levers[-1], self.t)
		self.e2 = get_old_e2(self.base_dots[-1], self.levers[-1], self.levers[0], self.t)		

	def get_new_id(self, dragged_dot):
		self.a = get_new_a(dragged_dot,self.c,self.ratio)
		self.e1 = get_e1(dragged_dot,self.old_e1, self.b)
		self.e2 = get_e2(dragged_dot,self.old_e2, self.b)
		self.levers[0] = get_c_start(self.base_dots[0], self.a, self.e1, self.t)
		self.levers[-1] = get_c_end(self.base_dots[-1], self.a, self.e2, self.t)
		self.k = get_k(self.base_dots[0], self.levers[0], self.t)
		self.j = get_j(self.levers[0], self.levers[-1], self.t)
		self.l = get_l(self.base_dots[-1], self.levers[-1], self.t)