from math import sqrt

# Определили класс
class Point:
    # Определили конструктор
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Определили метод
    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    # Переопределили операцию так, как нам хочется
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# print(Point(0, 0).distance(Point(3, 4)))

a = Point(0, 0)
b = Point(3, 4)
print(a.distance(b))
print(a == b)
print(a == Point(0, 0))
