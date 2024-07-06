class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def updateOdometer(self, om):
        if (om > self.odometer):
            self.odometer = om
        else:
            print("Can not update odometer at a lower value!")

    def __str__(self):
        return "This car is {} {} and year: {}".format(self.make, self.model, self.year)

    def __eq__(self, value):
        return (self.make == value.make and self.model == value.model and self.year == self.year)
    

c1 = Car("Toyota", "Camry", 2023)
c2 = Car("Subaru", "Forester", 2020)

print(c1.make, c1.model, c1.year)
print(c2.make, c2.model, c2.year)

print(c1)

c2.updateOdometer(50)
print(c2.odometer)

c2.updateOdometer(30)
print(c2.odometer)

if (c1 == c2):
    print("Both cars are same")
else:
    print("Both cars not are same")