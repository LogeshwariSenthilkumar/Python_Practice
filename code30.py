class a():
    def __init__(self):
        print("A")
    def display(self):
        print("a class")
class b():
    def __init__(self):
        print("B")
    def display(self):
        print("b class")
class c(a,b):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("c class")



obj1=c()
