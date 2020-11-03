class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        string = " Name: %s;  Price: %.2f" %( self.getName(), self.getPrice())
        return string

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price