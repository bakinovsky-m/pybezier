import pygame
# from pygame import *
from dot import Dot
from curve import Curve 

def main():
	a = Dot(1, 1, False, 0)
	b = Dot(1, 2, True, 0)
	c = Dot(1, 2, True, 0)
	d = Dot(1, 2, True, 0)

	curve = Curve((a,b,c,d))
	print(len(curve.dots))

	# print(a)
	pygame.init()
	pygame.quit()

if __name__ == "__main__":
	main()