class granddad():
    def money(self):
        print("Granddad's money")
class dad(granddad):
    def phone(self):
        print("Dad's phone")
class son(dad):
    def laptop(self):
        print("Son's laptop")


suresh=son()
suresh.money()
