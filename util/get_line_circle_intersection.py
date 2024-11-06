import math


def get_line_circle_intersection(a, b, c, h, k, r):
    if a == 0 and b == 0:
        return None

    if b == 0:
        x = c/a

        try:
            y_1 = k + math.sqrt(-h * h + 2 * h * x + r * r - x * x)
            y_2 = k - math.sqrt(-h * h + 2 * h * x + r * r - x * x)
        except ValueError:
            return None

        return (x, y_1), (x, y_2)

    if a == 0:
        y = c/b

        try:
            x_1 = h + math.sqrt(-k * k + 2 * k * y + r * r - y * y)
            x_2 = h - math.sqrt(-k * k + 2 * k * y + r * r - y * y)
        except ValueError:
            return None

        return (x_1, y), (x_2, y)
