class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  
    def add_animal(self, animal_type, count=1):
        """Add or update the animal count"""
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        """Return formatted farm info with animals and counts"""
        lines = [f"{self.name}'s farm\n"]
        for animal, count in self.animals.items():
            lines.append(f"{animal} : {count}")
        lines.append("\n    E-I-E-I-0!")
        return "\n".join(lines)

    def get_animal_types(self):
        """Return sorted list of animal types"""
        return sorted(self.animals.keys())

    def get_short_info(self):
        """Return a short sentence summary about the farm animals"""
        animal_list = self.get_animal_types()
        animals_str = []

        for animal in animal_list:
            if self.animals[animal] > 1:
                animals_str.append(animal + "s")
            else:
                animals_str.append(animal)

        if len(animals_str) > 1:
            short_info = ", ".join(animals_str[:-1]) + " and " + animals_str[-1]
        else:
            short_info = animals_str[0]

        return f"{self.name}'s farm has {short_info}."



macdonald = Farm("McDonald")

macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())