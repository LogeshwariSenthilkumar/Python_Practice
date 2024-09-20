class phone():
    chargertype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.chargertype)
samsung=phone("samsung","20000")
samsung.display()
redmi=phone("redmi","30000")
redmi.display()
