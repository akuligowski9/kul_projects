from kul_projects.Harcoppa.JustBeFunny import gameRules, comedyCategory, comedyScenes
from kul_projects.Harcoppa.JustBeFunny.helperFunctions import invalid_command_helper, retry


def start_game():
    print("Welcome to Just Be Funny!")
    print("The improv game to be played from the comfort of your home")
    print("It looks like you could use a laugh...")
    main_menu()


def end_game():
    print("Thanks for playing Just Be Funny!")
    exit()


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


def round_check():
    next = input("> ")
    if next == "Y" or "Yes" or "yes":
        round()
    elif next == "N" or "No" or "no":
        print("Ha! This ought to be good. Ok. Let's set a timer.")
    else:
        print("Invalid command, try again!")
        round_check()


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