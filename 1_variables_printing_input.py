#num = 2
#print(num)
#print("Hello world!")

#print(5+7)

#print(5+2*7)
'''
print(15/4)
print(15//4)
print(15**4)
print(15%4)
'''
#name = input("Enter your name: ")

#print("Hi",name)

#age = int(input("Enter your age: "))
#print(age+5) #person's age in 5 years

'''
This is
a multi line
comment
'''


'''
Write a program that asks 
the user for two numbers and prints their sum.
'''

#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

#print(num1+num2)

'''
Write a program that asks 
the user for a radius and 
calculates the area of a circle with 
that radius (use 3.14 for pi).
'''

radius = int(input("Enter a radius: "))


areaCircle = 3.14*radius**2
print(areaCircle)

'''
Write a program that asks the user for a length 
and width and calculates 
the area of a rectangle with 
those dimensions.
'''

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

areaRectangle = length*width

print(areaRectangle)


'''
Write a program that asks the user for a temperature in Fahrenheit 
and converts it to Celsius (use the 
formula C = (F - 32) * 5/9).
'''

fahrenheit = int(input("Enter a temperature in Fahrenheit"))

celsius =  (fahrenheit - 32) * 5/9

print(celsius)

'''
Write a program that asks 
the user for a number 
and prints its square 
and cube.
'''

number = int(input("Enter a number: "))

print(number**2)
print(number**3)

total = 2.99

print("The total cost is",total)

name = "Semira"

print("Hello my name is "+name)


def main():
   #Write a program that asks the user for two numbers and prints their sum.
    num1 = int(input("Enter the first number: ")) 
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(result)

    #Write a program that asks the user for a radius and calculates the area of a circle with that radius (use 3.14 for pi).
    radius = int(input("Enter the radius: "))
    area = 3.14*radius**2
    print(area)

main()