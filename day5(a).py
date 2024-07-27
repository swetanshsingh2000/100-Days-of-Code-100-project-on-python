# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total_height = 0
for hcsa in student_heights:
  total_height += hcsa
print(f"total height = {total_height}")
num_student = 0
for stud in student_heights:
  num_student+=1
print(f"number of students = {num_student}")
avg=total_height/num_student
avg= round(avg)
print(f"average height = {avg}")