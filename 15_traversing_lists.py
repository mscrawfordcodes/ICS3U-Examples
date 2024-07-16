fruits = ["Apple", "Orange", "Kiwi", "Pear"] #creating a list

print(fruits) #print the entire list
print(fruits[0]) #print the first element/item in the list
print(fruits[-1]) #print the last element/item in the list

fruits[0] = "Banana" #change the first element of the list to "Banana"

print(fruits) #print the updated list

for fruit in fruits: #loop/iterate over the list and print out each fruit one at a time
  print(fruit)

for i in range(len(fruits)): #a second way of looping over the list, using range() and len()
  print(fruits[i])


print(fruits[1:3]) #use list slicing to print a smaller list containing the elements of fruit at index 1 and 2
print(fruits[::2]) #print "every other" (step of 2) element of the list


#this is the type of loop that must be used to UPDATE or CHANGE
#items in the list
#this loop will change all of the fruits in the list to be Dragonfruit
for i in range(len(fruits)):
  fruits[i] = "Dragonfruit"

print(fruits)
