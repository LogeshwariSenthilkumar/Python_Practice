class fruit():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print("Name:",self.name)
        print("price:",self.price)
apple=fruit("apple","100")
apple.display()

orange=fruit("orange","200")
orange.display()
