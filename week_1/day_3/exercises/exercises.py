# ------ Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("tom",3)
cat2 = Cat("white",5)
cat3 = Cat("black",7)

def old_cat(*arg):
    return max(arg, key=lambda c: c.age,  )
    
oldest = old_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

# ------ Exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
            print(f"{self.name} goes woof!")
    def jump(self):
            print(f"{self.name} jumps {self.height*2} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog name: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog name: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}")
else:
    print("Both dogs are the same height.")

# ------ Exercise 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])
stairway.sing_me_a_song()

# ------ Exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("the animals already exist !")
        self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name} Zoo are: ")
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold not in self.animals:
            print("this animal does not exist")
        else :
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = animal 
            else:
                if isinstance(grouped[first_letter], list):
                    grouped[first_letter].append(animal)
                else:
                    grouped[first_letter] = [grouped[first_letter], animal]
        self.groups = grouped
        return grouped
    def get_groups(self):
        if not self.groups:
            print("No groups found. Please run sort_animals() first.")
            return
        print("\nAnimal Groups:")
        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")

new_york_zoo = Zoo("New York")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")
new_york_zoo.sell_animal("Bear")

new_york_zoo.get_animals()
print("\nSorted & Grouped Animals:", new_york_zoo.sort_animals())
new_york_zoo.get_groups()

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
