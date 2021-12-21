

from task_classes import Circle, Shape, Square, Triangle
import math
import unittest


class TestTask4(unittest.TestCase):
    def test_position_initial_value(self):
        c = Circle()
        self.assertEqual(c.get_center(), (0, 0), "Should be (0, 0)")

    def test_position_value(self):
        t = Triangle(5, 5, 2)
        self.assertEqual(t.get_center(), (5, 5), "Should be (5, 5)")

    def test_initial_size_value(self):
        c = Circle()
        self.assertEqual(c.size, 1, "Should be 1")

    def test_move(self):
        c = Circle()
        c.move(2, 2)
        self.assertEqual(c.get_center(), (2, 2), "Should be (2, 2)")

    def test_distance(self):
        c = Circle()
        t = Triangle(10, 10, 1)
        self.assertEqual(Shape.get_distance(
            c, t), math.sqrt(200), "Should be 10")

    def test_circle_area(self):
        c = Circle()
        self.assertEqual(c.get_area(), math.pi, "Should be %s" % math.pi)

    def test_square_area(self):
        s = Square(1, 1, 2)
        self.assertEqual(s.get_area(), 4, "Should be 4")

    def test_square_points(self):
        s = Square(0, 0, 2)
        self.assertEqual(s.get_vertex(), ((-1, 1), (1, 1), (1, -1),
                         (-1, -1)), "Should be (-1,1), (1,1), (1,-1), (-1,-1)")


suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)