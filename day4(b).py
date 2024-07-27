import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock, paper, scissors]

players= input("let's play a game of rock/ paper/ scissors\n")

if players=="rock":
    players=0
elif players=="paper":
    players=1
elif players=="scissors":
    players=2
else:
    print("Worng input choose from rock/ paper/ scissors")


print(game_images[players])
computer= random.randint(0,2)
print("computer have choosen ",game_images[computer])
if computer==0 and players==2:
    print("You loss!")
elif computer==2 and players==0:
    print("You win!!")
elif computer>players:
    print("you loss!")
elif players> computer:
    print("You win!!")
elif computer==players:
    print("its a draw (-_-)")