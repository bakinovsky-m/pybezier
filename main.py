import pygame
from dot import Dot
from curve import Curve 

## Global variables for pygame
WINDOW_H = 800
WINDOW_W = 600
DISPLAY = (WINDOW_H, WINDOW_W)
BG_COLOR = pygame.Color("#FFFFFF")
LINES_COLOR = pygame.Color("#000000")
FPS = 30
##

def main():
	# a = Dot(100, 100, True, 0)
	# b = Dot(1, 400, True, 0)
	# c = Dot(400, 400, True, 0)
	# d = Dot(400, 1, True, 0)

	# curve = Curve((a,b,c,d))

	## some init
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("Bezier")
	bg = pygame.Surface(DISPLAY)
	mouse_dragging = False
	##

	bg.fill(BG_COLOR)


	mode = 0
	curves = []
	base_dots = []
	dragged_dot = 0

	done = False
	while not done:
		# bg.fill(BG_COLOR)
		clock.tick(FPS)
		screen.blit(bg, (0,0))
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				done = True
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_q:
					done = True
				elif ev.key == pygame.K_SPACE:
					if mode == 0:
						mode = 1
					elif mode == 1:
						mode = 0

			## adding mode
			if ev.type == pygame.MOUSEBUTTONDOWN and mode == 0:
				mouse_x, mouse_y = ev.pos
				temp_dot = Dot(mouse_x, mouse_y, True, [])
				base_dots.append(temp_dot)
				if len(base_dots) > 1:
					b = [base_dots[-2], base_dots[-2], base_dots[-1], base_dots[-1]]
					temp_curve = Curve(b)
					curves.append(temp_curve)

			## edit mode
			elif mode == 1:
				if ev.type == pygame.MOUSEBUTTONDOWN:
					if ev.button == 1:
						for curve in curves:
							for base_dot in curve.base_dots:
								if base_dot.rect.collidepoint(ev.pos):
									mouse_dragging = True
									mouse_x, mouse_y = ev.pos
									offset_x = base_dot.rect.x - mouse_x
									offset_y = base_dot.rect.y - mouse_y
									dragged_dot = base_dot
				elif ev.type == pygame.MOUSEBUTTONUP:
					mouse_dragging = False

				elif ev.type == pygame.MOUSEMOTION:
					if mouse_dragging:
						mouse_x, mouse_y = ev.pos
						# for curve in curves:
						# 	for base_dot in curve.base_dots:
						# 		# mouse_dragging = True
						# 		base_dot.rect.x = mouse_x + offset_x
						# 		base_dot.x = mouse_x + offset_x
						# 		base_dot.rect.y = mouse_y + offset_y
						# 		base_dot.y = mouse_y + offset_y
							# curve.update()
						dragged_dot.rect.x = mouse_x + offset_x
						dragged_dot.x = mouse_x + offset_x
						dragged_dot.rect.y = mouse_y + offset_y
						dragged_dot.y = mouse_y + offset_y

		for c in curves:
			c.update()
			c.draw(bg)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()