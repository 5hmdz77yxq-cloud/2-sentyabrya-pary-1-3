class Graph:
    def __init__(self, x=0, y=0, scale=1):
        self._x = x
        self._y = y
        self._scale = scale

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        self._scale *= factor

    def get_state(self):
        return f"x={self._x}, y={self._y}, scale={self._scale}"

g1 = Graph(10, 20, 2)
g2 = Graph(5, 5, 1)
g3 = Graph(0, 0, 1)

g1.move(5, -5)
g2.change_scale(3)

print("g1:", g1.get_state())
print("g2:", g2.get_state())
print("g3:", g3.get_state())