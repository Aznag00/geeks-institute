import random
# ------ Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = zip(keys, values)
dictionary = dict(res)
print(dictionary)

# ------ Exercise 2
family = {}
num_members = int(input("How many family members do you want to add? "))
for _ in range(num_members):
    name = input("Enter name: ").strip()
    age = int(input(f"Enter age for {name}: "))
    family[name] = age
print(family)
def charges (ages) :
    cost = 0
    for age in ages.values():
        if age < 3 :
            cost += 0
        elif age in range(3 , 12) :
            cost += 10
        else :
            cost += 15
    return print(f"The totol cost for the fimily is {cost}$")
charges(family)

# ------ Exercise 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())
more_on_zara = {
   "creation_date": 1975,
   "number_stores": 10000
}
brand.update(more_on_zara)
print("Number of stores is:", brand["number_stores"])

# ------ Exercise 4
def describe_city(city, country= "Morocco"):
    print(f"{city} is in {country}")
describe_city("casablanca")
# ------ Exercise 5
def rend_func(rand_num):
    if rand_num not in range (1, 101):
        print("the number must be between 1 and 100")
    random_number = random.randint(1, 100)
    if rand_num == random_number:
                print(f" WOW! Both numbers are {rand_num}"
                )
    else:
        print(f"OOPS! your number is: {rand_num}, the random number is: {random_number}")

user_input = int(input("Enter a number between 1 and 100: "))
rend_func(user_input)


# ------ Exercise 6
def make_shirt(size = "large", text = "I love python"):
      print(f"The size of the shirt is {size} and the text is {text}")

make_shirt(size = "medium", text = "Geeks institute")
# ------ Exercise 7

def get_random_temp(season):
    if season == "winter":
        low, high = -10, 16
    elif season == "spring":
        low, high = 5, 23
    elif season == "summer":
        low, high = 16, 40
    elif season in ["autumn", "fall"]:
        low, high = 5, 25
    else:
        low, high = -10, 40
    return round(random.uniform(low, high), 1)
def main():
    month_number = int(input("enter the number of the mmonth: "))
    if month_number in [12, 1, 2] :
        season = "winter"
    elif month_number in [3,4,5] :
        season = "spring"
    elif month_number in [6,7,8] :
        season = "summer"
    elif month_number in [9,10,11] :
        season = "autumn"
    else:
        print("Invalid month. Using default season.")
    temperture = get_random_temp(season)

    print(f"The temperature right now is {temperture} degrees Celsius.")
    if temperture < 0 : 
        return print("`Brrr, that’s freezing! Wear some extra layers today")
    elif temperture in range(0, 17) :
        return print("Quite chilly! Don’t forget your coat")
    elif temperture in range(16, 24) :
        return print("What a nice wheather!")
    elif temperture in range(24, 33) :
        return print("it is getting hot!")
    elif temperture in range(32, 41) :
        return print("it is so hot!")
main()

# ------ Exercise 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def ask_question():
   correct_answer = 0
   wrong_answer = 0
   for element in data:
        user_answer = input(element["question"])
        if user_answer == element["answer"]:
           correct_answer += 1
        else :
           wrong_answer += 1
   return print(f"the worng answer are {wrong_answer}, and the correct answers are { correct_answer}")
       
ask_question()