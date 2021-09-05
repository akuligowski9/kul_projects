# a little warm project
# goal: when running the program you get the output of two dice
import time
import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

count = 0

x = input('Enter your name: ')
print('Welcome to the Dice Roll Simulator, ' + x)
y = input('How many sides does each dice have? (min 2, max 10)')
z = input('How many dice would you like to roll? (min 1, max 5)')
print('Uno momento por favor')
print('Rolling dice...')
time.sleep(2)
print('Rolling dice...')
time.sleep(2)
print('Rolling dice...')
time.sleep(2)

while count < z:
    print(random.randint(1,y))
    count += 1