class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish:
    def swim(self):
        print("swim")

        
cat = Mammal()
print(isinstance(cat, object))
print(issubclass(Mammal, Animal))

      
