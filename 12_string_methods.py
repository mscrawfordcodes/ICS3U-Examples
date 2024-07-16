word = "example"

wordUppercase = word.upper() #make a new string from word with all uppercase letters
print(wordUppercase)
print(word)

word2 = "TEST"

print(word2.lower()) #make a new string from word2 with all lowercase letters

print(word.title()) #capitalize every proper word in string

word3 = "harry potter"
print(word3.title())

firstName, lastName = word3.split() #split will store the first name in firstName variable, then last name in lastName variable

print("firstName", firstName)
print("lastName", lastName)

word4 = " testing    "
removeWhitespace = word4.strip() #remove beginning and end whitespace
print(len(removeWhitespace))

word3 = "harry potter"
print(word3.find("r")) # index of the first time r appears - index 2
print(word3.rfind("r")) #index of the last time r appears - index 11
print(word3.find("x")) #cannot find x, prints -1

print(word3.index("r")) #same behaviour as find method
#print(word3.index("x")) #produces a runtime error, NOT the same as find method

word3 = "harry potter"

print("count r", word3.count("r")) #counts the number of r in string

replaceR = word3.replace("r","R") #replace all lowercase r with uppercase R
print("Replace", replaceR)
print("original word", word3)

feelings = input("Enter how you feel about food: ")

happy = feelings.count("happy")
good = feelings.count("good")

print("Happy mentioned: ", happy)
print("Good mentioned: ", good)