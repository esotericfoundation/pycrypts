import math


def get_line_circle_intersection(a, b, c, h, k, r):
    if a == 0:
        if b == 0:
            return None

        y = c/b

        try:
            x_1 = h + math.sqrt(-b * b * (b * b * (k * k - r * r) - 2 * b * c * k + c * c)) / b * b
            x_2 = h - math.sqrt(-b * b * (b * b * (k * k - r * r) - 2 * b * c * k + c * c)) / b * b
        except ValueError:
            return None

        return (x_1, y), (x_2, y)

    return None
