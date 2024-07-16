'''
1. Write a Python program that checks if a given number is positive or negative

2. Write a program that prompts the user for the weight (in lbs) of luggage. If weight is greater than 20, print: “There is a $25 surcharge for luggage that is too heavy.” If weight is smaller than 20, print: “Have a safe flight!” If weight is exactly 20, print: “That was close, the weight is just right!”

3. Write a program that tests whether an integer is odd or even using the modulo operator.

4. Write a Python program that checks if a given letter is a vowel or a consonant

'''

number = int(input("Enter a number: "))
if number > 0: #number is positive
  print("the number is positive")
else:
  print("the number is negative")



weight = int(input("Enter the weight of the luggage: "))

if weight > 20:
  print("There is a $25 surcharge for luggage that is too heavy.")
if weight < 20:
  print("Have a safe flight!")
if weight == 20:
  print("That was close, the weight is just right!")

  
number = int(input("Enter a number: "))
remainder = number % 2
if remainder == 0:
  print("the number is even")
else:
  print("the number is odd")


letter = input("Enter a letter: ")
vowels = "aeiou"
vowelsAllCaps = "AEIOU"

if letter in vowels or letter in vowelsAllCaps:
  print("vowel")
else:
  print("consonant")