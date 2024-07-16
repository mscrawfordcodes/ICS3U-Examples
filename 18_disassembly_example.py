def isEven():
  x = 4
  if x%2 == 0:
    return 'yes'
  else:
    return 'no'














import dis
dis.dis(isEven)

#print(list(isEven.__code__.co_code))

#print(dis.opname[100])


#print(dis.opname[125])