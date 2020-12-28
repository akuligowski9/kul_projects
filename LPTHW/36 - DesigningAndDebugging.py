# RULES FOR IF-STATEMENTS
# 1. Every if- statement must have an else.
# 2. If this else should never be run because it doesn’t make sense, then you must use a die
# function in the else that prints out an error message and dies, just like we did in the last
# exercise. This will fi nd many errors.
# 3. Never nest if- statements more than two deep and always try to do them one deep.
# This means if you put an if in an if, then you should be looking to move that second if
# into another function.
# 4. Treat if- statements like paragraphs, where each if, elif, else grouping is like a
# set of sentences. Put blank lines before and after.
# 5. Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.
#
# RULES FOR LOOPS
# 1. Use a while- loop only to loop forever, and that means probably never. This only applies
# to Python; other languages are different.
# 2. Use a for- loop for all other kinds of looping, especially if there is a fi xed or limited
# number of things to loop over.
#
# TIPS FOR DEBUGGING
# 1. Do not use a “debugger.” A debugger is like doing a full- body scan on a sick person. You
# do not get any specifi c useful information, and you fi nd a whole lot of information that
# doesn’t help and is just confusing.
# 2. The best way to debug a program is to use print to print out the values of variables at
# points in the program to see where they go wrong.
# 3. Make sure parts of your programs work as you work on them. Do not write massive fi les
# of code before you try to run them. Code a little, run a little, fi x a little.

import random
import time
from sys import exit

categories = ['Alternative Comedy', 'Anecdotal Comedy', 'Anti-Humor', 'Dark Comedy', 'Blue Comedy', 'Character Comedy', 'Cringe Comedy',
              'Deadpan Comedy', 'Heritage Comedy', 'Improvisational Comedy', 'Insult Comedy', 'Musical Comedy',
              'Observational Comedy', 'One-liners', 'Physical Comedy', 'Prop Comedy', 'Shock Humor', 'Sketch Comedy', 'Spoof',
              'Surreal Comedy', 'Topical Comedy / Satire', 'Wit / Wordplay']
scenes = ['Funerals', 'Suicide', 'Sitting at a red light', 'Ghosting', '9/11 - always remember',
          'Your loving partner', 'Drinking', 'Military', 'Fighting', '#metoo movement',
          'Abortion rally', 'Fitness', 'Religion', 'Cancer', 'Fishtanks', 'Candles',
          'Waiting in line at the grocery store', 'Rape', 'Pooping', 'Animals/pets',
          'Books', 'Armpits','Parents','That one family member...','Siblings','Talking with your crush',
          'At the dinner table','Cultural norms','Cyclists','Death','Sports','The Homeless',
          'Poverty','Yoga','Sleeping','Vacation','Technology', 'Government', 'Racism', 'Mental Illness']
t = input("Enter the time in seconds you'd like for this round: ")

def retry():
    print("Invalid command, try again!")
    main_menu()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Nice round!')

def round_check():
    next = input("> ")
    if next == "Y" or "Yes" or "yes":
        round()
    elif next == "N" or "No" or "no":
        print("Ha! This ought to be good. Ok. Let's set a timer.")
    else:
        print("Invalid command, try again!")
        round_check()

def round():
    round_category = random.choice(categories)
    round_scene = random.choice(scenes)
    print("The category of comedy for this round: %s" % (round_category))
    print("The scene for this round: %s" % (round_scene))
    print("For every turn you get one mulligan. Get a new category and round? (Y/N)")
    round_check()
    countdown(int(t))
    

def display_rules():
    print('''Per turn you get:
    \t* A Time Limit (We recommend two minutes)
    \t* A Category of Comedy
    \t* A Scene or Topic
    ...And just be funny!
    
    Scoring per turn: (4 points possible per round)
    \t* Is it funny (2 points)
    \t* Did you use the category of comedy? (1 point)
    \t* Did you use the scene or topic? (1 point)
    
    In a round, every player gets a turn. First player to 12 points wins. 
    Sudden death if multiple players hit 12 points in a round. 
    For sudden death, a single turn will be taken by every player over 
    12 points using the same time limit, category of comedy, and scene. 
    ''')
    main_menu()

def display_scenes():
    for scene in scenes:
        print("\t*%s\n" % scene)

def display_categories():
    for category in categories:
        print("\t*%s\n" % category)

def start():
    print("Welcome to Just Be Funny!")
    print("The improv game to be played from the comfort of your home")
    print("It looks like you could use a laugh...")
    main_menu()

def end_game():
    print("Thanks for playing Just Be Funny!")
    exit()

def main_menu():
    print("Select one of the following:")
    print("""
\t* Play!
\t* Rules
\t* Categories
\t* Scenes
\t* Exit
""")

    next = input("> ")

    if next == "Play!":
        round()
    elif next == "Rules":
        display_rules()
    elif next == "Categories":
        display_categories()
    elif next == "Scenes":
        display_scenes()
    elif next == "Exit":
        end_game()
    else:
        retry()

start()