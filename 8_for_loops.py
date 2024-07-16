num = int(input("Enter a number: "))

'''
Since the user can enter in any number, it is very difficult to write
a program that would be able to handle counting backwards from the number entered.
For example, if the user entered 5, it is tempting to write the following:
print(num)
print(num-1)
print(num-2)
print(num-3)
and so on...

But of course the user could enter 6, or 10, or 1000000000....

This is where a LOOP comes in handy and is another example of
ABSTRACTION (solving lots of problems of a similar type) in computer science.

We want our code to be able to count backwards, down to 1, REGARDLESS of the number entered.
'''

print("Example 1")
for i in range(num): #first example of a for loop, which will count up to num-1
    print(num-i) #continuously subtract i from num


#more examples
print("Example 2")
for i in range(5): #will STOP at 5, but won't print out 5
    print(i) #notice that numbers 0-4 are printed out

print("Example 3")
for i in range(1, 5): #start at 1 (initial value of i is 1), stop at 5
    print(i)

#another example of counting backwards, using the step value
print("Example 4")
for i in range(num, 0, -1): #start at value of num, count BACKWARDS by 1 (step value -1) and stop at 0
    print(i)


print("Example 5")
'''
Write a program that gets a word from the user and checks if 
it has any letter "E"s in the word
'''
word = input("Enter a word: ")

countEs = 0
for letter in word: #look at each letter in the word, one at a time
    if letter == "E" or letter == 'e': #if we find a letter E - problem of capitalization?
        countEs += 1 #add 1 to the count so far
        
print(f"The number of Es is {countEs}")