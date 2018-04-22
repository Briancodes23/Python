# Describes a shape
class Square(object):
    def __init __(self,i):
    self.length = i
# Defining Area function
    def Area(self):
        return self.length**2

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h
    def Area(self):
        return 0.5 * self.base * self.height