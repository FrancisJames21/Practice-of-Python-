from Vehicals.vehical import Vehical

class Car(Vehical):

    def __init__(self,fuel, color,Brand,no_of_wheels):

        print("vehical is a car ")

        super().__init__(fuel, color,Brand,no_of_wheels)

    def supercar(self):

        print(f"{self.Brand}is a super car ")

    def sell(self):# to print the child class sell first  // this called method over ridding 
        super().sell()# to print both parent class and child class sell
        print("sell them ")

 



