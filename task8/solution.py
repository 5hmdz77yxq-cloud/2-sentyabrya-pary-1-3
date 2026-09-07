class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print("Рисуется линия")

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print("Рисуется прямоугольник")

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print("Рисуется эллипс")

class Triangle(Figure):
    def __init__(self, coords, width, color, side):
        super().__init__(coords, width, color)
        self.side = side

    def draw(self):
        print("Рисуется треугольник")

figures = [
    Line((0,0), 2, "red", 10),
    Rect((5,5), 3, "blue", 7),
    Ellipse((1,1), 1, "green", 4)
]

figures.append(Triangle((2,3), 1, "yellow", 5))

for fig in figures:
    fig.draw()