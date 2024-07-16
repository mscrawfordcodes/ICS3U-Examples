countdown = 10

while countdown > 0:
  print(countdown)
  countdown -= 1 # subtract 1 from countdown
  #subtracting will happen continously until the loop condition becomes False

print("Blast Off!")


'''
1. Write a program that prints the numbers 1 - 10, using a while loop.

 
 2. Write a program that prompts a user to enter a number. The program should continuously add all the numbers entered until 0 is entered. At the end of the program, print the total of the numbers.
    a.    Modify the program to also print the average of the numbers entered


3. Write a program that prompts a user to enter a password. The user has a maximum of three attempts. If the user enters the correct password before they run out of guesses, print an appropriate message. If the user runs out of attempts, print an appropriate message.
'''



'''   #1   '''
number = 1

while number <= 10:
  print(number)
  number += 1


'''     #2     '''

num = int(input("Enter a number: "))
total = 0

while num != 0:
  total = total + num
  num = int(input("Enter a number: "))
print(total)


'''     #3     '''

password = "ICS3U"
guesses = 0

while guesses < 3: #user has max 3 attempts to enter correct password
  userPassword = input("Enter a password: ")
  guesses += 1
  if userPassword == password: #user guessed the corrected password
    print("Signed in")
    break
  else: #password entered isn't correct
    print(f"Incorrect! You have {3-guesses} attempt(s) remaining.")