import unittest
from joaquin_gonzalez import *


class MyTestCase(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square(10), 100)
        self.assertAlmostEqual(square(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square('0.1')

        with self.assertRaises(ValueError):
            square(0)
            square(-4)

    def test_rectangle_area(self):
        self.assertEqual(rectangle(2, 3), 6)
        self.assertAlmostEqual(rectangle(2, 3.25), 6.50, delta=0.001)
        self.assertAlmostEqual(rectangle(2.25, 3.), 6.75, delta=0.001)
        self.assertAlmostEqual(rectangle(0.1, 0.2), 0.02, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle(1, '0.1')
            rectangle('0.1', 1)
            rectangle('1', '0.1')

        with self.assertRaises(ValueError):
            rectangle(0, 2.5)
            rectangle(2, 0)
            rectangle(0, 0)
            rectangle(-4, 4)
            rectangle(4, -4.2)
            rectangle(-4, -4)

    def test_circle_area(self):
        self.assertAlmostEqual(circle(3.2), 32.17, delta=0.001)
        self.assertAlmostEqual(circle(4), 50.2655, delta=0.001)

        with self.assertRaises(TypeError):
            circle('0.1')

        with self.assertRaises(ValueError):
            circle(0)
            circle(-1)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle(2, 3), 3, delta=0.001)
        self.assertAlmostEqual(triangle(2, 3.25), 3.25, delta=0.001)
        self.assertAlmostEqual(triangle(2.25, 3.), 3.375, delta=0.001)
        self.assertAlmostEqual(triangle(2.25, 3.25), 3.65625, delta=0.001)

        with self.assertRaises(TypeError):
            triangle(1, '0.1')
            triangle('0.1', 1)
            triangle('1', '0.1')

        with self.assertRaises(ValueError):
            triangle(0, 2.5)
            triangle(2, 0)
            triangle(0, 0)
            triangle(-4, 4)
            triangle(4, -4.2)
            triangle(-4, -4)


if __name__ == '__main__':
    unittest.main()
