#import pygame
#from pygame import *

import pygame, sys
from pygame import *


WIN_H = 800
WIN_W = 600
DISPLAY = (WIN_H, WIN_W)
BG_COLOR = "#004400"

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY)



# class Vec2:
# 	x = 0
# 	y = 0

# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# 	def __mul__(self, a):
# 		return Vec2(self.x * a.x, self.y * a.y)

# 	def __add__(self, a):
# 		return Vec2(self.x + a.x, self.y + a.y)

# 	def multiply(self, a):
# 		return Vec2(self.x * a, self.y * a)

# 	def retTuple(self):
# 		return (self.x, self.y)

# 	def retIntTuple(self):
# 		return (int(self.x), int(self.y))

def bezierPoint(t, p0, p1, p2, p3):
	u = 1-t
	tt = t*t
	uu = u*u
	uuu = uu * u
	ttt = tt * t

	# p = Vec2(p0.x * uuu, p0.y * uuu)
	# p += Vec2(p1.x * (3 * uuu * t), p1.y * (3 * uuu * t))
	# p += Vec2(p2.x * (3 * u * tt), p2.y * (3 * u * tt))
	# p += Vec2(p3.x * ttt, p3.y * ttt)

	# return p.retIntTuple()
	
	# p = p0.x * uuu, p0.y * uuu
	p = []
	p.append(p0.x * uuu)
	p.append(p0.y * uuu)

	# p += p1.x * (3 * uuu * t), p1.y * (3 * uuu * t)
	p[0] += p1.x * (3 * uuu * t)
	p[1] += p1.y * (3 * uuu * t)
	# p += p2.x * (3 * u * tt), p2.y * (3 * u * tt)
	p[0] += p2.x * (3 * u * tt)
	p[1] += p2.y * (3 * u * tt)
	# p += p3.x * ttt, p3.y * ttt
	p[0] += p3.x * ttt
	p[1] += p3.y * ttt

	return Rect(p[0], p[1], 1, 1)

def drawAll(screen, bg, iters, dots, p0, p1, p2, p3):
	# screen.fill(Color(BG_COLOR))
	# bg.fill(Color(BG_COLOR))
	# screen.blit(bg, (0,0))
	count = 0
	while count != iters:
		# draw.circle(bg, Color("#FFFFFF"), dots[count], 1)
		draw.rect(bg, Color("#FFFFFF"), dots[count], 1)
		count += 1
	draw.rect(bg, Color("#FFFFFF"), p0, 1)
	draw.rect(bg, Color("#FFFFFF"), p1, 1)
	draw.rect(bg, Color("#FFFFFF"), p2, 1)
	draw.rect(bg, Color("#FFFFFF"), p3, 1)

def main():
	pygame.init()
#	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("Bezier")
	#bg = Surface(DISPLAY)
	#bg.fill(Color(BG_COLOR))
	bg = pygame.image.load("bg.jpg").convert()
	bg = pygame.transform.scale(bg,DISPLAY)
	clock.tick(60)

	p0 = Rect(0,0, 10, 10)
	p1 = Rect(0, 400, 10, 10)
	p2 = Rect(400, 400, 10, 10)
	p3 = Rect(400, 0, 10, 10)

	print("adding dots done!")

	p = (1, 1)
	p += (2, 2)
	print(p)

	mouse_dragging_0 = False
	mouse_dragging_1 = False
	mouse_dragging_2 = False
	mouse_dragging_3 = False
	quit = False
	display.update()
	while not quit:
		
		screen.blit(bg, (0,0))
		dots = []

		done = False
		iters = 1000
		count = 0
		while not done:
			if count == iters:
				done = True

			temp = bezierPoint(count/iters, p0, p1, p2, p3)

			dots.append(temp)
			count += 1

		
		for ev in pygame.event.get():
			if ev.type == QUIT:
				quit = True
			elif ev.type == MOUSEBUTTONDOWN:
				if ev.button == 1:
					if p0.collidepoint(ev.pos):
						mouse_dragging_0 = 1
						mouse_x, mouse_y = ev.pos
						offset_x = p0.x - mouse_x
						offset_y = p0.y - mouse_y
					elif p1.collidepoint(ev.pos):
						mouse_dragging_1 = 1
						mouse_x, mouse_y = ev.pos
						offset_x = p1.x - mouse_x
						offset_y = p1.y - mouse_y
					elif p2.collidepoint(ev.pos):
						mouse_dragging_2 = 1
						mouse_x, mouse_y = ev.pos
						offset_x = p2.x - mouse_x
						offset_y = p2.y - mouse_y
					elif p3.collidepoint(ev.pos):
						mouse_dragging_3 = 1
						mouse_x, mouse_y = ev.pos
						offset_x = p3.x - mouse_x
						offset_y = p3.y - mouse_y

			elif ev.type == MOUSEBUTTONUP:
				mouse_dragging_0 = False
				mouse_dragging_1 = False
				mouse_dragging_2 = False
				mouse_dragging_3 = False


			elif ev.type == MOUSEMOTION:
				if mouse_dragging_0:
					mouse_x, mouse_y = ev.pos
					p0.x = mouse_x + offset_x
					p0.y = mouse_y + offset_y
					bg.fill(Color(BG_COLOR))
					drawAll(screen, bg, iters, dots, p0, p1, p2, p3)

				elif mouse_dragging_1:
					mouse_x, mouse_y = ev.pos
					p1.x = mouse_x + offset_x
					p1.y = mouse_y + offset_y
					#bg.fill(Color(BG_COLOR))
					drawAll(screen, bg, iters, dots, p0, p1, p2, p3)

				elif mouse_dragging_2:
					mouse_x, mouse_y = ev.pos
					p2.x = mouse_x + offset_x
					p2.y = mouse_y + offset_y
					#bg.fill(Color(BG_COLOR))
					drawAll(screen, bg, iters, dots, p0, p1, p2, p3)

				elif mouse_dragging_3:
					mouse_x, mouse_y = ev.pos
					p3.x = mouse_x + offset_x
					p3.y = mouse_y + offset_y
					#bg.fill(Color(BG_COLOR))
					drawAll(screen, bg, iters, dots, p0, p1, p2, p3)




		# screen.fill(Color(BG_COLOR))
		# screen.blit(bg, (0,0))
		# count = 0
		# while count != iters:
		# 	# draw.circle(bg, Color("#FFFFFF"), dots[count], 1)
		# 	draw.rect(bg, Color("#004400"), dots[count], 10)
		# 	count += 1
		# draw.rect(bg, Color("#FFFFFF"), p0, 1)
		# draw.rect(bg, Color("#FFFFFF"), p1, 1)
		# draw.rect(bg, Color("#FFFFFF"), p2, 1)
		# draw.rect(bg, Color("#FFFFFF"), p3, 1)
		drawAll(screen, bg, iters, dots, p0, p1, p2, p3)
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()