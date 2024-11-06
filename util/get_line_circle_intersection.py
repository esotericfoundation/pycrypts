import math


def get_line_circle_intersection(a, b, c, h, k, r):
    if a == 0 and b == 0:
        return None

    if b == 0:
        x = c/a

        try:
            y_1 = k + math.sqrt(-a * a * (a * a * (h * h - r * r) - 2 * a * c * h + c * c)) / a * a
            y_2 = k - math.sqrt(-a * a * (a * a * (h * h - r * r) - 2 * a * c * h + c * c)) / a * a
        except ValueError:
            return None

        return (x, y_1), (x, y_2)

    if a == 0:
        y = c/b

        try:
            x_1 = h + math.sqrt(-b * b * (b * b * (k * k - r * r) - 2 * b * c * k + c * c)) / b * b
            x_2 = h - math.sqrt(-b * b * (b * b * (k * k - r * r) - 2 * b * c * k + c * c)) / b * b
        except ValueError:
            return None

        return (x_1, y), (x_2, y)

    y = (1j * b * b * (h * h + k * k - r * r) + 2 * b * c * h - 1j * c * c)/(2 * b * (b * (h + 1j * k) - 1j * c))
    if y is complex:
        return None

    x = (c - b * y) / a
    return (x, y), (x, y)
