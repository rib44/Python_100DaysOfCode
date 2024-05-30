import random
import sys

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

vals = [rock, paper, scissor]
# 0 1 2
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if(user<0 or user>2):
    print("Invalid input, You Lose")
    sys.exit()
print(vals[user])

computer = random.randint(0,2)
print(f"Computer choses: \n {vals[computer]}")

if(user == computer):
    print("This is a tie.")
elif(user == 0):
    if(computer == 1):
        print("You Lose")
    elif(computer == 2):
        print("You Win")
elif(user == 1):
    if(computer == 0):
        print("You Win")
    elif(computer == 2):
        print("You Lose")
elif(user == 2):
    if(computer == 0):
        print("You Lose")
    elif(computer == 1):
        print("You Win")
