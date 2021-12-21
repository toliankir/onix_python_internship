from abc import abstractmethod
import math


class Shape:
    def __init__(self, x=0, y=0, size=1):
        self.x = x
        self.y = y
        self.size = size

    @abstractmethod
    def get_area():
        pass

    @abstractmethod
    def get_vertex():
        pass

    def get_center(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(figure_1, figure_2):
        if not isinstance(figure_1, Shape) or not isinstance(figure_2, Shape):
            raise TypeError("Arguments must be class Shape")
        dx = figure_1.x - figure_2.x
        dy = figure_1.y - figure_2.y
        distance = math.sqrt(pow(dx, 2) + pow(dy, 2))
        return distance


class Circle(Shape):
    def get_area(self):
        area = math.pi * math.pow(self.size, 2)
        return area

    def get_vertex():
        raise TypeError('Not supported by this Shape')


class Square(Shape):
    def get_area(self):
        area = self.size * self.size
        return area

    def get_vertex(self):
        half_size = self.size / 2
        x1 = (self.x - half_size, self.y + half_size)
        x2 = (self.x + half_size, self.y + half_size)
        x3 = (self.x + half_size, self.y - half_size)
        x4 = (self.x - half_size, self.y - half_size)
        return (x1, x2, x3, x4)


class Triangle(Shape):
    def get_area(self):
        area = (math.sqrt(3) * (self.size * self.size)) / 4
        return area

    def get_vertex(self):
        R = self.size / math.sqrt(3)
        r = self.size / (math.sqrt(3) * 2)
        half_size = self.size / 2
        x1 = (self.x, self.y - R)
        x2 = (self.x - half_size, self.y - r)
        x3 = (self.x + half_size, self.y - r)
        return (x1, x2, x3)
