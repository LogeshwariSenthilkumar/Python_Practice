class vehicle():
    def start(self):
        print("Vehicle started")
class car(vehicle):
    def start(self):
        print("Car started")



v1=car()
v1.start()
