from kul_projects.Harcoppa.JustBeFunny.roundNavigation import main_menu


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