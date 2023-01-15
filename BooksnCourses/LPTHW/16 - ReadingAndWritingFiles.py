# File commands to remember per Shaw
#  • close—Closes the file. Like File- >Save.. in your editor.
#  • read—Reads the contents of the file. You can assign the result to a variable.
#  • readline—Reads just one line of a text fi le.
#  • truncate—Empties the file. Watch out if you care about the fi le.
#  • write(stuff)—Writes stuff to the file.

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
#per pydoc we have to pass in 'w' as a parameter here to "open it for writing, truncating the file first"
#Here are the parameters avaialble to pass into open ~ open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#'w' is just the mode here
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to one file.")

#this is much more efficient than what was here originally, see what's commented out below
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()