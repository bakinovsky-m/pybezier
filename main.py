import pygame
from pygame import *

clock = time.Clock()

WIN_H = 800
WIN_W = 600
DISPLAY = (WIN_H, WIN_W)
BG_COLOR = "#004400"

class Vec2:
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __mul__(self, a):
		return Vec2(self.x * a.x, self.y * a.y)

	def __add__(self, a):
		return Vec2(self.x + a.x, self.y + a.y)

	def multiply(self, a):
		return Vec2(self.x * a, self.y * a)

	def retTuple(self):
		return (self.x, self.y)

def bezierPoint(t, p0, p1, p2, p3):
	u = 1-t
	tt = t*t
	uu = u*u
	uuu = uu * u
	ttt = tt * t

	p = p0.multiply(uuu)
	p += p1.multiply(3*uu*t)
	p += p2.multiply(3*u*tt)
	p += p3.multiply(ttt)

	return p.retTuple()

def main():
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("Bezier")
	bg = Surface(DISPLAY)
	bg.fill(Color(BG_COLOR))

	p0 = Vec2(0, 0)
	p1 = Vec2(0,400)
	p2 = Vec2(400, 400)
	p3 = Vec2(400,0)

	lines = []

	done = False
	iters = 1000
	count = 0
	while not done:
		if count == iters:
			done = True

		temp = bezierPoint(count/iters, p0, p1, p2, p3)

		lines.append(temp)
		count += 1

	print("adding lines done!")
	print(lines)

	quit = False
	while not quit:
		clock.tick(2)
		for ev in pygame.event.get():
			if ev.type == QUIT:
				quit = True
		screen.blit(bg, (0,0))
		draw.lines(bg, Color("#000000"), False, lines, 1)
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()