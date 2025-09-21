class Car:
    def _init_(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(self.color, self.brand)

c1 = Car("Tesla", "Red")
c1.show()