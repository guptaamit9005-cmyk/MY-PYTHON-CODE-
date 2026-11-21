class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    print('length',r.length)
    print('breadth',r.breadth)
    print('area',r.area())
    print('perimeter',r.perimeter())