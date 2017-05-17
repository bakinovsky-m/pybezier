from dot import Dot

class Curve:
	dots_count = 1000
	base_dots = []
	dots = []

	# def bezierPoint(self, t, base_dots):
	def bezierPoint(self, t):
		u = 1-t
		tt = t*t
		uu = u*u
		uuu = uu * u
		ttt = tt * t

		p = []
		p.append(self.base_dots[0].x * uuu)
		p.append(self.base_dots[0].y * uuu)

		p[0] += self.base_dots[1].x * (3 * uuu * t)
		p[1] += self.base_dots[1].y * (3 * uuu * t)

		p[0] += self.base_dots[2].x * (3 * u * tt)
		p[1] += self.base_dots[2].y * (3 * u * tt)
		
		p[0] += self.base_dots[3].x * ttt
		p[1] += self.base_dots[3].y * ttt

		# return Rect(p[0], p[1], 1, 1)
		return Dot(p[0], p[1], False, self)

	def __init__(self, base):
		for dot in base:
			self.base_dots.append(dot)

		count = 0

		while count != self.dots_count:
			temp = self.bezierPoint(count)
			self.dots.append(temp)
			count += 1