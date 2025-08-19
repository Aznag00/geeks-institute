# ------ Challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

i = 1
result = []
while i <= length : 
    result.append(number * i)
    i += 1
print(result)

# ------ Challenge 2
string = ""
user_word = input("please enter a word: ")
for char in user_word :
    if not string or char != string[-1]:
        string += char
print(string)
