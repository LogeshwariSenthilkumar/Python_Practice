class a():
    def __init__(self):
        print("A")
    def display(self):
        print("a class")
class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("b class")

obj1=b()
