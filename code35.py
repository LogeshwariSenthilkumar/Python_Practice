class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Dept:",self.dept)


e1=manager("Ram",15000,"IT")
e1.display()
