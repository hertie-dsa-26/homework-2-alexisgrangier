import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        """
        Performs:
        From the value of the radius, calculates the perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        Performs: from the value of the radius, calculates the area of the cicle.
        """
        return math.pi * (self.radius ** 2)
