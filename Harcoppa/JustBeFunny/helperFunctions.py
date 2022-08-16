from kul_projects.Harcoppa.JustBeFunny.roundNavigation import main_menu


def retry():
    print("Invalid command, try again!")
    main_menu()


def invalid_command_helper():
    error = "You've entered an invalid command. Please enter Yes or No. Also Y/N will also work. Try again!"
    raise AttributeError(error)