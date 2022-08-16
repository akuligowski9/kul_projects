from datetime import time
from random import random

from kul_projects.Harcoppa.JustBeFunny import gameRules, comedyCategory, comedyScenes
from kul_projects.Harcoppa.JustBeFunny.helperFunctions import invalid_command_helper, retry

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
    round_category = random.choice(comedyCategory.categories)
    round_scene = random.choice(comedyScenes.scenes)
    print("The category of comedy for this round: {}").format(round_category)
    print("The scene for this round: {}").format(round_scene)
    print("Would you like a description of {}? (Y/N)").format(round_category)
    describe_option()
    print("Would you like an example of {}? (Y/N)").format(round_category)
    example_option()
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


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time is up! Nice round!')


def describe_option(round_category):
    next = input("> ")
    if next.lower() == "y" or "yes":
        comedyCategory.category_description(round_category)
    elif next.lower() == "n" or "no":
        print("You've got this.")
    else:
        invalid_command_helper()


def example_option(round_category):
    next = input("> ")
    if next == round_category:
        comedyCategory.category_description()
        example_option()
    elif next == "N" or "No" or "no":
        print("You've got this.")
    else:
        invalid_command_helper()


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
        gameRules.display_rules()
    elif next == "Categories":
        comedyCategory.display_categories()
    elif next == "Scenes":
        comedyScenes.display_scenes()
    elif next == "Exit":
        end_game()
    else:
        retry()
