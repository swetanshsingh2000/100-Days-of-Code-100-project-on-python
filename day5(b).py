# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score= 0
for score in student_scores:
  if max_score<score:
    max_score=score
  else:
    max_score==max_score
print("The highest score in the class is:" ,max_score)