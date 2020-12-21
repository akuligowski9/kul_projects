# variable declaration with a formatted variable of 10
x = "There are %d types of people." % 10
# standard variable declarations
binary = "binary"
do_not = "don't"
# variable declaration with two formatted variables previously defined above
y = "Those who know %s and those who %s" % (binary, do_not)

# output of variables x and y
print(x)
print(y)

# output containing an object representation, a new object, of x
print("I said %r." % x)
# output containing a string, str output, representation of y
print("I also said: '%s'." % y)

# variable declaration of hilarious with boolean value
hilarious = False

# variable declaration including an object representation variable at the end of the string
joke_evaluation = "Isn't that joke so funny?! %r"

# output of joke evaluation variable with the string formatted to include the hilarious variable
print(joke_evaluation % hilarious)

# variable declaration of two strings
w = "This is the left side of..."
e = "a string with a right side."

# an example of how binary operations can be applied to string variables to combine two strings
print(w+e)
