import pygame
from pygame import *

clock = time.Clock()

WIN_H = 800
WIN_W = 600
DISPLAY = (WIN_H, WIN_W)
BG_COLOR = "#004400"

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
	p.append(p0.x * uuu)

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

def main():
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("Bezier")
	bg = Surface(DISPLAY)
	bg.fill(Color(BG_COLOR))

	p0 = Rect(0,0, 10, 10)
	p1 = Rect(0, 400, 10, 10)
	p2 = Rect(400, 400, 10, 10)
	p3 = Rect(400, 0, 10, 10)

	print("adding dots done!")

	p = (1, 1)
	p += (2, 2)
	print(p)

	mouse_dragging = False
	quit = False
	display.update()
	while not quit:
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

		clock.tick(120)
		for ev in pygame.event.get():
			if ev.type == QUIT:
				quit = True
			elif ev.type == MOUSEBUTTONDOWN:
				if ev.button == 1:
					if p0.collidepoint(ev.pos):
						mouse_dragging = 1
						mouse_x, mouse_y = ev.pos
						offset_x = p0.x - mouse_x
						offset_y = p0.y - mouse_y

			elif ev.type == MOUSEBUTTONUP:
				mouse_dragging = False

			elif ev.type == MOUSEMOTION:
				if mouse_dragging:
					mouse_x, mouse_y = ev.pos
					p0.x = mouse_x + offset_x
					p0.y = mouse_y + offset_y


		screen.blit(bg, (0,0))
		count = 0
		while count != iters:
			# draw.circle(bg, Color("#000000"), dots[count], 1)
			draw.rect(bg, Color("#000000"), dots[count], 10)
			count += 1
		draw.rect(bg, Color("#000000"), p0, 1)
		draw.rect(bg, Color("#000000"), p1, 1)
		draw.rect(bg, Color("#000000"), p2, 1)
		draw.rect(bg, Color("#000000"), p3, 1)
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()