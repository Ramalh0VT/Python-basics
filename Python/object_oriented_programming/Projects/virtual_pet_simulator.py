class Pet:
    def __init__(self, hunger=50, hygiene=50, happiness=50, health=50):
        # 1. Define limits first
        self.min_value = 0
        self.max_value = 100
        
        # 2. Assign values (This triggers the setters below automatically)
        self.hunger = hunger
        self.hygiene = hygiene
        self.happiness = happiness
        self.health = health

    def _clamp(self, value):
        return max(self.min_value, min(value, self.max_value))

    # --- Hunger ---
    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        self._hunger = self._clamp(value)

    # --- Hygiene ---
    @property
    def hygiene(self):
        return self._hygiene

    @hygiene.setter
    def hygiene(self, value):
        self._hygiene = self._clamp(value)

    # --- Happiness ---
    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        self._happiness = self._clamp(value)

    # --- Health ---
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = self._clamp(value)

    # --- Actions ---
    def feed(self):
        # These += operations automatically trigger the setters and clamping
        self.hunger += 20
        self.health += 5
        print(f"Fed the pet! Hunger is now {self.hunger} and Health is {self.health}.")

    def play(self):
        self.hunger -= 10
        self.happiness += 20
        print(f"Played with pet! Happiness is {self.happiness}, Hunger is {self.hunger}")

    def get_status(self):
        # We create the dictionary here so it captures the LATEST values
        current_values = {
            "Hunger": self.hunger,
            "Hygiene": self.hygiene,
            "Happiness": self.happiness,
            "Health": self.health,
        }
        
        print("\nThese are the current status of the pet's feelings:")
        for name, value in current_values.items():
            print(f"{name}: {value}")

# --- Execution ---
my_pet = Pet()
my_pet.get_status() # Check initial values

print("\n--- Feeding ---")
my_pet.feed()       # Should increase hunger/health (clamped at 100)

print("\n--- Overfeeding to test limits ---")
my_pet.feed()
my_pet.feed()       # Even if we feed too much, it won't pass 100
my_pet.get_status()