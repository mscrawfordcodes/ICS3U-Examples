def add(a, b):
  result = a + b
  print("Line 3", result)
  return result 


def main():
  x = int(input("Num 1: "))
  y = int(input("Num 2: "))

  calculation = add(x, y)

  print("Line 13", calculation)
  
  if calculation > 10:
    print("Result of addition is greater than 10!")

main()