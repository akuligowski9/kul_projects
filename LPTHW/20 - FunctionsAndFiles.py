# we're importing the argv package from the sys library
from sys import argv

# this defines the parameters we must pass in to run this script
script, input_file = argv

#creating a function to print whatever file is passed into this function
def print_all(f):
    print(f.read())

#this function alters the position of a file, the [0] position being at the beginning of the file at the first byte
def rewind(f):
    f.seek(0)

#this function takes in an int and file; followed by outputting a single line of a file
def print_a_line(line_count, f):
    print(line_count,f.readline())

#whatever file is passed as the input_file from the terminal
current_file = open(input_file)

#output string and call of function above
print("First let's print the whole file:\n")
print_all(current_file)

#output string and call of function above
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

#output and call of function above several times while updating the current_line variable to change the positioning of what's outputted
print("Let's print three lines:")

current_line=1
print_a_line(current_line, current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)