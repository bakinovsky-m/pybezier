

class Figure:
    def __init__(self):
        self.base_dots = []
        self.curves = []
        self.dragged_curve = None

    def addCurve(self, curve):
        self.curves.append(curve)