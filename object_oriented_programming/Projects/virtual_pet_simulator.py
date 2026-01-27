import json
import os

class Pet:
    def __init__(self, energy=50, hygiene=50, happiness=50, health=50):
        self.min_value = 0
        self.max_value = 100
        
        self.energy = energy 
        self.hygiene = hygiene
        self.happiness = happiness
        self.health = health

    def _clamp(self, value):
        return max(self.min_value, min(value, self.max_value))

   
    @property
    def energy(self): return self._energy
    @energy.setter
    def energy(self, value): self._energy = self._clamp(value)

    @property
    def hygiene(self): return self._hygiene
    @hygiene.setter
    def hygiene(self, value): self._hygiene = self._clamp(value)

    @property
    def happiness(self): return self._happiness
    @happiness.setter
    def happiness(self, value): self._happiness = self._clamp(value)

    @property
    def health(self): return self._health
    @health.setter
    def health(self, value): self._health = self._clamp(value)

    # --- Actions ---
    def feed(self):
        self.energy += 20 
        self.health += 5
        print("Fed the pet! Energy increased.")

    def play(self):
        self.energy -= 10 
        self.happiness += 20
        print("Played with pet!")

    def bath(self):
        self.hygiene += 40
        print("Gave a bath!")

    def pass_time(self):
        self.energy -= 10
        self.hygiene -= 5
        self.happiness -= 5

    
    def __str__(self):
        return f"[{self.__class__.__name__}] Energy: {self.energy} | Hygiene: {self.hygiene} | Happiness: {self.happiness} | Health: {self.health}"

class Cat(Pet):
    def bath(self):
        super().bath()
        self.happiness -= 50
        print("The cat scratched you and is now very grumpy!")

class Dog(Pet):
    def play(self):
        super().play()
        self.happiness += 40
        self.hygiene -= 20
        print("Dog is happy but muddy!")

# --- SAVE & LOAD FUNCTIONS ---

def save_pet(pet):
    data = {
        "type": pet.__class__.__name__,
        "energy": pet.energy,
        "hygiene": pet.hygiene,
        "happiness": pet.happiness,
        "health": pet.health
    }
    with open("savegame.json", "w") as f:
        json.dump(data, f)
    print("--- Game Saved Successfully! ---")

def load_pet():
    try:
        with open("savegame.json", "r") as f:
            data = json.load(f)
        pet_type = data["type"]
        if pet_type == "Cat":
            return Cat(energy=data["energy"], hygiene=data["hygiene"], happiness=data["happiness"], health=data["health"])
        elif pet_type == "Dog":
            return Dog(energy=data["energy"], hygiene=data["hygiene"], happiness=data["happiness"], health=data["health"])
        return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# --- MAIN EXECUTION ---

def main():
    pass_time_counter = 0
    print("Welcome to Python Pets!")
    current_pet = None

    if os.path.exists("savegame.json"):
        choice = input("Found a saved game! Do you want to load it? (yes/no): ").lower()
        if choice == "yes":
            current_pet = load_pet()

    if current_pet is None:
        print("\nStarting a New Game...")
        while True:
            choice = input("Do you want a Cat or a Dog? ").strip().lower()
            if choice == "dog":
                current_pet = Dog()
                break
            elif choice == "cat":
                current_pet = Cat()
                break
            else:
                print("Invalid Option")

    while True:
         
        print(f"\n{current_pet}")
        
        action = input("Action (feed, play, bath, save, quit): ").lower()
        pass_time_counter += 1
        if pass_time_counter % 2 == 0:
            current_pet.pass_time()
        
        if action == "feed":
            current_pet.feed()
        elif action == "play":
            current_pet.play()
        elif action == "bath":
            current_pet.bath()
        elif action == "save":
            save_pet(current_pet)
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()