class Vehical:

    def __init__(self, fuel, color,Brand,no_of_wheels):

        print("life is good")

        self.fuel = fuel
        self.color = color
        self.Brand = Brand
        self.no_of_wheels = no_of_wheels


    def Run(self):
        
        print(f"it can move from one place to another by {self.fuel}")

    def Buy(self):

        print("we can buy them from showroom or a person")

    def sell(self):
        print("sell them according to you")
        
