# CREATE A CLASS CIRCLE THAT TAKES THE VALUE OF A RADIUS AND 
# RETURN THE AREA OF A CIRCLE

import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius


    def calc_radius(self):
        area = math.pi * (self.radius)**2
        return area

   

circle = Circle(8)
print(circle.calc_radius())
