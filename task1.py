import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        a = self.vertices[0].distance_from_point(self.vertices[1])
        b = self.vertices[1].distance_from_point(self.vertices[2])
        c = self.vertices[2].distance_from_point(self.vertices[0])
        return a + b + c


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())