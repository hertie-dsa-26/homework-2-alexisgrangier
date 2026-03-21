
import unittest
from circle import Circle

class testCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(1)
        self.assertAlmostEqual(c.perimeter(), 2 * 3.14159, places = 4)
    
    def test_area(self):
        c = Cricle (1)
        self.assertAlmostEqual(c.area(), 3,14159, places = 4)

if __name__ = "__main__":
unittest.main()