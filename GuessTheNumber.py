#Guess The Number Game! 

from random

#Create variables
randomv = 0
uinput = 1
parameters = [1,2,3,4,5,6,7,8,9,10]

#Start loop to repeat randomly generated number
if (randomv != uinput)
  {
#Randomly generating a number into variable with a range from 1-10
  randomv = random.choice(parameters)

#Input of a number from the user in another variable
  uinput = input("Enter value between 1 and 10")
  
#Does random output match random input from user

#If match, show the matching outputs to user
print(Close but not close enough!)
print(f'User input: {uinput}')
print(f'Randomly generated number input: {randomv}')
print(Try again!)

#If not match, user can try again to keep match new random number
print(Good job!)
print(f'User input: {uinput} matches the randomly generated number input: {randomv}!')