word = "example"

print(word[0])
print(word[1])

print(word[0]+word[1])

word2 = "Hello World!"
print(word2[2:6])

print(word2[2:]) # start at index 2, go until end of string
print(word2[:6]) #start at beginning of string, go until index 6

word3 = "2test"

print(word2[-1])
print(word3[-1])

print(word3[0])
print(word3[-5]) #5th last character of the string... is also the first character of the string


word2 = "Hello World!"
print(word2[3::2]) #start at index 3 and step by 2

print(word2[::-1]) #step of -1 indicates we START at the END of the string, and go to the BEGINNING - reversing the string

palindrome = input("Enter a word: ")

if palindrome == palindrome[::-1]:
  print("Word is a palindrome")
else:
  print("Word is not a palindrome")