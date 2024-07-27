#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill=float(input("what is the total amount of the bill? $\n"))
tip=int(input("what percentage of tip u want to give from 5,10,12,15? or more if u wishe to or zero if u dont want to tip\n"))
if tip==0:
  total_amount_of_tip=0
  tip_by_each_person=0
  print("ok")
else:
  people=int(input("how many people to splitt the bill with?\n"))
  tip_as_percentage= tip/100
  total_amount_of_tip= bill*tip_as_percentage
  tip_by_each_person= total_amount_of_tip/people
total_bill= bill+total_amount_of_tip
print (f"Total amount is {total_bill} Group have tipped $ {total_amount_of_tip} and ur tip is ${tip_by_each_person} ")