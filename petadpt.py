import random
class Pet:
    def __init__(self,name,species,age):
        self.name = name
        self.species=species
        self.age=age
    def display(self):
        return f"Name - {self.name}  Species - {self.species}  Age - {self.age}"
    
class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color
    def display(self):
        base= super().display()
        return f"{base} Breed - {self.breed}  Color - {self.color}"
    
class Cat(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.color = color
    def display(self):
        base= super().display()
        return f"{base} Breed - {self.breed}  Color - {self.color}"
    
class PetAdpot():
    def __init__(self):
        self.pets = {}
        
    def addpet(self,pet):
        while True:
            petid= random.randint(100,999)
            if petid not in self.pets:
                break
        self.pets[petid]=pet
        return petid
    def view_pets(self):
        if not self.pets:
            print("No pets available")
            return
        print(" ===+PETS AVAILABLE+=== ")
        for petid,pet in self.pets.items():
            print(f"ID: {petid} - {pet.display()}")
    def adopt_pet(self,petid):
        if petid in self.pets:
            adpt = self.pets.pop(petid)
            print(f"Congratulations! You have adopted a pet - {adpt.name}")
            return adpt
        else:
            print("Invalid Pet ID. Please try again")
            return None

def main():
    system = PetAdpot()
    
    system.addpet(Dog("Lucky",3,"Golden retriever","Golden"))
    system.addpet(Dog("Yeontan",2,"Pomeranian","Biscuit"))
    system.addpet(Cat("Ash",3,"Persian","Grey"))
    system.addpet(Cat("Bella",1,"Siamese","White"))

    print("/^^^\\======PRETTY PAWS=======/^^^\\")
    print("Welcome to our Pet shop ")
    while True:
        print("- - - MENU - - -")
        print("1 - View available pets ")
        print("2 - Adopt a pet")
        print("3 - Add a pet ")
        print("4 - Exit ")
        
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            system.view_pets()
        elif choice == 2:
            system.view_pets()
            if system.pets:
                try:
                    id=int(input("Enter the PetId of the pet you want to adopt: "))
                    system.adopt_pet(id)
                except ValueError:
                    print("Enter a valid Id")
            
            
            
        elif choice == 3:
            pet_type=input("Enter the Pet type (Dog/Cat)").capitalize()
            if pet_type not in ["Dog","Cat"]:
                print("Enter a valid Pet type - \"Dog\" or \"Cat\" ")
                continue
            name = input("Enter name of the pet: ").capitalize()
            try:
                age = int(input("Enter the age of the pet: "))
            except ValueError:
                print("Enter valid age")
                continue
            breed = input(f"Enter the breed of {pet_type}: ")
            color = input(f"Enter the color of {pet_type}: ")
            if pet_type == "Dog":
                new_pet=Dog(name,age,breed,color)
            else:
                new_pet = Cat(name,age,breed,color)
            petid = system.addpet(new_pet)
            print(f"{pet_type} added with pet id - {petid}")
            
        elif choice == 4:
            print("Thanks for using our system!")
            break

        else:
            print("Invalid choise. Enter a valid option")           
            
# if __name__ == "__main__":
main()
        
            
                 
        
