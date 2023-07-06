from shape import Shape

class Rectangel(Square):

    def __init__(self,name,x,y):
        super().__init__(name,side)

        self.x=x
        self.y=y
    
    def area(self):
        return self.x * self.y
