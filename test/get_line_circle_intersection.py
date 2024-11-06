import unittest

from util.get_line_circle_intersection import get_line_circle_intersection


class LineCircleIntersectionTest(unittest.TestCase):
    def test_algorithm_1(self):
        a, b, c = 1, 0, 1
        h, k, r = 1, 5, 1

        x_expected = 1
        y_1_expected = 6
        y_2_expected = 4

        solutions = get_line_circle_intersection(a, b, c, h, k, r)

        x = solutions[0][0]
        y_1 = solutions[0][1]
        y_2 = solutions[1][1]

        self.assertEqual(x, x_expected)
        self.assertEqual(y_1, y_1_expected)
        self.assertEqual(y_2, y_2_expected)

    def test_algorithm_2(self):
        a, b, c = 0, 1, 1
        h, k, r = 5, 1, 1

        y_expected = 1
        x_1_expected = 6
        x_2_expected = 4

        solutions = get_line_circle_intersection(a, b, c, h, k, r)

        y = solutions[0][1]
        x_1 = solutions[0][0]
        x_2 = solutions[1][0]

        self.assertEqual(y, y_expected)
        self.assertEqual(x_1, x_1_expected)
        self.assertEqual(x_2, x_2_expected)

    def test_algorithm_3(self):
        a, b, c = 0, 4.4, 6
        h, k, r = 5.4, 4.2, 4.6

        solutions = get_line_circle_intersection(a, b, c, h, k, r)

        self.assertEqual(solutions[0], (1.77853, 1.36364))
        self.assertEqual(solutions[1], (9.02147, 1.36364))
