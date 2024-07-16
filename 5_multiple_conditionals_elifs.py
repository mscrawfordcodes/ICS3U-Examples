raining = False
cold = False

if cold == True and raining == True:
  print("I need a coat and umbrella") 
elif cold == True:
  print("I need a coat")
elif raining == True:
  print("I need an umbrella")
else:
  print("I do not need a coat or umbrella")


num = int(input("enter a number: "))
if num > 0:
  print("positive")
elif num < 0:
  print("negative")
else:
  print("the number is 0")


'''
1. Rewrite the luggage practice problem to use if-elif-else instead of individual if statements:
Write a program that prompts the user for the weight (in lbs) of luggage. If weight is greater than 20, print: “There is a $25 surcharge for luggage that is too heavy.” If weight is smaller than 20, print: “Have a safe flight!” If weight is exactly 20, print: “That was close, the weight is just right!”

2. Write a program that prompts the user to enter a type of pet. If the user enters “cat”, print “Meow!”. If the user enters “dog”, print “Woof!”. If the user enters “bird”, print “Squawk!’. If the user enters anything else, print “I don’t know what sound that animal makes”.

'''


weight = int(input("Enter the weight of the luggage: "))

if weight == 20:
  print("That was close, the weight is just right!")
elif weight < 20:
  print("Have a safe flight!")
else: #weight > 20
  print("There is a $25 surcharge for luggage that is too heavy.")


pet = input("Enter the type of pet: ")

if pet == "cat":
  print("Meow")
elif pet == "dog":
  print("Woof")
elif pet == "bird":
  print("Squawk")
else:
  print("I don't know what sound that pet makes")




'''
Write a program that accepts 5 grade averages. The program should keep a count of how many honor students (>= 80%) are entered.
'''

grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))
grade3 = int(input("Enter grade 3: "))
grade4 = int(input("Enter grade 4: "))
grade5 = int(input("Enter grade 5: "))

honors = 0

if grade1 >= 80:
  honors = honors + 1
if grade2 >= 80:
  honors = honors + 1
if grade3 >= 80:
  honors = honors + 1
if grade4 >= 80:
  honors = honors + 1
if grade5 >= 80:
  honors = honors + 1

print(f"There are {honors} honors students")