numsList = [1, 2, 2, 3, 4, 5]

print(numsList)

numsList.append(6) #add 6 to end of list

print(numsList)

numsList.pop(0) #delete first item

print(numsList)

numsList.pop(3) #delete item at index 3

print(numsList)

numsList.pop(-1) #delete last item in the list

print(numsList)

numsList.insert(2,3) #at index 2, insert number 3

print(numsList)

print("The number of 2s is", numsList.count(2)) # count the number of 2s in the list

print("2 occurs at index", numsList.index(2))


#find and print out all the indexes that 2 occurs at
#len(numsList) works because we stop at this value and do not proceed in the loop, so no index out of range issues
for index in range(0, len(numsList)):
  if numsList[index] == 2:
    print(index, end=" ")


# checking for values in or not in the list
if 3 in numsList:
  print("\n3 is in the list")

if 7 not in numsList:
  print("7 is not in the list")


print(numsList[1:3]) # get list from index 1 to, but not including, index 3

#print every 2nd element in the list
print(numsList[::2])

#reverse the list
print(numsList[::-1])


animal1, animal2 = "Lions Tigers".split()

print(animal1)
print(animal2)

animalList = "Lions Tigers".split()
print(animalList)

for item in animalList:
  print(item)

# take numbers entered on a single line and put them into a list
nums = input().split()
print(nums)
# convert each item in the list to an int, then add 1 to it
for index in range(0, len(nums)):
  nums[index] = int(nums[index]) + 1

print(nums)

fruits = ["apples","bananas","oranges","kiwi", "bananas"]

fruits.append("strawberries") #adds to the end

print(fruits)

fruits.insert(0,"dragonfruit") #adds as the first element

print(fruits)

fruits.pop(-1) #deletes the last element
print(fruits)

numBananas = fruits.count("bananas") #counts the number of specified values
print(numBananas)

#by default will split on a space,
#can add other characters to split on:
animals = input().split(",")

#if you separate by a comma ONLY, data may be entered like so:
#goat, sheep, pig, cat
#the extra spaces between the animals will result in an extra space being added at the FRONT of each separate string
# the list would look like this, note the extra spaces: ["goat", " sheep", " pig", " cat"]
#loop over the list and strip off the extra whitespace
for index in range(len(animals)):
    animals[index] = animals[index].strip()

print(animals)

# alternatively, you can add additional characters to the split method. input().split(", ") will include the extra space to split the values apart. 
# But it might not solve the problem of users accidentally typing in extra spaces!