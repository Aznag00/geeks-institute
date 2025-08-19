# ------ Exercise 1
print(("Hello world\n" * 4))

# ------ Exercise 2
print((99**3)*8)

# ------ Exercise 3
name = input("please enter your name: ")
if name == "mehdi":
    print ("WOW, we both have the same name")
else :
    print (" You look great today" + name)
# ------ Exercise 4
height = int(input("please enter your height (cm) :"))
if height < 145 :
    print("You need to grow some more to ride")
else :
    print("You not tall enough o ride!")
# ------ Exercise 5
my_fav_numbers  = set([3 , 8 , 22 , 10])
my_fav_numbers.update([4, 75])
my_fav_numbers.pop()
print(my_fav_numbers)

friend_fav_numbers = {5, 1, 15, 20}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print (our_fav_numbers)
# ------ Exercise 6
#  is not possible because tuple is immutable

# ------ Exercise 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")

apple_count = 0
for fruit in basket:
    if fruit == "Apples":
       apple_count += 1
print(apple_count)
basket.clear()
print(basket)

# ------ Exercise 8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
  sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
finished_sandwiches = list()
for sandwich in sandwich_orders[:]:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)
    print("I made your " + sandwich)