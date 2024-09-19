class teacher:
    def __init__(self,nam,reg):
        self.name=nam
        self.regno=reg
    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)
t1=teacher("Chitra",1)
t2=teacher("Senthil Kumar",2)
t1.display()
t2.display()
