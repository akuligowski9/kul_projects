import random
import time
from sys import exit

categories = ['Alternative Comedy', 'Anecdotal Comedy', 'Anti-Humor', 'Dark Comedy', 'Blue Comedy', 'Character Comedy',
              'Cringe Comedy',
              'Deadpan Comedy', 'Heritage Comedy', 'Improvisational Comedy', 'Insult Comedy', 'Musical Comedy',
              'Observational Comedy', 'One-liners', 'Physical Comedy', 'Prop Comedy', 'Shock Humor', 'Sketch Comedy',
              'Spoof',
              'Surreal Comedy', 'Topical Comedy / Satire', 'Wit / Wordplay']
scenes = ['Funerals', 'Suicide', 'Sitting at a red light', 'Ghosting', '9/11 - always remember',
          'Your loving partner', 'Drinking', 'Military', 'Fighting', '#metoo movement',
          'Abortion rally', 'Fitness', 'Religion', 'Cancer', 'Fishtanks', 'Candles',
          'Waiting in line at the grocery store', 'Rape', 'Pooping', 'Animals/pets',
          'Books', 'Armpits', 'Parents', 'That one family member...', 'Siblings', 'Talking with your crush',
          'At the dinner table', 'Cultural norms', 'Cyclists', 'Death', 'Sports', 'The Homeless',
          'Poverty', 'Yoga', 'Sleeping', 'Vacation', 'Technology', 'Government', 'Racism', 'Mental Illness']
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
    print("Would you like a description of %s? (Y/N)" % (round_category))
    describe_option()
    print("Would you like an example of %s? (Y/N)" % (round_category))
    example_option()
    print("For every turn you get one shuffle. Get a new category and round? (Y/N)")
    round_check()
    countdown(int(t))


def describe_option(round_category):
    next = input("> ")
    if next == "Y" or "Yes" or "yes":
        category_description(round_category)
    elif next == "N" or "No" or "no":
        print("You've got this.")
    else:
        print("Invalid command, try again!")
        category_helper()


def category_description(round_category):
    next = round_category
    if next == round_category:
        category_description()


def example_option(round_category):
    next = input("> ")
    if next == round_category:
        category_description()
        example_option()
    elif next == "N" or "No" or "no":
        print("You've got this.")
    else:
        print("Invalid command, try again!")
        category_helper()


def category_example(round_category):
    next = round_category
    if next == round_category:
        category_description()


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