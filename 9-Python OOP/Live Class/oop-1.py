class Maths:
    #Constructor
    def __init__(self, s):
        self.name = s
        print(self.name, "From constructor.....")
    
    s = "I am from Maths Class"
    
    def sub(self, x, y):
        return x-y
    
    def add(self, x, y):
        return x+y
    
    def printAdd(self):
        print("Added val: ", self.add(3, 5))


obj = Maths("Shah_Sayem")
obj2 = Maths("Shah_Sayem 2")

print(obj.add(3, 4))
print(obj.sub(3, 4))
print(obj.s)


print(obj.add(10, 4))
print(obj.sub(10, 4))
obj.printAdd()



