class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("Addition of two numbers is:",self.num1+self.num2)
    def sub(self):
        print("Subtraction of two numbers is:",self.num1-self.num2)
    def mul(self):
        print("Multiplication of two numbers is:",self.num1*self.num2)
    def div(self):
        print("Division of two numbers is:",self.num1/self.num2)


numbers=calculator(6,3)
numbers.add()
numbers.sub()
numbers.mul()
numbers.div()
