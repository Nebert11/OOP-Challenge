# Pet Class
class Pet:
    def __init__ (self, name, hunger, energy, happiness, tricks):
        self.name = 5
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger -3)
        self.happiness = min(10, self.happiness +1)
        print(f"{self.name} finished eating")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} emjoyed playing!")
        else:
            print(f"{self.name} is tired.")
    
    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"Hunger {self.hunger}/10")
        print(f"Energy {self.energy}/10")
        print(f"Happiness {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {','. join(self.tricks)}")
            
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
