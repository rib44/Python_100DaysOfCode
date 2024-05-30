
print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
choice1 = input("You\'re at a crossroad, where do you want to go? Type \"left\" or \"right\".").lower()

if choice1 == "left":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wiat for a boat. Type \"swim\" to swim across.").lower()

    if(choice2 == "wait"):
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()

        if(choice3 == "yellow"):
            print("Game Over")
        elif(choice3 == "red"):
            print("You Win")
        else:
            print("You Fool, Try Again!")
    else:
        print("Game Over")

else:
    print("You fell into a hole. Game Over.")