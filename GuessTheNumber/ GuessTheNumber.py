#Guess The Number! 

import random

#Create variables
randomv = 0
parameters = [1,2,3,4,5,6,7,8,9,10]

#Randomly generating a number into variable with a range from 1-10
randomv = random.choice(parameters)

#Get input from user to select an integer from 1-10
print("Welcome to Guess The Number!")
uinput = input("Enter value between 1 and 10:")

while uinput != ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10):
	print("Invalid input! Try again with an integer between 1 and 10")
	uinput = input()
		
#Start loop to repeat randomly generated number
while randomv != uinput:
  
#Does random output match random input from user
#If match, show the matching outputs to user
	print("Close but not close enough!")
	print(f'User input: {uinput} did not match random number between 1 and 10')
	print("Try again!")

#If not match, user can try again to keep match new random number
print("Good job!")
print(f'User input: {uinput} matches the randomly generated number input: {randomv}!')
