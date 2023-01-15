#argv is an argument variable, this holds the arguments you pass to your Python script when you run the script
from sys import argv

#The unpacking... take whatever is in argb, unpack it, and assign it to all these variables on the left in order."
script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# we use import to add features (modules or libraries) to a script from the Python feature set (better known as modules or libraries)

uinput = input("Now give me a little script input...")
print("And with '%r' that's command line input and script input in a script - neat!" % uinput)
