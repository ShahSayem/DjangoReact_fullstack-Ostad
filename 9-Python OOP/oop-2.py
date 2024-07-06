class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def addTrick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")

d.addTrick("Roll Over")
e.addTrick("Jumps")