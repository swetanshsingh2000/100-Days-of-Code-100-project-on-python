# Enter your height in meters e.g., 1.55
height = float(input("what is ur height? "))
# Enter your weight in kilograms e.g., 72
weight = int(input("what is ur weight? "))

cal_bmi = weight/height**2
if cal_bmi<=18.5:
  print(f"Your BMI is {cal_bmi}, you are underweight.")
else:
  if cal_bmi<25:
    print(f"Your BMI is {cal_bmi}, you have a normal weight.")    
  else:
    if cal_bmi<=30:
      print(f"Your BMI is {cal_bmi}, you are slightly overweight.")
    else:
      if cal_bmi<=35:
        print(f"Your BMI is {cal_bmi}, you are obese.")
      else:
        print(f"Your BMI is {cal_bmi}, you are clinically obese.")
        