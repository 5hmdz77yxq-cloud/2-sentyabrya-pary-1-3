class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        sides = [self.a, self.b, self.c]
        for side in sides:
            if not isinstance(side, (int, float)) or side <= 0:
                return 1
        a, b, c = sorted(sides)
        if a + b <= c:
            return 2
        return 3

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
