target = int(input()) # Enter a number between 0 and 1000

even_sum=0
for even in range(2,target+1,2):
  even_sum+= even
print(even_sum) 
