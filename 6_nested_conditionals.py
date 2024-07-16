attendanceType = input("Absence or Late? ")
attendanceNumber = int(input("How many attendance issues? "))

#check the absences issues
if attendanceType == "absence":
  #could also use individual if statements here if we wanted multiple notifications to be sent
  if attendanceNumber >= 10:
    print("Email to principal sent")
  elif attendanceNumber >= 5:
    print("Email to parent sent")
  elif attendanceNumber >= 2:
    print("Email to student sent")

#check lateness issues
elif attendanceType == "late":
  if attendanceNumber >= 20:
    print("Email to principal sent")
  elif attendanceNumber >= 10:
    print("Email to parent sent")
  else: #email student, 5 lates
    print("Email to student sent")





# if we did not use nested conditionals this is what our code could look like
#notice the redundancy of having to check the attendance type multiple times as part of each condition
#if we had other conditions to check (e.g. whether the attendance issue was consistent or sporadic) this condition would get very long and potentially hard to read
'''
if attendanceType == "absence" and attendanceNumber >= 10:
  print("Email to principal sent")
elif attendanceType == "absence" and attendanceNumber >= 5:
  print("Email to parent sent")
'''