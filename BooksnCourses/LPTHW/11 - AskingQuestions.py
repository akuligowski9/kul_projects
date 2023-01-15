#the comma is used at the end of each print line so the print does end with a new line character and go to the next line
print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input()

print("So you're %r old, %r tall and %r heavy." % (age, height, weight))

#this exercise originally included the raw_input function which is deprecated in Python 3