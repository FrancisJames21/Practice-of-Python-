
""" 
here we explain all the principle of oops 

inheritance

encapsulation

abstraction

"""

"""

class Bank:

    def __init__(self,name):

        self.name = name 
        self._amount = 0

    def add_amount(self,x):
        self._amount += x

    def get_amount(self):
        return self._amount

class HDFC(Bank):

    def __init__(self):

        name = "HDFC"
        super().__init__(name)

if __name__ == "__main__":

    bank = HDFC()

    bank.add_amount(100)
    print(bank.get_amount())  """


"""
Polymorphism
"""
"""
class Shape:

    def __init__(self, name):

        self.name = name 


class Square(Shape):

    def __init__(self,name,side):
        super().__init__(name)

        self.side = side

    def area (self):

        return self.side * self.side 


class Rectangel(Shape):

    def __init__(self,name,x,y):
        super().__init__(name)

        self.x=x
        self.y=y
    
    def area(self):
        return self.x * self.y

if __name__ == "__main__":

    square = Square("Square", 6)

    print(square.name)

    print(square.area())

    rectangel= Rectangel("Rectangel",3,5)

    print(rectangel.name)

    print(rectangel.area())"""



# another examplain of abstraction 

class Payment:

    def __init__(self,amount):

        self.amount = amount

    def make_payment(self):
        print("initiating payment")
        self.pay()
    
    def pay(self):
        print("default payment")


class COD(Payment):

    def __init__(self,amount):
        super().__init__(amount)

    def pay(self):
        print("paying from cod")

class CreditCard(Payment):

    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):

        print("paying from CC")


if __name__ == "__main__":

    cod = COD (100)
    cod.make_payment()



 






