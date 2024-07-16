def main():
  string1 = "Hello There how are you"
  string2 = "AAAaaa"
  numA = count_a(string1)
  numA2 = count_a(string2)
  
  print(f"The number of a's in {string1} is {numA}")

  print(f"The number of a's in {string2} is {numA2}")



  string1 = "Hey"
  string2 = "Bye"

  print(same_length(string1, string2))



  nums = [4, 1, 3, 9, 8, 4, 6]

  evens = even_list(nums)

  print(evens)
  print(nums)

'''
Write a Python function called

count_a that takes a string as a parameter and returns the number of times the letter 'a' appears in the string.
'''
def count_a(string):
  countA = 0
  for character in string:
    if character.lower() == "a":
      countA += 1
  return countA

'''
Write a Python function called same_length that takes two strings as parameters and returns True if they have the same length.
'''
def same_length(str1, str2):
  if len(str1) == len(str2):
    return True
  else:
    return False



'''
Write a Python function called even_list that takes a list of integers as a parameter and returns a new list containing only the even numbers in the input list.

'''

def even_list(numList):
  evenNums = []

  for number in numList:
    if number % 2 == 0:
      evenNums.append(number)
  return evenNums


main()