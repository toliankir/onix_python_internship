

from task_classes import Circle, Shape, Square, Triangle
import math
import unittest


class TestSum(unittest.TestCase):
    def position_initial_value(self):
        c = Circle()
        self.assertEqual(c.get_center(), (0, 0), "Should be (0, 0)")

    # def position_value_test(self):
    #     t = Triangle(5, 5, 2)
    #     self.assertEqual(t.get_center(), (5, 5), "Should be (5, 5)")

    # def initial_size_value(self):
    #     c = Circle()
    #     self.assertEqual(c.size(), 1, "Should be 1")

    # def move_test(self):
    #     c = Circle()
    #     c.move(2, 2)
    #     self.assertEqual(c.get_center(), (2, 2), "Should be (2, 2)")

    # def distance_test(self):
    #     c = Circle()
    #     t = Triangle(10, 10, 1)
    #     self.assertEqual(Shape.get_distance(
    #         c, t), 10, "Should be 10")

    # def circle_area_test(self):
    #     c = Circle()
    #     self.assertEqual(c.get_area(), math.pi, "Should be %s" % math.pi)

    # def square_area_test(self):
    #     s = Square(1, 1, 2)
    #     self.assertEqual(s.get_area(), 4, "Should be 4")

    # def square_points_test(self):
    #     s = Square(0, 0, 2)
    #     self.assertEqual(self.s.get_vertex(), ((-1, 1), (1, 1), (1, -1),
    #                      (-1, -1)), "Should be (-1,1), (1,1), (1,-1), (-1,-1)")


# if __name__ == '__main__':
unittest.main()
