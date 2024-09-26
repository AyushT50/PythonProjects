import random

"""
Number Guessing Game

This script generates a random number between 1 and 100 and allows the user to 
guess the number through a series of hints. The user can quit the game anytime 
by entering 'Q'.
"""

# Generate a random target number between 1 and 100
target = random.randint(1, 100)

# Game loop
while True:
    user_choice = input("Enter your guess or quit (Q): ")

    # Exit condition
    if user_choice.upper() == "Q":
        print("You have quit the game.")
        break

    # Convert the user's input to an integer
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Invalid input! Please enter a number or 'Q' to quit.")
        continue

    # Compare the guess to the target number
    if user_choice == target:
        print("Success: Correct Guess!")
        break
    elif user_choice < target:
        print("Your guess is too low. Try a bigger number...")
    else:
        print("Your guess is too high. Try a smaller number...")

# End of game
print("-----GAME OVER-----")
