class Animal:
    def __init__(self, name):
        self.name = name

    def go(self):
        print(f"{self.name} is going!")

    def eat(self):
        print(f"{self.name} is eating!")

        #Inheritance
class Reptile(Animal):
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print(f"{self.name} is crawling!")

        #Inheritance
class Crocodile(Reptile):
    pass

        #Inheritance
class Snake(Reptile):
    animalType = "Snake"

    def eat(self):
        print("I prefer bite instead of eat!!!")

a1 = Snake("Russel Viper")     
a1.go()
a1.eat() 
a1.crawl()  
print(a1.animalType)

c1 = Crocodile("Henry")
c1.eat()

