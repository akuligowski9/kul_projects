#the 3 statements declare variables
people = 30
cars = 30
buses = 50

#if the value of cars is greater than people, then print the following statement
if cars>people:
    print("We should take the cars.")
#if cars is not greater than peopl and if the value of cars is less than people, thenprint the following statement
elif cars<people:
    print("We should not take the cars.")
#if neither statements are true above then print the following statement
else:
    print("We can't decide.")

#if buses are greater than cars then print the following statement
if buses>cars:
    print("That's too many buses.")
#if the first if in this block is not true, and buses are less than cars, then print the following statement
elif buses<cars:
    print("Maybe we could take the buses.")
#if neither statements in this block are true then print the following
else:
    print("We still can't decide.")

#if people are greater than busses and buses is less than cars then print the following statement
if people>buses and buses<cars:
    print("Alright, let's just take the buses.")
#if no statements in this block are true then print the following statement
else:
    print("Fine, let's stay home then")
