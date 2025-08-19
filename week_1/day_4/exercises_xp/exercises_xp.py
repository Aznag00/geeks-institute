# ------ Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

class Siamese (Cat):
    def sing(self, sound):
        return (f"{sound}")
    
bengal_instance = Bengal("Bengal", 2)
chartreux_instance = Chartreux('Chartreux', 3)
siamese_instance = Siamese('Siamese', 1)
all_cats = [bengal_instance, chartreux_instance, siamese_instance]
sara_pets = Pets(all_cats)
sara_pets.walk()
# ------ Exercise 2

class Dog :
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return (f'{self.name} is barking')
    def run_speed(self):
        return self.weight/self.age*10
    def fight(self, other_dog):
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight

        if my_score > other_score:
            return f"{self.name} wins the fight!"
        elif my_score < other_score:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"        
        
dog1 = Dog("red", 3, 15)
dog2 = Dog("max", 4, 17)
dog3 = Dog("rex", 5, 14)

print(dog1.fight(dog3))

# ------ Exercise 3

import random

# Assuming your previous Dog class looks like this:
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"


# New class
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *dog_names):
        names = ", ".join([dog.name for dog in dog_names])
        print(f"{self.name}, {names} all play together")
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

# ------ Exercise 4

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members  # list of dicts

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! The {self.last_name} family has a new child: {kwargs['name']}")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return None  # if not found

    def family_presentation(self):
        print(f"\nThe {self.last_name} family:")
        for member in self.members:
            print(member)


members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
smiths = Family("Smith", members)

smiths.born(name="Tommy", age=2, gender="Male", is_child=True)
print(smiths.is_18("Michael"))   # True
smiths.family_presentation()

# ------ Exercise 5

class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{member['name']}'s power is {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")
                return

    def incredible_presentation(self):
        print("\n✨ Here is our powerful family ✨")
        super().family_presentation()

incredible_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power':'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power':'read minds','incredible_name':'SuperWoman'}
]

inc_family = TheIncredibles("Incredibles", incredible_members)
inc_family.incredible_presentation()
inc_family.born(name="Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")
inc_family.incredible_presentation()
inc_family.use_power("Michael")


# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
