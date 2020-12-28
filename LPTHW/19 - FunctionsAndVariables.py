#this is a function taking in inputs of cheese & cracker count with ouputs including formatted strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % (cheese_count))
    print("You have %d boxes of crackers!" % (boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#this is chunk of code printing a string before calling the cheese and crackers functions with inputs of 20 and 30
print("We can just give the functions numbers directly:")
cheese_and_crackers(20,30)

#this chunk of code prints a string before declaring variables to be passed into the function cheese and crackers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#same patten but we can do math on the parameters we pass into the cheese and crackers function
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#again, same patterns but we can pass in variables and do math to the parameters we pass into functions
print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

#Write at least one function of your own and run it 10 different ways
def my_own(something_to_say,number_to_switch_on):
    print("So you said %r" % (something_to_say))
    repeat_something = something_to_say
    if number_to_switch_on == 0:
        print("you probably didn't it say it enough times")
    else:
        print(repeat_something*number_to_switch_on)
        print("Ok. You'd think %r would be enough times for me to hear you" % (number_to_switch_on-1))

my_own("Blah",0)
my_own("Blah",2)
my_own("Blah blah",0)
my_own("Blah blah",1)
my_own("Blah blah",2)
my_own("10 times is a lot of times",0)
my_own("At least I'll remember functions",0)
my_own("AT LEAST I'LL REMEMBER FUNCTIONS!",3)
my_own("I adjusted my function to output the what I said by the number of times I repeat it", 0)
my_own("10 never looked so good", 2)

