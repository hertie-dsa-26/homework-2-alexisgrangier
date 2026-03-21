
import unittest
import math
from circle import Circle

class testCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(1)
        self.assertAlmostEqual(c.perimeter(), 2 * 3.14159, places = 4)
    
    def test_area(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), math.pi, places = 4)

if __name__ == "__main__":
    unittest.main()