# Guess The Number Game!
import random

# Create variables
parameters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Randomly generating a number into variable with a range from 1-10
randomv = random.choice(parameters)
print(f'{randomv})

# Get input from user to select an integer from 1-10
print("Welcome to Guess The Number!")
uinput = int(input("Enter value between 1 and 10: "))

# Check if user input is within range of parameters of the game
if uinput not in parameters:
    uinput = input('Invalid input! Try again with an integer between 1 and 10: ')
elif uinput in parameters:
    # Check if random output matches random input from user
    while uinput != randomv:
        print('Close but not close enough!')
        print(f'User input: {uinput} did not match the random number between 1 and 10')
        # If not match, user can try again to keep match new random number
        uinput = input("Try again!: ")
    if uinput == randomv:
        print('Good job!')
        # If match, show the matching outputs to user
        print(f'User input: {uinput} matches the randomly generated number input: {randomv}!')