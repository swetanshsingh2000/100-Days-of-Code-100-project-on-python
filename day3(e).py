print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")  
name2 = input("What is their name?") 
combine_names = name1+name2
#combining name so it can be read as a string 
lowercase = combine_names.lower()
#making all of the name in lowercase to avoid confusion 
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
#counting the number of times the words have been repeted and then adding them 
first_digit = t+r+u+e
#doing the similar thing with this word
l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
second_digit = l+o+v+e
#adding them as a str as per game rule as each digit should be combined and not added
score= str(first_digit)+str(second_digit)
num_score= int(score)
#printing the love result
if num_score<10 or num_score>90:
  print(f"Your score is {score}, you go together like coke and mentos. ")
elif num_score>=40 and num_score<=50 :
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  