import math as geometric_area


def circle(radius):
    if type(radius) != float and type(radius) != int:
        raise TypeError('Not numeric input')
    if radius <= 0:
        raise ValueError('Not positive')
    return geometric_area.pi * radius * radius


def rectangle(length, width):
    if type(length) != float and type(length) != int and type(width) != float and type(width) != int:
        raise TypeError('Not numeric input')
    if length <= 0 or width <= 0:
        raise ValueError('Not positive')
    return length * width


def square(length):
    if type(length) != float and type(length) != int:
        raise TypeError('Not numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    return geometric_area.pow(length, 2)


def triangle(base, height):
    if type(base) != float and type(base) != int and type(height) != float and type(height) != int:
        raise TypeError('Not numeric input')
    if base <= 0 or height <= 0:
        raise ValueError('Not positive')
    return (base * height)/2

