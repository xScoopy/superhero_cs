class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def drink(self):
        print(f"{self.name} is drinking")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")

dog = Animal("Rufus")
frog = Frog("Frogger")

dog.eat()
dog.drink()
frog.eat()
frog.drink()
frog.jump()
dog.jump()