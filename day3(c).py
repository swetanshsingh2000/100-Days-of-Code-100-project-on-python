print("welcome to rollercoster! ")
#height should be above 120cm
height =int(input("what is ur height in cm? "))
#age can be any thingh if it clears the height requirement
age = int(input("wat is ur age?"))
bill=0
if height>120:
  if age>=18:
    bill=12
    print("u can ride the rollercoster and pay $12")
  elif age<12:
    bill=5
    print("u can ride this rollercoster and pay $5")
  else:
    bill=7
    print("u can ride the rollercoster and pay $7")
  #if they want a photo
  photo=input("do u want a photo taken? y/n [u have to pay extra $3] ")
  if photo=="y":
    bill+=3
    print(f"Your total ticket amount will be ${bill}.")
#when they are not eligible to ride
else:
  print("sorry, u have to grow taller before u can buy the ticket")
  