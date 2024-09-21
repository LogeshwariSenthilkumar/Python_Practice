class pen:
    def __init__(self,color,price):
        self.color=color
        self.price=price
    def display(self):
        print("Color:",self.color)
        print("Price:",self.price)
p1=pen("red","10")
p1.display()

p2=pen("blue","30")
p2.display()
