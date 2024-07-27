# Which year do you want to check?
year = int(input("Which year do you want to check?\n"))

# Write your code below this line 👇
leap_year_test1= year%4

if leap_year_test1==0:
  leap_year_test2= year%100
  if leap_year_test2==0:
    leap_year_test3= year%400
    if leap_year_test3==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
     print("Leap year")
else:
   print("Not leap year")