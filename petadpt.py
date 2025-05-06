import random

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        return f"{self.name} {self.species}, Age: {self.age}"

class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        return f"{super().display_info()}, Breed: {self.breed}, Color: {self.color}"

class Cat(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        return f"{super().display_info()}, Breed: {self.breed}, Color: {self.color}"

pet_preferences = {
    "Dog": ("Bones", "Walk"),
    "Cat": ("Fish", "Nap")
}
pet_id = random.randint(10,99)
print("************ P E T S******************")
dog1 = Dog("Lucky",'10m','husky','Black n White')
dog1.display_info()