#This script contains: Write down every word and symbol you have used.
#Next to each word or symbol, write its name and what it does

#a '#' is a comment chracter to exclude what follows from execution
#notes
#this is sets the value of variable x equal to the value of a string
x = "string"
#variable y contains a formatted string passed in by the %d parameter
y = "There are %d types of people." % 10
#this outputs the value stored in string x
print(x)
#this outputs the values of the strings stored in x and y variables
print(x+y)
#the variable formatter stores formatting parameters
formatter = "%r %r"
#this characters creates a new line when outputting strings
#\n
#output several lines of strings
print('''
this outputs several lines
like this one
and this one
''')
#output is indented
tabby_cat = "\tI'm tabbed in."
#output splits string into 3 words
backslash_cat = "I'm \\ a \\ cat."
#output is a list of 4 indented strings
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#the comma is used at the end of each print line so the print does end with a new line character and go to the next line
print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
#more efficient way of entering inputs
age = input("How old are you? ")
#argv is an argument variable, this holds the arguments you pass to your Python script when you run the script
from sys import argv
#The unpacking... take whatever is in argb, unpack it, and assign it to all these variables on the left in order."
script, first, second, third = argv
#declare a variable to open the file passed into the script when it's running
# txt = open(filename)
# #Here's where the text is printed out to the console from the filename passed into the txt argv above
# print(txt.read())
# #this line closes the variable we opened through the txt declaration above
# txt.close()
# #this method resizes the file to the given number
# truncate()
# #copy file into a variable
# to_file = open(from_file, 'w')
#this is a function taking in inputs of cheese & cracker count with ouputs including formatted strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % (cheese_count))
    print("You have %d boxes of crackers!" % (boxes_of_crackers))
#creating a function to print whatever file is passed into this function
def print_all(f):
    print(f.read())
#this function alters the position of a file, the [0] position being at the beginning of the file at the first byte
def rewind(f):
    f.seek(0)