import random
import time
from kul_projects.Harcoppa.JustBeFunny.ComedyCategory import display_categories, category_description, category_helper
from kul_projects.Harcoppa.JustBeFunny.ComedyScenes import display_scenes
import
from sys import exit

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
    print("The category of comedy for this round: %s" % (ComedyCategory.round_category))
    print("The scene for this round: %s" % (round_scene))
    print("Would you like a description of %s? (Y/N)" % (ComedyCategory.round_category))
    describe_option()
    print("Would you like an example of %s? (Y/N)" % (ComedyCategory.round_category))
    example_option()
    print("For every turn you get one shuffle. Get a new category and round? (Y/N)")
    round_check()
    countdown(int(t))


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
        category_description()
        example_option()
    elif next == "N" or "No" or "no":
        print("You've got this.")
    else:
        invalid_command_helper()

def invalid_command_helper():
    error = "You've entered an invalid command. Please enter Yes or No. Also Y/N will also work. Try again!"
    raise AttributeError(error)

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