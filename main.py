import pygame
import math
import sys
from dot import Dot
from curve import Curve 
from figure import Figure

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

	# image loading init
	if len(sys.argv) == 1:
		image = pygame.image.load("metro.jpg")
	else:
		image = pygame.image.load(sys.argv[1])
	img = image.copy()

	# screen = pygame.display.set_mode(DISPLAY)
	screen = pygame.display.set_mode(img.get_rect().size)
	pygame.display.set_caption("Bezier")
	mouse_dragging = False

	# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
	font = pygame.font.SysFont("monospace", 12)
	# render text
	text_label_instr = font.render("q: quit; c: clear; f: finalize; u: undo; n: new cycle; space: change mode", 1, (0,0,0))
	text_label_mode = font.render("edit mode", 1, (255,0,0))
	##

	mode = 0
	dragged_dot = 0

	figures = []

	done = False
	while not done:
		clock.tick(FPS)

		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				done = True
			elif ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_q or ev.key == pygame.K_ESCAPE:
					done = True
				elif ev.key == pygame.K_SPACE:
					if mode == 0:
						mode = 1
					elif mode == 1:
						mode = 0
				elif ev.key == pygame.K_f:
					b1 = current_figure.curves[-1].base_dots[-1]
					b2 = current_figure.curves[0].base_dots[0]
					lever1 = calculateLever(b1, b2)
					lever2 = calculateLever(b1, b2)
					temp_curve = Curve([b1, lever1, lever2, b2])
					current_figure.curves.append(temp_curve)

				elif ev.key == pygame.K_c:
					figures = []

				elif ev.key == pygame.K_u:
					if len(current_figure.curves) > 0:
						current_figure.curves.pop()
					elif len(figures) > 0:
						figures.pop()
						if len(figures) != 0:
							current_figure = figures[-2]



				elif ev.key == pygame.K_n:
					temp_figure = Figure()
					figures.append(temp_figure)
					current_figure = temp_figure

			## adding mode
			if ev.type == pygame.MOUSEBUTTONDOWN and mode == 0:
				if len(figures) == 0:
					temp_figure = Figure()
					current_figure = temp_figure
					figures.append(temp_figure)
				mouse_x, mouse_y = ev.pos
				temp_dot = Dot(mouse_x, mouse_y, "base", [])

				current_figure.base_dots.append(temp_dot)
				if len(current_figure.base_dots) > 1:
					prev_dot = current_figure.base_dots[-2]
					lever1 = calculateLever(prev_dot, temp_dot)
					lever2 = calculateLever(prev_dot, temp_dot)
					c = Curve((prev_dot, lever1, lever2, temp_dot))
					current_figure.addCurve(c)
				##

			## edit mode
			elif mode == 1:
				if ev.type == pygame.MOUSEBUTTONDOWN:
					if ev.button == 1:
						for f in figures:
							for curve in f.curves:
								mouse_x, mouse_y = ev.pos

								poly = []
								poly.append((curve.base_dots[0].x, curve.base_dots[0].x))
								poly.append((curve.levers[0].x, curve.levers[0].y))
								poly.append((curve.levers[1].x, curve.levers[1].y))
								poly.append((curve.base_dots[1].x, curve.base_dots[1].x))

								for base_dot in curve.base_dots:
									if base_dot.rect.collidepoint(ev.pos):
										mouse_dragging = True
										offset_x = base_dot.rect.x - mouse_x
										offset_y = base_dot.rect.y - mouse_y
										dragged_dot = base_dot
								for lever in curve.levers:
									if lever.rect.collidepoint(ev.pos):
										mouse_dragging = True
										offset_x = lever.rect.x - mouse_x
										offset_y = lever.rect.y - mouse_y
										dragged_dot = lever

								if point_inside_polygon(mouse_x, mouse_y, poly):
									for dot in curve.dots:
										if dot.inv_rect.collidepoint(ev.pos):
											mouse_dragging = True
											offset_x = dot.inv_rect.x - mouse_x
											offset_y = dot.inv_rect.y - mouse_y
											dragged_dot = dot
											print("ALARM")
										# pass



				elif ev.type == pygame.MOUSEBUTTONUP:
					mouse_dragging = False

				elif ev.type == pygame.MOUSEMOTION:
					if mouse_dragging:
						mouse_x, mouse_y = ev.pos

						dragged_dot.x = mouse_x + offset_x
						dragged_dot.y = mouse_y + offset_y


		for f in figures:
			for c in f.curves:
				c.update()
				c.draw(img)

		screen.blit(image, (0,0))
		screen.blit(img, (0,0))
		screen.blit(text_label_instr, (0, 0))
		if mode:
			screen.blit(text_label_mode, (0, 15))

		img = image.copy()

		pygame.display.update()

	pygame.quit()

def calculateLever(b1, b2):
	mid = ((b1.x + b2.x)/2, (b1.y + b2.y)/2)
	coords = (mid[0], mid[1])
	return Dot(coords[0], coords[1], "lever", [])

# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.

def point_inside_polygon(x, y, poly):

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n + 1):
        p2x,p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


if __name__ == "__main__":
	main()