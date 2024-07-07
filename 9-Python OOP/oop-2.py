class Dog:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.tricks = []

    #Method
    def addTrick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")

d.addTrick("Roll Over")
print(d.name, d.tricks)

e.addTrick("Jumps")
print(e.name, e.tricks)
