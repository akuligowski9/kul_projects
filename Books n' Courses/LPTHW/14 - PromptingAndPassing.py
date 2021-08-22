from sys import argv

script, user_name = argv
#this is the beginning of the prompt for each time the user adds input to this script when executing
prompt = '*** '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# the string formatter here is used by passing in the likes, lives, and computer
# input given by the user in the questions prompting the user specified above
print('''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. 
And you have a %r computer. Nice. 
''' % (likes, lives, computer)
)