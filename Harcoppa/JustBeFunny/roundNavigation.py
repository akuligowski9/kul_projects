from random import choice
from time import sleep

from kul_projects.Harcoppa.JustBeFunny.comedyCategory import categories, category_description, display_categories
from kul_projects.Harcoppa.JustBeFunny.comedyScenes import scenes, display_scenes
from kul_projects.Harcoppa.JustBeFunny.helperFunctions import invalid_command_helper
from sys import exit

t = input("Enter the time in seconds you'd like for this round: ")


def start_game():
    print("Welcome to Just Be Funny!")
    print("The improv game to be played from the comfort of your home")
    print("It looks like you could use a laugh...")
    main_menu()


def end_game():
    print("Thanks for playing Just Be Funny!")
    exit()


def round():
    round_category = choice(categories)
    round_scene = choice(scenes)
    round_prep = """
                 The category of comedy for this round: {} \n
                 The scene for this round: {} \n 
                 Would you like a description of {}?
                 """
    print(round_prep.format(round_category, round_scene, round_category))
    describe_option(round_category)
    print("Would you like an example of %s? (Y/N)" % round_category)
    example_option(round_category)
    print("For every turn you get one shuffle. Get a new category and round? (Y/N)")
    round_check()
    countdown(int(t))


def round_check():
    next = input("> ")
    if next.lower() == "y" or "yes":
        round()
    elif next.lower() == "n" or "no":
        print("Ha! This ought to be good. Ok. Let's set a timer.")
    else:
        print("Invalid command, try again! Accepted values are 'yes and y' or 'no and n'")
        round_check()


def retry():
    print("Invalid command, try again!")
    main_menu()


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1
    print('Time is up! Nice round!')


def describe_option(round_category):
    next = input("> ")
    if next.lower() == "y" or "yes":
        category_description(round_category)
    elif next.lower() == "n" or "no":
        print("You've got this.")
    else:
        invalid_command_helper()


def example_option(round_category):
    next = input("> ")
    if next == round_category:
        category_description(round_category)
        example_option(round_category)
    elif next == "N" or "No" or "no":
        print("You've got this.")
    else:
        invalid_command_helper()


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


def main_menu():
    print("Enter one of the following:")
    print("""
\t* Play 
\t* Rules
\t* Categories
\t* Scenes
\t* Exit
""")

    next = input("> ")

    if next.lower() == "play":
        round()
    elif next.lower() == "rules":
        display_rules()
    elif next.lower() == "categories":
        display_categories()
    elif next.lower() == "scenes":
        display_scenes()
    elif next.lower() == "exit":
        end_game()
    else:
        retry()
