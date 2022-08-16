from datetime import time

from kul_projects.Harcoppa.JustBeFunny.roundNavigation import main_menu

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


def invalid_command_helper():
    error = "You've entered an invalid command. Please enter Yes or No. Also Y/N will also work. Try again!"
    raise AttributeError(error)