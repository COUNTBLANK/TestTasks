import math

import SquareCounter
import unittest

class TestSquareCounter(unittest.TestCase):

    def test_types(self):
        a = SquareCounter.Figure([1,2,3])
        b = SquareCounter.Figure([1, 2, 3, 5], 'Triangle')
        c = SquareCounter.Figure([1, 2, 3], 'Circle')
        d = SquareCounter.Figure([1])

        self.assertEqual(a.name,'Triangle')
        self.assertEqual(b.name, 'Triangle')
        self.assertEqual(c.name, 'Circle')
        self.assertEqual(d.name, 'Circle')

    def test_squares(self):
        a = SquareCounter.Figure([3,4,5])
        b = SquareCounter.Figure([5, 5, 3], 'Triangle')
        c = SquareCounter.Figure([1], 'Cirle')
        d = SquareCounter.Figure([3])

        self.assertEqual(a.calculate_square(), 6.0)
        self.assertEqual(b.calculate_square(), 7.1545440106270926)
        self.assertEqual(c.calculate_square(), math.pi)
        self.assertEqual(d.calculate_square(), math.pi*9)

    def test_execption(self):
        self.assertRaises(ValueError,SquareCounter.Figure,[-1])
        self.assertRaises(Exception,SquareCounter.Figure,[])
        self.assertRaises(ValueError, SquareCounter.Figure,['a'])
        self.assertRaises(ValueError, SquareCounter.Figure.calculate_square,SquareCounter.Figure([1,2,4]))