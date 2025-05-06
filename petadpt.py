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
    "Lucky": ("playing", "Walk"),
    "Leo":("Sleeping", "Bones"),
    "Cat": ("Fish", "Yarn Ball")
}

print("******************* P E T S ***********************")
dog1 = Dog("Lucky",'10m','husky','Black n White')
dog2 = Dog("Leo",'15m','Pomeranian','brown')
cat1 = Cat("ash",'9m','persian','grey')

pet_shelter = {}

def gen_petid():
  return f"{random.randint(10,99)}"

def add_pet(pet):
  pet_id = gen_petid()
  while pet_id in pet_shelter:
    pet_id = generate_pet_id()
  pet_shelter[pet_id] = pet
  return pet_id

def adopt_pet(pet_id):
  return pet_shelter.pop(pet_id, None)

def display_pets():
  return {pid: pet.display_info() for pid, pet in pet_shelter.items()}

id1 = add_pet(dog1)
id2 = add_pet(dog2)
id3 = add_pet(cat1)

print("\nAvailable pets:")
for pid, info in display_pets().items():
  print(f"{pid}: {info}")

print("\nAdopting pet:", id1)
adopted = adopt_pet(id1)
if adopted:
  print("Adopted:", adopted.display_info())
else:
  print("Pet not found.")

print("\nRemaining pets:")
for pid, info in display_pets().items():
  print(f"{pid}: {info}")
