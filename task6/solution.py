class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

line = Line((0,0), 2, "red", 10)
rect = Rect((5,5), 3, "blue", 7)
ellipse = Ellipse((1,1), 1, "green", 4)

print(f"Line: coords={line.coords}, width={line.width}, color={line.color}, length={line.length}")
print(f"Rect: coords={rect.coords}, width={rect.width}, color={rect.color}, height={rect.height}")
print(f"Ellipse: coords={ellipse.coords}, width={ellipse.width}, color={ellipse.color}, radius={ellipse.radius}")