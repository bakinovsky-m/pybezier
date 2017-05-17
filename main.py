import pygame
from dot import Dot
from curve import Curve 

## Global variables for pygame
WINDOW_H = 800
WINDOW_W = 600
DISPLAY = (WINDOW_H, WINDOW_W)
BG_COLOR = pygame.Color("#FFFFFF")
LINES_COLOR = pygame.Color("#000000")
FPS = 60
##

def main():
	a = Dot(100, 100, True, 0)
	b = Dot(1, 400, True, 0)
	c = Dot(400, 400, True, 0)
	d = Dot(400, 1, True, 0)

	curve = Curve((a,b,c,d))

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("Bezier")
	bg = pygame.Surface(DISPLAY)
	bg.fill(BG_COLOR)
	done = False
	while not done:
		clock.tick(FPS)
		screen.blit(bg, (0,0))
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				done = True

		curve.draw(bg)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()