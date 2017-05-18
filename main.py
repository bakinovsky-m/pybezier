import pygame
import math
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
	dragged_curves = []
	dragging = 0
	index_of_first_curve_in_cycle = 0

	done = False
	while not done:
		clock.tick(FPS)
		
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				done = True
			elif ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_q:
					done = True
				elif ev.key == pygame.K_SPACE:
					if mode == 0:
						mode = 1
					elif mode == 1:
						mode = 0
				elif ev.key == pygame.K_f:
					b1 = curves[-1].base_dots[-1]
					b2 = curves[index_of_first_curve_in_cycle].base_dots[0]
					lever1 = Dot(b1.x + 10, b1.y + 10, "lever", [])
					lever2 = Dot(b2.x + 10, b2.y + 10, "lever", [])
					temp_curve = Curve([b1, lever1, lever2, b2])
					curves.append(temp_curve)
				elif ev.key == pygame.K_c:
					base_dots = []
					curves = []
					index_of_first_curve_in_cycle = 0
				# elif ev.key == pygame.K_d:
				# 	curves.pop()
				elif ev.key == pygame.K_n:
					index_of_first_curve_in_cycle  = len(curves)
					base_dots = []

			## adding mode
			if ev.type == pygame.MOUSEBUTTONDOWN and mode == 0:
				mouse_x, mouse_y = ev.pos
				temp_dot = Dot(mouse_x, mouse_y, "base", [])

				## levers inserts between last dot in list (which is fisrt point at all or base point of last curve)
				## and new base point of current curve
				base_dots.append(temp_dot)
				if len(base_dots) > 1:
					lever_dot1 = Dot(base_dots[-2].x + 10, base_dots[-2].y + 10, "lever", base_dots[-1].owners)
					base_dots.insert(-1, lever_dot1)
					lever_dot2 = Dot(temp_dot.x + 10, temp_dot.y + 10, "lever", base_dots[-1].owners)
					base_dots.insert(-1, lever_dot2)
					b = [base_dots[-4], base_dots[-3], base_dots[-2], base_dots[-1]]
					temp_curve = Curve(b)
					curves.append(temp_curve)
				##

			## edit mode
			elif mode == 1:
				if ev.type == pygame.MOUSEBUTTONDOWN:
					if ev.button == 1:
						for curve in curves:
							for base_dot in curve.base_dots:
								if base_dot.rect.collidepoint(ev.pos):
									mouse_dragging = True
									dragging = "base"
									mouse_x, mouse_y = ev.pos
									offset_x = base_dot.rect.x - mouse_x
									offset_y = base_dot.rect.y - mouse_y
									dragged_dot = base_dot
									dragged_curves.append(curve)
							for lever in curve.levers:
								if lever.rect.collidepoint(ev.pos):
									mouse_dragging = True
									dragging = "lever"
									mouse_x, mouse_y = ev.pos
									offset_x = lever.rect.x - mouse_x
									offset_y = lever.rect.y - mouse_y
									dragged_dot = lever
									dragged_curves.append(curve)

				elif ev.type == pygame.MOUSEBUTTONUP:
					mouse_dragging = False
					dragged_curves = []

				elif ev.type == pygame.MOUSEMOTION:
					if mouse_dragging:
						mouse_x, mouse_y = ev.pos

						temp_x = dragged_dot.x
						temp_y = dragged_dot.y

						dragged_dot.x = mouse_x + offset_x
						dragged_dot.y = mouse_y + offset_y

						if dragging == "base":
							for dragged_curve in dragged_curves:
								ind = dragged_curve.base_dots.index(dragged_dot)
								# if ind:
								l = dragged_curve.levers[ind]
								l.x = l.x - (temp_x - dragged_dot.x)
								l.y = l.y - (temp_y - dragged_dot.y)



		## fill with bg_color, THEN draw on bg and then BLIT bg on screen. works fine
		bg.fill(BG_COLOR)

		for c in curves:
			c.update()
			c.draw(bg)

		screen.blit(bg, (0,0))
		##

		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()