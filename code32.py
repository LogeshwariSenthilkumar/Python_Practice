class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        return (l*b)


s1=rectangle()
print(s1.area())

