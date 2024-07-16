#IMPORTANT: to avoid issues, run the examples below one at a time
#by un-commenting each block of code. When finished with the example, add the block quotes back.


# read one name at a time

'''
with open('names.txt', 'r') as data:
  line = data.readline()
  print(line)

  line = data.readline()
  print(line)

'''

#read all the names in the file with a for loop

'''
names = []
with open('names.txt','r') as data:
  for name in data.readlines():
    name = name.strip() #remove extra white space
    names.append(name)
print(names)
'''

#add a new name to the end of the file
'''
with open('names.txt', 'a') as data:
  data.write("\nSarina") #note the addition of a new line character \n to make the name appear on a new line
'''

#overwriting the file
#when you overwrite a file programmatically there is no "UNDO" button - be very careful!

'''
with open('names.txt', 'w') as data:
  data.write("Logan")
'''


#fixing the mistake of overwriting

'''
addnames = ['Benedict', 'Georgia', 'Sam', 'Edith', 'Sarah', 'Siddarth']

# write each name into the file again with a for loop
with open('names.txt', 'a') as data:
  for name in addnames:
    data.write("\n")
    data.write(name)

'''

#working with CSVs.. create a list to contain the data for every column you need

''' #start csv example

firstNames = []
lastNames = []
ages = []
countAges = 0 
sumAges = 0
with open("data.csv","r") as file:
#read each row but only look at the first column
  file.readline() # read the first line, which is the column headers, to avoid adding them to the list of names
  #file.readlines() gives a list which contains every row of the spreadsheet
  #since the values for each column in a row are comma separated, split the values based on a comma to separate the values (this creates a new list)
  
  #print(file.readlines()) #prints a list, where each element is an entire row of the CSV
  # IMPORTANT NOTE: you can only use file.readlines() ONCE within each context manager. 
  # This is because readlines() will read the entire contents of your file at once
  # If you try to use readlines() again, there is nothing left to read
  
  for line in file.readlines():
    #use line.split(',') to create a new list that separates the values based on commas
    row = line.split(',')

    print("Row: ", row) #print out each row, notice that all of the values are separated and in a new list

    firstName = row[0] #the first name will always be the first element

    firstNames.append(firstName) #add the name to a list of first names

    #last names are the 2nd column, index 1
    lastName = row[1]
    lastNames.append(lastName)

    age = int(row[2]) #get the third item in the new list which will always be the age - need to convert it to an integer
    
    sumAges += age #keep a running total of ages
    countAges += 1 #keep a total of how many ages there are

print("First Names: ", firstNames)
print("Last Names: ", lastNames)
print("Average age: ", sumAges/countAges)

''' #end CSV example