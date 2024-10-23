class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.availability = True 

    def isAvailable(self, is_available):
        self.availability = is_available

    def Display(self):
        pass


class Mammal(Animal):
    def __init__(self, name, age, habitat, furLen, diet):
        super().__init__(name, age, habitat)
        self.furLen = furLen
        self.diet = diet

    def Display(self):
        print(f"Mammal Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Habitat: {self.habitat}")
        print(f"Fur Length: {self.furLen}")
        print(f"Diet Type: {self.diet}")
        print(f"Availability: {self.availability}\n")
    
    def Update(self, flag):
        self.availability = flag


class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flightAltitude):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flightAltitude = flightAltitude

    def Display(self):
        print(f"Bird Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Habitat: {self.habitat}")
        print(f"Wingspan: {self.wingspan}")
        print(f"Flight Altitude: {self.flightAltitude}")
        print(f"Availability: {self.availability}\n")

    def Update(self, flag):
        self.availability = flag


class Reptile(Animal):
    def __init__(self, name, age, habitat, scalePattern, isVenomous):
        super().__init__(name, age, habitat)
        self.scalePattern = scalePattern
        self.isVenomous = isVenomous

    def Display(self):
        venom = "Venomous" if self.isVenomous else "Non-Venomous"
        print(f"Reptile Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Habitat: {self.habitat}")
        print(f"Scale Pattern: {self.scalePattern}")
        print(f"Venom Status: {venom}")
        print(f"Availability: {self.availability}\n")
    
    def Update(self, flag):
        self.availability = flag


#Driver Code

dolphin = Mammal(name="Dolphin", age=11, habitat="Pacific Ocean", furLen="Medium", diet="Carnivore")
hawk = Bird(name="Hawk", age=7, habitat="Mountains", wingspan="3m", flightAltitude="3000m")
snake = Reptile(name="Snake", age=2, habitat="Desert", scalePattern="Striped", isVenomous=True)

dolphin.Display()
hawk.Display()
snake.Display()

dolphin.Update(False)
hawk.Update(True)
snake.Update(False)

print("------------------After updating------------------\n")
dolphin.Display()
hawk.Display()
snake.Display()
