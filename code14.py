class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("RAM:",self.ram)
        print("Processor:",self.processor)

hp=laptop()
hp.ram="8GB"
hp.processor="i5"
hp.display()
