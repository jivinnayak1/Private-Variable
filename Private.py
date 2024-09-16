class Car:
    def __init__(self, Price, Engine, Colour):
        self.__Price = Price
        self.Engine = Engine
        self.Colour = Colour

BMW = Car(6000000,"Inline 6","Blue")
Toyota = Car(30000000,"V8","Grey")
Tata = Car(2500000,"Electric","Light Blue")
Honda = Car(2000000,"i-VTEC","Brown")
Buggati = Car(500000000,"W 16","Black")

print(BMW.Price)

