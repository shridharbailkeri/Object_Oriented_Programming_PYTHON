import math

class Point:
    all_points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add_point(self):
        self.all_points.append((self.x, self.y))

    def distance(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

class Polygon:

    all_coords = Point.all_points


    def __init__(self, no_sides):
        self.no_sides = no_sides

    def perimeter(self):
        perimeter = 0
        for i in range(self.no_sides):
            all_points = self.all_coords + [self.all_coords[0]]
            x1, y1 = all_points[i]
            x2, y2 = all_points[i+1]
            perimeter += Point(x1, y1).distance(Point(x2, y2))
        return perimeter







if __name__ == '__main__':
    p1 = Point(11.55, 36.95)
    p1.add_point()
    p2  = Point(24.50, 44.61)
    p2.add_point()
    p3 = Point(37.35, 36.86)
    p3.add_point()
    p4 = Point(37.25, 21.45)
    p4.add_point()
    p5 = Point(24.40, 13.89)
    p5.add_point()
    p6 = Point(11.55, 21.45)
    p6.add_point()
    print(p6.all_points)
    print(p1.distance(p2))
    poly = Polygon(6)
    print(poly.all_coords)
    print(poly.perimeter())




