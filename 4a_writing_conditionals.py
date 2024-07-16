'''
Write a Python program that checks if a given number is positive or negative
'''

'''
num = int(input("Enter a number: "))

if num > 0:
  print("Positive number")
if num < 0:
  print("Negative number")
if num == 0:
  print("Number is 0")
'''


'''
Write a program that prompts the user for the weight (in lbs) of luggage. If weight is greater than 20, print: “There is a $25 surcharge for luggage that is too heavy.” If weight is smaller than 20, print: “Have a safe flight!” If weight is exactly 20, print: “That was close, the weight is just right!”
'''


'''
weight = int(input("Enter the weight of the luggage: "))

if weight > 20:
  print("There is a $25 surcharge for luggage that is too heavy.")

if weight < 20:
  print("Have a safe flight")

if weight == 20:
  print("That was close, the weight is just right!")
'''


'''
Write a Python program that checks if a given letter is a vowel or a consonant
'''

'''
letter = input("Enter a letter: ")

if letter in "aeiou" or letter in "AEIOU":
  print("Letter is a vowel")
else:
  print("Letter is a consonant")
'''


'''
weather = input ("What's the weather? ")

if weather == "snowing":
  print("Wear a coat")
elif weather == "raining":
  print("Bring an umbrella")
else:
  print("No umbrella or coat")

'''


'''
num = int(input("Enter a number: "))

if num < 0:
  print("Number is negative")
elif num > 0:
  print("Number is positive")
else: # number = 0
  print("Number is 0")
'''
'''

weight = int(input("Enter the weight of the luggage: "))

if weight > 20:
  print("There is a $25 surcharge for luggage that is too heavy.")
elif weight < 20:
  print("Have a safe flight")
else: # weight is equal to the maximum amount
  print("That was close, the weight is just right!")
'''

'''
Write a program that prompts the user to enter a type of pet. If the user enters “cat”, print “Meow!”. If the user enters “dog”, print “Woof!”. If the user enters “bird”, print “Squawk!’. If the user enters anything else, print “I don’t know what sound that animal makes”.

'''

'''
pet = input("Enter your pet species: ")

if pet == "dog":
  print("Woof")
elif pet == "cat":
  print("Meow")
elif pet == "bird":
  print("Squawk!")
else:
  print("I don’t know what sound that animal makes")
'''


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