from rectangel import Rectangel
class Square(Shape):

    def __init__(self,name,side):
        super().__init__(name)

        self.side = side

    def area (self):

        return self.side * self.side 