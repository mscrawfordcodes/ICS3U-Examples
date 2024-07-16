word = "persnickety"
for letter in word:
  print(letter)

#print the number of characters in word
print(len(word))

#use index notation to access the first 4 characters in word, and concatenate them using +
print(word[0] + word[1] + word[2] + word[3])

#len(word)//2 will find the middle character in word
#print the start of the word to the middle character - basically prints the first half of the word
print(word[0:len(word)//2])

#print the last character of the word
print(word[-1])

#extended slicing example
#will reverse the entire word
#step of -1 indicates we start at the END of the word and STOP at the beginning
print(word[::-1])