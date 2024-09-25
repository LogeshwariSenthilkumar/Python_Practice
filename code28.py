class dad():
    def money(self):
        print("Dad's money")
class land():
    def landspace(self):
        print("Land")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass


s1=son1()
s1.landspace()
s1.money()
