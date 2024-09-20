class laptop():
    chargertype="B-type"
    @classmethod
    def changechargertype(cls):
        cls.chargertype="C-type"
        print("B-C changed")


laptop.changechargertype()
