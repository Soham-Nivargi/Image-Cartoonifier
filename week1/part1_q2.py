class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(self.name)
        print("woof woof")

my_dog = Dog("tommy", "labrador")
my_dog.bark()