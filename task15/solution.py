class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range(1000):
    x = 1 + 2 * i
    y = 1 + 2 * i
    points.append(Point(x, y))

points[1].color = 'yellow'
