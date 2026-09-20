class Dog:
    species = "Canine"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def display(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Color:", self.color)


dog1 = Dog("German Shepherd", "Black and Brown")
dog2 = Dog("Labrador", "Golden")

print("Dog 1:")
dog1.display()

print("Dog 2:")
dog2.display()