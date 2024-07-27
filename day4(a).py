line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\n ") 

letter = position[0].lower() #turing letter into lowercase to avoid any confusion in scrip from input 
abc= ["a", "b", "c"] #Creating a new list that contains all possible letters 
#using .index to do the comparison 
letter_index = abc.index(letter) 
num_index = int(position[1])-1 

map[num_index][letter_index]= "X"

print(f"{line1}\n{line2}\n{line3}")