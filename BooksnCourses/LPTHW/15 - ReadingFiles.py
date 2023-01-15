#this imports the argv module from the Python sys package to be able to use the argv function
from sys import argv

#this is where we declare what parameters we'll pass into argv for the user to fill out when they run this script from the command line
script, filename = argv

#declare a variable to open the file passed into the script when it's running
txt = open(filename)

#A output to direct the user to what filename was read
print("Here's your file %r:" % filename)
#Here's where the text is printed out to the console from the filename passed into the txt argv above
print(txt.read())
#this line closes the variable we opened through the txt declaration above
txt.close()

#a prompt to direct the user to what file to open again
print("Type the filename again:")
#a variable to hold user input from the prompt above
file_again = input("> ")

#depending on what was entered in the previous prompt declares the txt_again entered in from the user input entered
txt_again = open(file_again)

#print the text read from the txt_again variable which was gathered from the file_again prompt to the user
print(txt_again.read())

#again, we're closing the file we first opened in the declaration of the variable above
txt_again.close()

#Revisit
#I don't understand why it's important for a user to close a file or database after reading or using it
#Maybe it's just more processing power on the computer if the file or database is excessively large?
#This makes sense. I haven't meandered to files of this size so it's difficult to say
