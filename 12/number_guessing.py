import art
import random



def main():
    print(art.logo)
    print("Welcome to the Number Try Game!")

    number = random.randint(1, 100)
    
    print("I'm thinking of a number between 1 and 100.")
    print(f"Ans is: {number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        level = 10
    elif difficulty == 'hard':
        level = 5

    keep_playing = True

    while keep_playing and level > 0:
        print(f"You have {level} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The number was {guess}.")
            keep_playing = False
        elif guess > number:
            print("Too high.\nGuess again.")
        elif guess < number:
            print("Too low.\nGuess again.")

        level -= 1
        
    if level == 0:
        print("You've run out of guesses, you lose.")

    
if __name__ == "__main__":
    main()